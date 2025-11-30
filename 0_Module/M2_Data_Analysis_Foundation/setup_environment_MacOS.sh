#!/bin/bash
python -m venv daf_venv
source daf_venv/bin/activate
pip install -r requirements.txt
python -m ipykernel install --user --name=daf_venv --display-name="DAF Python"
