#!/bin/sh
sudo apt-get remove --purge -y python-virtualenv python-pip python-setuptools
wget https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py -O - | sudo python2.7
rm -f setuptools*.zip
sudo easy_install-2.7 -U pip
sudo pip2.7 install -U virtualenv