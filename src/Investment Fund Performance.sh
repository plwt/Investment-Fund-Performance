#!/bin/bash

cd /opt/Investment Fund Performance

python3 -m venv venv
source venv/bin/activate

# install requirements
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade datetime

# run the script
python3 /opt/WaterMarker/src/Investment Fund Performance.py

sleep 5m

deactivate

rm -r venv
