# CAS Digital LifeScience
This project collects the top bioinformatics Python libraries and provides a simple evaluation harness.


### Environment Setup
#0 Install VS Code + Python Extensions
#1 Install Extensions: continue dev, Cline
#2 Install Ollama download and activate the Coding Assistent Model,  ollama pull deepseek-r1, ollama pull qwen2.5-coder:1.5b-base, ollama pull nomic-embed-text:latest
#3 Test autocompletion in a python file

#11 Install Git https://git-scm.com/downloads
#12 GitHub (Create Account) https://github.com/
 -  git config --global user.email "pascal.luc@hotmail.com"
 -  git config --global user.name "eRazor"
#13 Extension: Git Pull and Issue Extension 
#14 Test with clean Project (create readme, change, add and sync)

#15 Install Docker Desktop https://www.docker.com/
#16 Extension: Docker
#17 Test with create new Dev Container and Attach to it

#18 Install Python
#19 Install Miniconda and set System Paths
#20 Set python.condaPath to miniconda to activate

#21 Install CUDA (latest compatible version with Docker )
#22 Install Cuda Libraries and set path in miniconda
#23 Check Cuda installation with check_cuda.py

#24 Create Environment using Miniconda https://gist.github.com/bennyistanto/46d8cfaf88aaa881ec69a2b5ce60cb58
#25 Install dependencies (Pytorch, cuDNN, CudaToolkit, Tensorflow[no GPU])


## How to install Miniconda (Windows)

1. Go to the official Miniconda download page:  
   https://docs.conda.io/en/latest/miniconda.html
2. Download the latest Miniconda installer for Windows (64-bit, Python 3.x).
3. Run the installer and follow the prompts.  
   - Choose "Add Miniconda to my PATH environment variable" if you want conda available in all terminals.
   - Recommended: leave "Register Miniconda as the system Python" unchecked.
4. After installation, open a new Command Prompt or PowerShell and run:
   ```powershell
   conda --version
   ```
   to verify conda is installed.



Structure:
- `requirements.txt` - list of libraries (pip names where possible).
- `run_tests.py` - contains test functions (two per library) and an evaluation runner.

Notes:
- Some libraries (e.g., Bioconda, Galaxy) are not simple pip installs; see `requirements.txt` comments.
- Running `python run_tests.py` will attempt to import each library and run lightweight smoke tests; missing packages will mark tests as failed (0).

Skipped packages
----------------
Two packages from the original top-list — `pysam` and `deeptools` — are intentionally
excluded from the pip `requirements.txt` and from the test harness on Windows.

Reason: both packages depend on native libraries (htslib, deeptoolsintervals and other
extensions) that are not available as pip-installable wheels for Windows in this
environment. Attempts to build them with pip fail because they require platform
toolchains and prebuilt binaries. The recommended ways to use these packages are:

- Use WSL2 (Ubuntu) and install via conda-forge / bioconda:
	- Install Miniconda in WSL, then `conda create -n cas_bio -c conda-forge -c bioconda pysam deeptools`
- Or use Docker with a Linux base and conda-forge/bioconda installed inside the image.

If you want, I can help set up WSL2 or a Dockerfile and install `pysam` and `deeptools`
there so they can be used and tested with this project.

How to install packages (Windows PowerShell):
```powershell
python -m pip install -r requirements.txt
```

Conda GPU environment (Windows example)
-------------------------------------
If you need a CUDA-enabled PyTorch and better support for native packages, create a conda env and install PyTorch from the `pytorch` channel:

1) Install Miniconda (if needed).
2) conda create -n cas_gpu python=3.12
3) conda install -n cas_gpu -c pytorch -c nvidia pytorch pytorch-cuda=12.4
4) $DocumentsPath = [Environment]::GetFolderPath("MyDocuments")
5) conda run -n cas_gpu python -m pip install -r "$DocumentsPath\My Training\CAS\CAS_DLS\Prerequisites\requirements.txt"

Notes:
- On Windows some packages (pysam, deeptools) are best installed via bioconda on Linux/WSL or inside a Docker container.
- flash-attn requires matching CUDA and PyTorch versions; on Windows you may need to match your system CUDA or use WSL/Docker for prebuilt wheels.

## How to activate Python on Windows

1) Verify Python is available:
- CMD: python --version
- Or use the launcher: py --version

2) If Python is not found:
- Install from https://www.python.org/downloads/ (choose "Add Python to PATH" during install)
- Or install Miniconda (see Conda GPU environment section)

3) Create and activate a virtual environment (recommended)
- Create: python -m venv CAS_DLS
- Activate (Command Prompt): CAS_DLS\Scripts\activate
- Activate (PowerShell): CAS_DLS\Scripts\Activate.ps1
  - If PowerShell refuses to run, run as admin or:
    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
    then re-run the Activate.ps1 command.

4) Conda environments
- After installing Miniconda: conda create -n cas_gpu python=3.12
- Activate: conda activate cas_gpu

5) Confirm activation:
- python --version
- pip list

## How to add Python and Miniconda to PATH (Windows)

Important: modifying your PATH affects programs launched after the change. Prefer the installer's "Add to PATH" option when available, or use the commands below with care.

1) Installer options (recommended)
- Python.org installer: check "Add Python to PATH" during installation.
- Miniconda installer: the installer offers "Add Miniconda to PATH" (not recommended by maintainers) — instead prefer "Register Miniconda as default Python" or leave it off and use conda init (see below).

2) Temporary session (only affects current terminal)
- Command Prompt:
  - set PATH=%PATH%;C:\Full\Path\To\Python;C:\Full\Path\To\Python\Scripts
- PowerShell:
  - $env:PATH += ";C:\Full\Path\To\Python;C:\Full\Path\To\Python\Scripts"

3) Persistent user PATH (affects new terminals)
- PowerShell (recommended, safe user-level change):
  - Replace the path placeholders with your actual install locations:
    ```powershell
    $newPaths = ";C:\Users\<you>\Miniconda3;C:\Users\<you>\Miniconda3\Scripts;C:\Users\<you>\Miniconda3\Library\bin"
    [Environment]::SetEnvironmentVariable("PATH", $env:PATH + $newPaths, "User")
    ```
  - Close and re-open your terminal to pick up the change.

- CMD using setx (note: setx truncates very long PATH values):
  ```cmd
  setx PATH "%PATH%;C:\Users\<you>\Miniconda3;C:\Users\<you>\Miniconda3\Scripts;C:\Users\<you>\Miniconda3\Library\bin"
  ```
  - Then close and re-open your terminal.

4) Conda initialization (recommended for shells)
- After installing Miniconda, run:
  - cmd.exe / PowerShell: conda init
  - Then close and reopen the terminal. This configures your shell to locate conda and activates base behavior.

5) Verify
- After changing PATH or running conda init, open a new terminal and run:
  - python --version
  - conda --version

Notes:
- Replace C:\Users\<you>\Miniconda3 with your actual Miniconda installation path.
- Avoid duplicating PATH entries; prefer using conda init for shell integration rather than always adding Miniconda to PATH.

