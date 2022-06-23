#!/bin/bash 
#SBATCH -N 1
#SBATCH -t 00:30:00
#SBATCH -p single
#SBATCH -A hpc_mlde_gb2
#SBATCH -o createMLDE2.sub
#SBATCH -e createMLDE2.sub

date
cd $PBS_O_WORKDIR
conda env create -f /home/pvalle6/ftMLDE/MLDE/mlde2.yml
#