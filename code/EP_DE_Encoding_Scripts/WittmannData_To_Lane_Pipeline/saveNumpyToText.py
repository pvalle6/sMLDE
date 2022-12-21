# CONVERTED NUMPY FILES TO CSV FILS
import numpy as np

input_file = R"C:\Users\valle\Downloads\MldeData\SimulationTrainingData\Encodings\msa_transformer.npy"
output_file = R"C:\Users\valle\OneDrive\Documents\EP-DE\data\test\tests_encodings\msa_transformer.csv"


def TwoDeeReduction(x):
	# if len(x.shape) !=3:
	# 	raise ValueError("Input must be 3D Array")
	flat_length = np.prod(x.shape[1:])
	return np.reshape(x,[len(x),flat_length])

threeDeeNumpy = np.load(input_file)

outputNumpy = TwoDeeReduction(threeDeeNumpy)
np.savetxt(output_file, outputNumpy, fmt = '%f', delimiter =',')