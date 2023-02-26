"""Script converts numpy file to txt file"""
import numpy as np
INPUT = R"B:\HardDrive_Files\Wittmann Data\MldeData\SimulationTrainingData\Encodings\msa_transformer.npy" #msa_transformer.npy"
OUTPUT = R"B:\HardDrive_Files\Wittmann Data\MldeData\SimulationTrainingData\Encodings\msa_transformer.txt"#msa_transformer.csv

three_dim = np.load(INPUT)
output_numpy = np.ndarray.flatten(three_dim)
np.savetxt(OUTPUT, output_numpy, fmt='%f', delimiter=',')
