## Overview

Currently, this is a quick way to get harstorage running locally and programatically feed it HAR files.


## Starting a harstorage server

From this directory, run `vagrant up`. Follow the instructions that print when provisioning is complete.


## Feeding HAR files

Use [harupload.py](https://github.com/clytwynec/har-scripts/blob/master/harupload.py) to feed hars. Use `python harupload.py -h` for details. Be sure to `pip install -r requirements` first.  There are a couple of sample har files in the [sample_data](https://github.com/clytwynec/har-scripts/tree/master/sample_data) folder.