"""Script converts numpy file to txt file"""
import numpy as np
INPUT = R"C:\Users\valle\OneDrive\Desktop\WitmannData\Encodings\Fitness.npy" #msa_transformer.npy"
OUTPUT = R"C:\Users\valle\OneDrive\Desktop\WitmannData\Encodings\Fitness.csv"#msa_transformer.csv

three_dim = np.load(INPUT)
output_numpy = np.ndarray.flatten(three_dim)
np.savetxt(OUTPUT, output_numpy, fmt='%f', delimiter=',')
