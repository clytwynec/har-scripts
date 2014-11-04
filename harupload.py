"""
A basic python script for posting HAR files to a HarStorage server.
Adapted from https://code.google.com/p/harstorage/wiki/PythonTutorial.

Args: 
    Path to HAR file or directory containing har files to be uploaded.

Options:
    --port    PORT to connect to for posting the HAR (default: 5000)
    --host    HOST to connect to for posting the HAR (default: 'localhost')

Example:
    python /path/to/HAR/file.har --port 8000 --host 127.0.0.1
"""
import httplib
import urllib
import os
import requests 
import argparse


class HttpRequest():

    def __init__(self, hostname, port):
        self.hostname = hostname
        self.port = port


    def send(self, method, path, body=None, headers=None):
        connection = httplib.HTTPConnection(self.hostname, self.port)

        if body is not None and headers is not None:
            connection.request(method, path, body, headers)
        else:
            connection.request(method, path)

        response = connection.getresponse().read()
        connection.close()

        return response


class HarStorage():

    def __init__(self, host, port):
         self.http_request = HttpRequest(host, port)

    def save(self, har):
        with open(har) as file:
            path = "/results/upload"
            headers = {
                "Content-type": "application/x-www-form-urlencoded", 
                "Automated": "true",
            }
            body = urllib.urlencode({"file": file.read()})
            return self.http_request.send("POST", path, body, headers)

    def post_har(self, filepath):
        try:
            print "Uploading {} ... ".format(os.path.basename(filepath)),
            print self.save(filepath)
        except:
            pass


if __name__ == "__main__":

    parser = argparse.ArgumentParser(prog='myprogram')
    parser.add_argument('harpath', help="Path to HAR file or directory containing har files to be uploaded")
    parser.add_argument('--host', default='localhost', help="HOST to connect to for posting the HAR (default: 'localhost')")
    parser.add_argument('--port', default=5000, help="PORT to connect to for posting the HAR (default: 5000)")
    args = parser.parse_args()

    harpath = os.path.realpath(args.harpath)
    store = HarStorage(args.host, args.port)


    # The input is a file, just send it.
    if os.path.isfile(harpath):
        store.post_har(harpath)  
    # The input is a directory, send any har files from it,
    elif os.path.isdir(harpath):
        for dirpath,_,filenames in os.walk(harpath):
            for f in filenames:
                if f.endswith('.har'):
                    p = os.path.realpath(os.path.join(dirpath, f))
                    store.post_har(p)
    # The input is neither a file or a directory, do nothing.
    else:
        print "Can't find file or directory {}".format(harpath)
