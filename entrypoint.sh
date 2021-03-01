#!/bin/bash

python3 $(dirname $(readlink -f $0))/create_checkmarx_ini_config.py
python3 $(dirname $(readlink -f $0))/tag_project.py
