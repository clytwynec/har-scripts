# -*- mode: ruby -*-
# vi: set ft=ruby :

# Reference: https://code.google.com/p/harstorage/wiki/Installation#Debian/Ubuntu/Mint_dependencies

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

$script = <<SCRIPT
# Install mongo and some python packages
sudo apt-get update
sudo apt-get install mongodb -y
sudo apt-get install lib32stdc++6 -y
sudo apt-get install build-essential python-dev -y
sudo apt-get install python -y
sudo apt-get install python-cairo -y
sudo apt-get install python-rsvg -y
sudo apt-get install python-setuptools -y
easy_install pylons==1.0
easy_install webob==0.9.8
easy_install pymongo
sudo easy_install  http://harstorage.googlecode.com/files/harstorage-1.0-py2.7.egg

echo  Provisioning Complete. To start server:
echo  ...$   vagrant ssh
echo  ...$   paster make-config harstorage local.ini
echo  ...$   paster setup-app local.ini
echo  ...$   paster serve local.ini
echo  Then go to localhost:5000 and wait for migrations to finish.
SCRIPT

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  # For reference, please see the online documentation at vagrantup.com.
  config.vm.box = "precise64"
  config.vm.network "forwarded_port", guest: 5000, host: 5000
end

Vagrant.configure("2") do |config|
  config.vm.provision "shell", inline: $script
end
