import numpy as np
import os
import pathlib
from pathlib import Path
#file1 contains the n [200] sequences provided for the tests
#last 4 characters contains the 4 positions 
input_file = R"C:\Users\valle\OneDrive\Documents\EP-DE\data\149Thousand_ID_Variant.txt"
outputNumpy = R"C:\Users\valle\OneDrive\Documents\EP-DE\data\OneHot149ThousandEncodings.npy"


#all possible amino acids [0-19 index]
possible_amino_acid = ['A','R','N','D','C','Q','E','G','H','I','L','K',
                             			'M','F','P','S','T','W','Y','V']

#reads file into list and cuts white space
comboListGen = []
comboList = []
with open(input_file) as file:
	comboListGen = file.readlines()
	comboListGen = (x.rstrip() for x in comboListGen)
#takes only the last 4, which are the encoding from the file 
for x in comboListGen:
	x = x[-4:]
	comboList.append(x)

#based on a function found on https://github.com/fhalab/MLDE/blob/main/code/encode/encoding_generator.py
def generate_onehot():
	# Make a dictionary that links amino acid to index
	one_hot_dict = {aa: i for i, aa in enumerate(possible_amino_acid)}

	# Build an array of zeros from combolist length, 4 positions, 20 amino acids
	onehot_array = np.zeros([len(comboList), 4, 20])

	# Loop over all combos. This should all be vectorized at some point.
	for i, combo in enumerate(comboList):
	    
	    # Loop over the combo and add ones as appropriate
	    for j, character in enumerate(combo):# Add a 1 to the appropriate position
	        onehot_ind = one_hot_dict[character]
	        onehot_array[i, j, onehot_ind] = 1

	return onehot_array
#reduces 3d to 2d 


np.save(outputNumpy, generate_onehot())