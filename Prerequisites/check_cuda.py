import subprocess
import tensorflow as tf
import sys
print('Python Version:' , sys.version)

def check_cuda_support():
    print("=== CUDA Support Check ===")
    
    # Check nvcc
    try:
        result = subprocess.run(['nvcc', '--version'], capture_output=True, text=True)
        print(f"nvcc available: {'Yes' if result.returncode == 0 else 'No'}")
        if result.returncode == 0:
            print(f"nvcc version: {result.stdout.split('release')[-1].split(',')[0].strip()}")
    except:
        print("nvcc available: No")
    
    # Check PyTorch CUDA
    try:
        import torch
        print(f"PyTorch CUDA available: {torch.cuda.is_available()}")
        if torch.cuda.is_available():
            print(f"PyTorch CUDA version: {torch.version.cuda}")
            print(f"Number of GPUs: {torch.cuda.device_count()}")
    except ImportError:
        print("PyTorch not installed")
    

    print('=== TF Check ===')
    print('TF does not support GPU after version 2.10 on Windows')

    # Check TensorFlow CUDA
    try:
        import tensorflow as tf
        print(f"TensorFlow CUDA available: {tf.test.is_built_with_cuda()}")
        gpus = tf.config.list_physical_devices('GPU')
        print(f"TensorFlow GPU devices: {len(gpus)}")
    except ImportError:
        print("TensorFlow not installed")
        # Create a constant tensor
    
    hello = tf.constant('Hello, TensorFlow!')
    # Start a TensorFlow session
    print('TF Version: ', tf.__version__)

if __name__ == "__main__":
    check_cuda_support()