@echo off
python -m venv cas_gpu_venv
call cas_gpu_venv\Scripts\activate.bat
pip install nvidia-cudnn-cu13
pip install nvidia-cuda-runtime
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu130

pip install -r prerequisites\requirements.txt
python -m ipykernel install --user --name=cas_gpu_venv --display-name="CAS GPU"


sudo nvidia-ctk runtime configure --runtime=docker
sudo  apt install cuda-drivers
 hostnamectl
  export NVIDIA_CONTAINER_TOOLKIT_VERSION=1.18.2-1
  sudo apt-get install -y \
      nvidia-container-toolkit=${NVIDIA_CONTAINER_TOOLKIT_VERSION} \
      nvidia-container-toolkit-base=${NVIDIA_CONTAINER_TOOLKIT_VERSION} \
      libnvidia-container-tools=${NVIDIA_CONTAINER_TOOLKIT_VERSION} \
      libnvidia-container1=${NVIDIA_CONTAINER_TOOLKIT_VERSION}

sudo nvidia-ctk runtime configure --runtime=docker

sudo docker run -it --gpus all -d --name CUDA_NN nvidia/cuda:12.8.1-cudnn-runtime-rockylinux8 tail -f
docker run -it  --rm --gpus all nvidia/cuda:12.8.1-cudnn-runtime-rockylinux8 nvidia-smi
docker exec -it CUDA_NN bash
dnf groupinstall "Development Tools"
dnf install python3.12 python3.12-pip python3.12-devel -y
python3.12 -m pip install tensorflow[and-cuda]
 python3 -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"