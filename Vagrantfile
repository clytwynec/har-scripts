# -*- mode: ruby -*-
# vi: set ft=ruby :

# Reference: https://code.google.com/p/harstorage/wiki/Installation#Debian/Ubuntu/Mint_dependencies

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

$script = <<SCRIPT
# Install mongo and some python packages
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10
echo 'deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist 10gen' | sudo tee /etc/apt/sources.list.d/mongodb.list
sudo apt-get update -y
sudo apt-get install mongodb-org -y
sudo apt-get install lib32stdc++6 -y
sudo apt-get install build-essential python-dev -y
sudo apt-get install python -y
sudo apt-get install python-cairo -y
sudo apt-get install python-rsvg -y
sudo apt-get install python-setuptools -y
sudo apt-get install python-pip -y
sudo apt-get install git -y
sudo pip install -r /requirements/harstorage.txt

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
  config.vm.synced_folder "requirements", "/requirements"
end

Vagrant.configure("2") do |config|
  config.vm.provision "shell", inline: $script
end
