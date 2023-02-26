"""Script converts numpy file to txt file"""
import numpy as np
INPUT= R"B:\HardDrive_Files\Wittmann Data\MldeData\SimulationTrainingData\Fitness.npy" #msa_transformer.npy"
OUTPUT = R"B:\HardDrive_Files\Wittmann Data\MldeData\SimulationTrainingData\Fitness.txt" #msa_transformer.csv
three_dim = np.load(INPUT)
print(three_dim)
np.savetxt(OUTPUT, three_dim, fmt = '%f', delimiter =',')
