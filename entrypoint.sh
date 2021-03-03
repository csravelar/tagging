#!/bin/bash

set -eux

export checkmarx_config_path=${PWD}'/config.ini'
pip install -r $(dirname $(readlink -f $0))/requirements.txt
python3 $(dirname $(readlink -f $0))/create_checkmarx_ini_config.py
python3 $(dirname $(readlink -f $0))/tag_project.py
