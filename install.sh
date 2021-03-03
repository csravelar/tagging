#!/usr/bin/env sh

set -ux

sudo -E yum update
sudo -E yum install curl git
sudo -E touch /usr/local/bin/lol.txt
sudo -E curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
sudo -E python3 get-pip.py
sudo -E git clone https://github.com/csravelar/tagging.git /usr/local/bin/tagging
echo "alias checkmarx_tag='bash /usr/local/bin/tagging/entrypoint.sh'" | sudo tee -a /etc/bashrc
