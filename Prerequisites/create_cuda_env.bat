@echo off
REM Check for python or py launcher
where python >nul 2>nul
if %errorlevel%==0 (
    set "PY_CMD=python"
) else (
    where py >nul 2>nul
    if %errorlevel%==0 (
        set "PY_CMD=py"
    ) else (
        echo Python is not installed or not in your PATH.
        echo Install from https://www.python.org/downloads/ or install Miniconda.
        echo After installation, re-open this terminal and re-run this script.
        exit /b 1
    )
)


set "CUDA_HOME=C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4"
set "PATH=%CUDA_HOME%\bin;%PATH%"
set DISTUTILS_USE_SDK=1

REM Create a virtual environment named 'CAS_DLS'
%PY_CMD% -m venv CAS_DLS



call "%USERPROFILE%\Miniconda3\Scripts\activate.bat" CAS_DLS

REM Activate the environment (Command Prompt)
call CAS_DLS\Scripts\activate

REM Upgrade pip
%PY_CMD% -m pip install --upgrade pip

REM Install PyTorch with CUDA 12.x support (update index-url if needed)
REM Note: change the index URL to the correct CUDA toolchain if/when available
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121

REM Install TensorFlow (CPU/GPU wheel selection is automatic if compatible)
pip install tensorflow

REM Install Flash-Attention
pip install flash-attn --no-build-isolation --verbose

REM NOTE: If you prefer conda-managed CUDA (recommended for GPU toolkits),
REM install Miniconda and create a conda env, then use:
REM   conda create -n cas_gpu python=3.12
REM   conda activate cas_gpu
REM   conda install -c pytorch -c nvidia pytorch pytorch-cuda=12.4
REM and then pip install -r requirements.txt inside that conda env.

echo.
echo Virtual environment 'CAS_DLS' created and activated.
echo To activate later (Command Prompt): call CAS_DLS\Scripts\activate
echo To activate later (PowerShell): CAS_DLS\Scripts\Activate.ps1
echo To deactivate: deactivate
