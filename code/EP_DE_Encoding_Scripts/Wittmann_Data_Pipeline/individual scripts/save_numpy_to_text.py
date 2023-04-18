"""Script converts numpy file to txt file"""
import numpy as np
INPUT = None
#"Fitness.npy" #msa_transformer.npy"
OUTPUT = None

three_dim = np.load(INPUT)
output_numpy = np.ndarray.flatten(three_dim)
np.savetxt(OUTPUT, output_numpy, fmt='%f', delimiter=',')
