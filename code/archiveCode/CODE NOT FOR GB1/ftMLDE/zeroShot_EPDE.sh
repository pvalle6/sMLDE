#!/bin/bash 
#SBATCH -N 1
#SBATCH -n 48
#SBATCH -t 48:00:00
#SBATCH -p single
#SBATCH -A hpc_mlde_gb2
#SBATCH -o zerShotOUT
#SBATCH -e zeroShotErrorMESSAGE

date
cd $PBS_O_WORKDIR
#
	#changes it to the MLDE directory 
	# run zeroShot on workdirectory 
python /home/pvalle6/ftMLDE/MLDE/predict_zero_shot.py --positions V39 D40 G41 V54 --models esm_msa1_t12_100M_UR50S --fasta /home/pvalle6/ftMLDE/MLDE/code/validation/basic_test_data/2GI9.fasta --alignment /home/pvalle6/ftMLDE/MLDE/code/validation/basic_test_data/GB1_Alignment.a2m  --include_conditional --mask_col --batch_size 32 



#(END_OF_FILE)