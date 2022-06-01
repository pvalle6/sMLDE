import numpy as np 

#prevents sciNot from being used as output
np.set_printoptions(suppress=True)

#set these to: your 3d array numpy encoding; your location for a binaryOutput in numpy (optional), and your location for a raw Text OneHot output
#input numpy unnormalized
file1 = R"C:\Users\valle\OneDrive\Documents\Class Documents\Research\pythonScripts\GB1_WT_MQ_T2Q_onehot_UnNormalized.npy"
#output files 
file2 = R"C:\Users\valle\OneDrive\Documents\Class Documents\Research\pythonScripts\arrayTests\numpyTwoDim_BinaryOutput.npy"
file3 = R"C:\Users\valle\OneDrive\Documents\Class Documents\Research\pythonScripts\arrayTests\numpyTwoDim_RawText.txt"
#loads in the array from the 3d binary numpy
threeDeeArray = np.load(file1)
#takes in a 3D array and returns a 2d Array flattened
# alongside the amino acid 20 dim

#function originally from https://github.com/fhalab/MLDE/blob/main/code/run_mlde/finalize_x.py
def TwoDeeReduction(x):
	# if len(x.shape) !=3:
	# 	raise ValueError("Input must be 3D Array")
	flat_length = np.prod(x.shape[1:])
	return np.reshape(x,[len(x),flat_length])

#reduces the 3d array to 2d array
twoDeeArray = TwoDeeReduction(threeDeeArray)
#saves first as binary and second as output
np.save(file2, twoDeeArray)	
np.savetxt(file3, twoDeeArray.astype(int), fmt='%i', delimiter=" ")




