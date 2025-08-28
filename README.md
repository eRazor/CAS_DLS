# CAS Digital LifeScience

This project collects the top bioinformatics Python libraries and provides a simple evaluation harness.

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
4) conda run -n cas_gpu python -m pip install -r requirements.txt

Notes:
- On Windows some packages (pysam, deeptools) are best installed via bioconda on Linux/WSL or inside a Docker container.
- flash-attn requires matching CUDA and PyTorch versions; on Windows you may need to match your system CUDA or use WSL/Docker for prebuilt wheels.

