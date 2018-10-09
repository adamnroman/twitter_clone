#!/usr/bin/env bash

#Install Python3's package manager
apt-get -y install python3-pip

# Install virtual environment
pip3 install virtualenv

#Use Virtualenv to provision a virtual environment with lib as name
virtualenv -p python3 --no-site-packages lib

#Instantiate a virtual environment
source lib/bin/activate

#Recursively isntall this project's dependencies
pip3 install -r requirements.txt
sudo apt-get -y install sqlite3
