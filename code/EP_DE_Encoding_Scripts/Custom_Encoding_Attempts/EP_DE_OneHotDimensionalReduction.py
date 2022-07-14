import numpy as np
from sklearn import datasets
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA


#prevents sciNot from being used as output
np.set_printoptions(suppress=True)
input_file = R"C:\Users\valle\OneDrive\Documents\EP-DE\data\test\numpys\oneHotEncode.npy"
#output_file = R"C:\Users\valle\OneDrive\Documents\EP-DE\data\ReducedOneHot149.txt"
output_file = R"C:\Users\valle\OneDrive\Documents\EP-DE\data\test\oneHotReduced.csv"
HighDimArray = np.load(input_file)

#output files of binary data 

#takes in a 3D array and returns a 2d Array flattened
# alongside the amino acid 20 dim
#function originally from https://github.com/fhalab/MLDE/blob/main/code/run_mlde/finalize_x.py
def TwoDeeReduction(x):
	# if len(x.shape) !=3:
	# 	raise ValueError("Input must be 3D Array")
	flat_length = np.prod(x.shape[1:])
	return np.reshape(x,[len(x),flat_length])

reducedArray = TwoDeeReduction(HighDimArray)
#print(reducedArray)
pca = PCA(n_components = 3)

printed_out_Hot = pca.fit_transform(reducedArray)
#pca.fit(reducedArray)
#print(pca.explained_variance_)

np.savetxt(output_file, printed_out_Hot, fmt = '%.18f', delimiter =',')
#np.savetxt(output_file, reducedArray, fmt = '%i', delimiter =',')
