import numpy as np
from sklearn import datasets
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA


#prevents sciNot from being used as output
np.set_printoptions(suppress=True)
input_file = R"C:\Users\valle\OneDrive\Documents\EP-DE\Data\200_Georgiev.npy"
output_file = R"C:\Users\valle\OneDrive\Documents\EP-DE\Data\AAindexReducedPCA.txt"
#set these to: your 3d array numpy encoding; your location for a binaryOutput in numpy (optional), and your location for a raw Text OneHot output
#input numpy unnormalized array with the onehot encodings
#HighDimensionalOneHotFile = R"C:\Users\valle\OneDrive\Documents\Class Documents\Research\pythonScripts\georgiev_Save.npy"
#HighDimensionalOneHotFile = R
#loads in the array from the 3d binary numpy
HighDimArray = np.load(input_file)
#HighDimArray = np.load(R"C:\Users\valle\OneDrive\Documents\Class Documents\Research\pythonScripts\reducedDim\reducedDimOneHot.npy")

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

printed_out_georgiev = pca.fit_transform(reducedArray)
pca.fit(reducedArray)
print(pca.explained_variance_)
print(printed_out_georgiev)
np.savetxt(output_file, printed_out_georgiev, fmt = '%.18f', delimiter =',')
