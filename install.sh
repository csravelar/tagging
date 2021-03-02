#!/usr/bin/env sh

set -ux

sudo -E bash <<EOF
yum update
yum install curl git
touch /usr/local/bin/lol.txt
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py
git clone https://github.com/csravelar/tagging.git /usr/local/bin/tagging
pip install -r /usr/loca/bin/tagging/requirements.txt
EOF
