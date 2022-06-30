import numpy as np
from sklearn import datasets
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

#numpy file to read into a array as a text to read 
input_file = R"C:\Users\valle\OneDrive\Desktop\4Position Transformer Encoding\GB1_T2Q_transformer_UnNormalized.npy"
#output_file = R"C:\Users\valle\OneDrive\Desktop\4Position Transformer Encoding\4Position Transformer Encoding\normal_tran_text.csv"
outputPCAfile = R"C:\Users\valle\OneDrive\Desktop\4Position Transformer Encoding\4Position Transformer Encoding\transformerPCA.csv"
transformerText = np.load(input_file)

def TwoDeeReduction(x):
	# if len(x.shape) !=3:
	# 	raise ValueError("Input must be 3D Array")
	flat_length = np.prod(x.shape[1:])
	return np.reshape(x,[len(x),flat_length])

flatArray = TwoDeeReduction(transformerText)

pca = PCA(n_components = 3)

pca.fit(flatArray)
print(pca.explained_variance_)

#pca.fit(flatArray)
print(pca.explained_variance_ratio_)
#reducedTransformers = pca.fit_transform(flatArray)
#print(reducedTransformers)

#np.savetxt(output_file, flatArray, fmt = '%.9f', delimiter =',')
#np.savetxt(outputPCAfile, reducedTransformers, fmt = '%.9f', delimiter =',')