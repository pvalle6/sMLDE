"""Script used in previous testing for dimensional reduction"""
import numpy as np
INPUT= None #msa_transformer.npy"
OUTPUT = None #msa_transformer.csv
def dim_reduction(x):
	"""Function used in previous testing for dimensional reduction"""
	flat_length = np.prod(x.shape[1:])
	return np.reshape(x,[len(x),flat_length])
three_dim = np.load(INPUT)
output_numpy = dim_reduction(three_dim)
np.savetxt(OUTPUT, output_numpy, fmt = '%f', delimiter =',')