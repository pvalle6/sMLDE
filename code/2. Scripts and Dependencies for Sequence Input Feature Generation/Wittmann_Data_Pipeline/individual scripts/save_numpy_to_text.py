"""Script converts numpy file to txt file"""
import numpy as np
INPUT = None #msa_transformer.npy"
OUTPUT = None #msa_transformer.csv

three_dim = np.load(INPUT)
output_numpy = np.ndarray.flatten(three_dim)
np.savetxt(OUTPUT, output_numpy, fmt='%f', delimiter=',')
