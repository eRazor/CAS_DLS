@echo off
REM Prepare MSVC and conda env, then build flash-attn
REM Prevent setuptools from re-activating the VC environment
set "DISTUTILS_USE_SDK=1"
call "C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\Build\vcvarsall.bat" x64
call "%USERPROFILE%\Miniconda3\Scripts\activate.bat" cas_gpu
set "CUDA_HOME=C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4"
set "PATH=%CUDA_HOME%\bin;%PATH%"
cd /d C:\flash-attn
python setup.py install
REM Test the installation
