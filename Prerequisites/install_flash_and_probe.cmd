@echo off
set "CUDA_HOME=C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4"
set "PATH=%CUDA_HOME%\bin;%PATH%"
set DISTUTILS_USE_SDK=1

python -m pip uninstall -y ninja

python "H:\Documents\My Training\CAS DL\ml_import_probe.py"
pause