#!/bin/bash

set -eux

pip install -r $(dirname $(readlink -f $0))/requirements.txt
export checkmarx_config_path=${PWD}'/config.ini'
python3 $(dirname $(readlink -f $0))/create_checkmarx_ini_config.py
python3 $(dirname $(readlink -f $0))/tag_project.py
