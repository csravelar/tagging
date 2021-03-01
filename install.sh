#!/usr/bin/env sh

set -ux

echo "LMFAO"
sudo -E yum update
sudo -E yum install curl git
sudo -E touch /usr/local/bin/lol.txt
sudo -E curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
sudo -E python get-pip.py
sudo -E git clone https://github.com/csravelar/tagging.git /usr/local/bin/tagging
sudo -E pip install -r /usr/loca/bin/tagging/requirements.txt
