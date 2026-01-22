@echo off
python -m venv cas_gpu_venv
call cas_gpu_venv\Scripts\activate.bat
pip install nvidia-cudnn-cu13
pip install nvidia-cuda-runtime
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu130

pip install -r prerequisites\requirements.txt
python -m ipykernel install --user --name=cas_gpu_venv --display-name="CAS GPU"