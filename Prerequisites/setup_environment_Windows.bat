@echo off
python -m venv cas_gpu_venv
call cas_gpu_venv\Scripts\activate.bat
pip install -r prerequisites\requirements.txt
python -m ipykernel install --user --name=cas_gpu_venv --display-name="CAS GPU"