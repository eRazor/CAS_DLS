# 🌍 AI Portfolio — Welcome

Welcome to my Artificial Intelligence portfolio! 👋

This repository is a curated collection of my work, experiments, and learning journey across multiple areas of Artificial Intelligence, Data Science, and Computational Research. My goal is to explore intelligent systems, build practical solutions, and continuously learn by doing.

Whether you're a recruiter, researcher, developer, or fellow AI enthusiast — you're warmly invited to explore, learn, and collaborate.

---

# ✨ About This Portfolio

This portfolio showcases projects across **8 AI Computational and Life Science domains** and 3 different Schools:

- 🐍 [Python Programming](#-python-programming) <picture>
  <img src="/3_Media/ZHAW-logo.png" alt="ZHAW" width="20" />
</picture>

- 📊 [Data Analysis](#-Data-Analysis)<picture>
  <img src="/3_Media/ZHAW-logo.png" alt="ZHAW" width="20" />
</picture>

- 🤖 [Machine Learning](#-Machine-Learning)<picture>
  <img src="/3_Media/ZHAW-logo.png" alt="ZHAW" width="20" />
</picture>

- 🧠 [Neural Networks](#-neural-networks)<picture>
  <img src="/3_Media/ZHAW-logo.png" alt="ZHAW" width="20" />
</picture>

- 🧬 [Bioinformatics](#-Bioinformatics)<picture>
  <img src="/3_Media/ZHAW-logo.png" alt="ZHAW" width="20" />
</picture>

- 🔬 [Simulations](#-Simulations)<picture>
  <img src="/3_Media/ZHAW-logo.png" alt="ZHAW" width="20" />
</picture>

- 🎮 [Reinforcement Learning](#-Reinforcement-Learning)<picture>
  <img src="/3_Media/Coursera.png" alt="Coursera" width="20" />
</picture>(coming soon)

- 💬 [Natural Language Processing with Transformers](#-Natural-Language-Processing-with-Transformers)<picture>
  <img src="/3_Media/digicomp_logo.jpg" alt="Digicomp" width="20" />
</picture>(coming soon)


Each module contains hands‑on projects, experiments, and well‑documented implementations.

---


# 📚 Modules Overview

## 🐍 Python Programming

This module demonstrates strong Python fundamentals and practical programming skills used throughout AI and data science.

**Highlights:**

✔️  Clean and modular Python design<br>
✔️  Procecural programming<br>
✔️  File Input/Output<br>
✔️  Automation scripts<br>
✔️  Utility tools for AI workflows<br>
✔️  Develop a library with automation utilities for data processing pipelines which can be used for continious AI model training<br>


**Technologies:**

- Pandas
- FuncTools
- Matplotlib
- shutil
- io
- Jupyter Notebooks

<picture>
  <img src="/3_Media/python.gif" alt="python" width="400"/>
</picture>

---

## 📊 Data Analysis

This module focuses on extracting insights from structured and unstructured datasets.

**Highlights:**

✔️	Programming of a data pipeline in Python, including a custom-developed XML parser<br>
✔️	Exploratory data analysis (EDA) to identify key characteristics and data cleaning using Pandas<br>
✔️	Application of signal processing methods using NumPy and Scikit-learn<br>
✔️	Temporal interpolation of training breaks and exercise transitions (in cases of incomplete data)<br>
✔️	Use of Fast Fourier Transform (FFT), Savitzky–Golay smoothing, and peak/valley detection with additional libraries<br>
✔️	Creation of automated interactive visualizations with Seaborn, including annotations for interpreting training data<br>
✔️	Transformation of raw sensor data from Smart Watch into structured datasets and interpretable analytical insights.<br>


**Technologies:**

- SciPy (Signal)
- NumPy
- Seaborn
- xml.etree
- plotly
<picture>
  <img src="/3_Media/Screenshot Inputs.png" alt="input" width="300"/>
</picture>
<picture>
  <img src="/3_Media/Hand Notes.png" alt="input" width="300"/>
</picture>
<picture>
  <img src="/3_Media/data_analysis.gif" alt="data analysis" width="400"/>
</picture>


---

## 🤖 Machine Learning

This module explores classical machine learning algorithms and applied predictive modeling.
In collaboration with P. Vagenknecht.

**Highlights:**

✔️	Implementation and comparison of multiple algorithms: Random Forest, Decision Tree, SVM<br>
✔️	Model evaluation and selection of the best-performing classifier<br>
✔️	Analysis of the impact of Principal Component Analysis (PCA) on model performance<br>
✔️  Successful automatic recognition of training exercises based solely on wearable sensor data. Accuracy: 96% (Kappa score)<br>
✔️  Development of a multiclass machine learning model to classify 26 different fitness exercises based on smartwatch sensor data.<br>


**Technologies:**

- Scikit‑Learn (PreProc, Ensemble, Decomp, Model_Selection, Metrics)
- autofeat
- itertools

<picture>
  <img src="/3_Media/ML Exercise Classification using Smart Watch Data.gif" alt="ML" width="400"/>
</picture>

---

## 🧠 Neural Networks

Extension of the ML project using computer vision and deep learning to classify fitness exercises based on video data.
In collaboration with F. Hächler.

**Highlights:**

✔️	Extraction of skeletal motion data from videos (Source: Pexels.com) using OpenPose (Credits: https://github.com/cmu-perceptual-computing-lab/openpose) <br>
✔️	Recombination of individual frames into training datasets<br>
✔️	Implementation of an LSTM network to analyze temporal motion sequences<br>
✔️	Model optimization using TensorFlow/Keras hyperparameter tuning<br>
✔️ The model successfully generalized motion patterns within a single epoch. Final model accuracy: 98% (within 1 epoch, without overfitting)<br>


**Technologies:**

- OpenPose
- PyTorch (ML Extension and comparison)
- Multithreading
- TensorFlow / Keras

<picture>
  <img src="/3_Media/ezgif-75fbdcb3bbee8217.gif" alt="Bicep Curl 1" width="300"/>
</picture>
<picture>
  <img src="/3_Media/ezgif-7634e0b37bfa5e7f.gif" alt="Bicep Curl 2" width="300"/>
</picture>
<picture>
  <img src="/3_Media/ezgif-7ddb69cf6b82f9b4.gif" alt="Bicep Curl 3" width="300"/>
</picture>
<br>
<picture>
  <img src="/3_Media/NN.gif" alt="Neural Network" width="400"/>
</picture>

---

## 🧬 Bioinformatics

This module explores computational biology and biological data analysis.

**Highlights:**

✔️  Sequence alignment<br>
✔️  Gene pattern discovery (Short Tandem Repeats)<br>
✔️  Variant Consequence analysis<br>
✔️  Protein structure exploration with IGV & VEP<br>
✔️  Proof of possible malignant mutation is found in our sample<br>
✔️  Biological data visualization<br>

**Technologies:**
- Remote SSH
- HPC RockyLinux8
- biopython
- Bio (SeqIO)
- cyvcf2
- bwa-mem2
- samtools
- cnvkit
- GangSTR (WebSTR)

<picture>
  <img src="/3_Media/str_analysis.gif" alt="DNA Sequencing" width="400"/>
</picture>

---

## 🔬 Simulations

This module contains computational process simulations and modeling experiments.

**Highlights:**

✔️  Industrial production line simulation and optimization<br>
✔️  KPI Definitions<br>
✔️  Experiments with 5 different parameters<br>
✔️  BPMN Modelling (Phase 3 - Clinical Trial)<br>

**Simulation Software:**
- Simio

<picture>
  <img src="/3_Media/Phase3_Clinical_Trial_Pascal_Luc.gif" alt="Clinical Trial" width="400"/>
</picture>

---

## 🎮 Reinforcement Learning
(coming soon)

This module explores intelligent agents that learn through interaction.

**Highlights:**

✔️  Q‑Learning<br>
✔️  Optimization agents<br>
✔️  Autonomous decision making<br>
✔️  Policy Gradient methods<br>
✔️  Environment simulations<br>


---

## 💬 Natural Language Processing with Transformers
(coming soon)

This module focuses on modern NLP using transformer architectures.


----------------

# ⚙️ Environment Setup
Follow these steps to set up to download and setup the environment.
-  The neural network module requires a CUDA environment, if you want to explore this module aswell and don't have a cuda python envrinonment yet, 
please follow Section 2 to set it up.
-  If you want to use a Docker environment follow Section 3.

### 1. Clone Repository

```bash
git clone https://github.com/eRazor/CAS_DLS.git
cd CAS_DLS
```
### 2. Create Virtual Environment

Using venv

```bash
python -m venv venv
```

#### Activate Environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / Mac**

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r 0_Prerequisites/requirements.txt
```

### 4. Launch Jupyter (Optional)

```bash
jupyter notebook
```
----------------

### 2. CUDA Environment

All reusable scripts (batch / shell) required for the setup are located in CAS_DLS/0_Prerequisites.

#0 Install VS Code + Python Extensions

#1 Install Extensions: continue dev, Cline

#2 Install Ollama download and activate the Coding Assistent Model,  ollama pull deepseek-r1, ollama pull qwen2.5-coder:1.5b-base, ollama pull nomic-embed-text:latest

#3 Test autocompletion in a python file

#4 Install Git https://git-scm.com/downloads

#5 GitHub (Create Account) https://github.com/

#4 Install Git https://git-scm.com/downloads

#5 GitHub (Create Account) https://github.com/

 -  git config --global user.email "pascal.luc@hotmail.com"
   
 -  git config --global user.name "eRazor"
   
#6 Extension: Git Pull and Issue Extension 

#7 Test with clean Project (create readme, change, add and sync)

#6 Extension: Git Pull and Issue Extension 

#7 Test with clean Project (create readme, change, add and sync)

#8 Install Docker Desktop https://www.docker.com/

#9 Extension: Docker

#10 Test with create new Dev Container and Attach to it

#11 Install Python

#12 Install Miniconda and set System Paths

#13 Set python.condaPath to miniconda to activate

#14 Install CUDA (latest compatible version with Docker )

#15 Install Cuda Libraries and set path in miniconda

#16 Check Cuda installation with check_cuda.py

#17 Create Environment using Miniconda https://gist.github.com/bennyistanto/46d8cfaf88aaa881ec69a2b5ce60cb58

#18 Install dependencies (Pytorch, cuDNN, CudaToolkit, Tensorflow[no GPU])


### Sequence is important:

pip install nvidia-cudnn-cu13

pip install nvidia-cuda-runtime

pip install torch torchvision --index-url https://download.pytorch.org/whl/cu130

Restart Env after install

Install requirements after


### How to install Miniconda (Windows)

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

### Skipped packages

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

### Conda GPU environment (Windows example)

If you need a CUDA-enabled PyTorch and better support for native packages, create a conda env and install PyTorch from the `pytorch` channel:

1) Install Miniconda (if needed).<br>
2) conda create -n cas_gpu python=3.12<br>
3) conda install -n cas_gpu -c pytorch -c nvidia pytorch pytorch-cuda=12.4<br>

4) $DocumentsPath = [Environment]::GetFolderPath("MyDocuments")<br>
5) conda run -n cas_gpu python -m pip install -r "$DocumentsPath\My Training\CAS\CAS_DLS\Prerequisites\requirements.txt"<br>

Notes:
- On Windows some packages (pysam, deeptools) are best installed via bioconda on Linux/WSL or inside a Docker container.
- flash-attn requires matching CUDA and PyTorch versions; on Windows you may need to match your system CUDA or use WSL/Docker for prebuilt wheels.

### How to activate Python on Windows

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

### How to add Python and Miniconda to PATH (Windows)

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

----------------

## 3. Docker Environment

Docker environment requires advanced knowledge of the individual image and the system you are working on.
Here we are using RockyLinux8 with CUDA support.
https://www.youtube.com/watch?v=RJlhCqRZHv4


sudo nvidia-ctk runtime configure --runtime=docker<br>
sudo  apt install cuda-drivers<br>
 hostnamectl<br>
  export NVIDIA_CONTAINER_TOOLKIT_VERSION=1.18.2-1<br>
  sudo apt-get install -y \<br>
      nvidia-container-toolkit=${NVIDIA_CONTAINER_TOOLKIT_VERSION} \<br>
      nvidia-container-toolkit-base=${NVIDIA_CONTAINER_TOOLKIT_VERSION} \<br>
      libnvidia-container-tools=${NVIDIA_CONTAINER_TOOLKIT_VERSION} \<br>
      libnvidia-container1=${NVIDIA_CONTAINER_TOOLKIT_VERSION}<br>

sudo nvidia-ctk runtime configure --runtime=docker<br>

sudo docker run -it --gpus all -d --name CUDA_NN nvidia/cuda:12.8.1-cudnn-runtime-rockylinux8 tail -f<br>
docker run -it  --rm --gpus all nvidia/cuda:12.8.1-cudnn-runtime-rockylinux8 nvidia-smi<br>
docker exec -it CUDA_NN bash<br>
dnf groupinstall "Development Tools"<br>
dnf install python3.12 python3.12-pip python3.12-devel -y<br>
python3.12 -m pip install tensorflow[and-cuda]<br>
 python3 -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"<br>
 

### WSL Alternative
Alternatively you may setup WSL instead. 
https://www.youtube.com/watch?v=MwxZ2hswZ6A


----------------
### 🚀 Goals of This Portfolio

- Build real‑world AI projects
- Explore multiple AI domains
- Share knowledge with the community
- Continuously improve and experiment

---

### 🤝 Contributions & Collaboration

This work is my own achievement. Those sections where I have used external sources are appropriately indicated.

Ideas, suggestions, and collaborations are welcome!

Feel free to:

- Open an issue
- Submit a pull request
- Share feedback

---

# ⭐ If You Find This Helpful

If you find this portfolio interesting or useful, consider giving it a star ⭐

to help others discover the repository and supports my AI learning journey 

or contact me via <a href="https://www.linkedin.com/in/pascal-luc">Linkedin</a>

---

# 🌟 Thank You for Visiting

Thanks for taking the time to explore my AI portfolio.

Let's build a better future together 🚀

---
