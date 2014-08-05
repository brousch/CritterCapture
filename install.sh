#!/bin/sh

# Install system packages needed for this project
sudo apt-get update
cat system_packages.txt | xargs sudo apt-get -y install

# Create a virtualenv
rm -rf venv
virtualenv -p python2.7 venv

# Install required Python packages into the virtualenv
source venv/bin/activate
pip install -r requirements.txt
