"""Script used in previous testing for dimensional reduction"""
import numpy as np
INPUT= R"C:\Users\valle\Downloads\MldeData\SimulationTrainingData\Encodings\msa_transformer.npy"
OUTPUT = R"C:\Users\valle\OneDrive\Documents\EP-DE\data\test\tests_encodings\msa_transformer.csv"
def TwoDeeReduction(x):
	"""Function used in previous testing for dimensional reduction"""
	# if len(x.shape) !=3:
	# 	raise ValueError("Input must be 3D Array")
	flat_length = np.prod(x.shape[1:])
	return np.reshape(x,[len(x),flat_length])
	threeDeeNumpy = np.load(INPUT)
outputNumpy = TwoDeeReduction(threeDeeNumpy)
np.savetxt(OUTPUT, outputNumpy, fmt = '%f', delimiter =',')