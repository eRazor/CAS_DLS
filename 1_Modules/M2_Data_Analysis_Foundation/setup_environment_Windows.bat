@echo off
python -m venv daf_venv
call daf_venv\Scripts\activate.bat
pip install -r requirements.txt
python -m ipykernel install --user --name=daf_venv --display-name="DAF Python"