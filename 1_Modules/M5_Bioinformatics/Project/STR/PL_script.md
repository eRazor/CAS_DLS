ssh lucpas01@login-rhel8.hpc.zhaw.ch
cd $LSFM_CLUSTER_SCRATCH_USER_PATH
cd /net/home/lucpas01/
conda env create -f environment.yaml
conda activate Bioinfo4B-STR

tmux (for persistent Session to start the jupyter server)

jupyter notebook --notebook-dir=/cfs/earth/scratch/lucpas01/STR --no-browser --port=8888

ssh -L 8888:localhost:8888 lucpas01@login-rhel8.hpc.zhaw.ch

ssh -N -f -L 8891:localhost:8891 lucpas01@login-rhel8.hpc.zhaw.ch