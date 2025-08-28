@echo off
set "CUDA_HOME=C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4"
set "PATH=%CUDA_HOME%\bin;%PATH%"
set DISTUTILS_USE_SDK=1
call "%USERPROFILE%\Miniconda3\Scripts\activate.bat" cas_gpu
python -m pip uninstall -y ninja
python -m pip install flash-attn --no-build-isolation --verbose
python "H:\Documents\My Training\CAS DL\ml_import_probe.py"
pause

