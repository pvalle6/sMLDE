import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn import preprocessing

#file = R"C:\Users\valle\OneDrive\Documents\Class Documents\Research\pythonScripts\pca\pcaOneHot.txt.npy" #onehot
file = R"C:\Users\valle\OneDrive\Documents\Class Documents\Research\pythonScripts\pca\pcaOneHotAllPerm.txt.npy" #all perm
#file = R"C:\Users\valle\OneDrive\Documents\Class Documents\Research\pythonScripts\georgiev DE_EP\georgiev SAVE.txt.npy" #georgiev

#file2 = R"C:\Users\valle\OneDrive\Documents\Class Documents\Research\pythonScripts\oneHot DE_EP\oneHot_pca.txt"
#file3 = R"C:\Users\valle\OneDrive\Documents\Class Documents\Research\pythonScripts\oneHot DE_EP\oneHotPCACovar.txt"
dataIn = np.load(file)


norm = preprocessing.normalize(dataIn)
fitted =  PCA(n_components =2).fit(norm)
reduced = PCA(n_components =1).fit_transform(norm)


#print(fitted) # PCA(n_components=3)
#print(reduced) #[Matrix of Reduced Dimensions]

#attributes 

#print(fitted.components_) #largest possible variance length
print(fitted.explained_variance_) # [a,b,c] variances : largest eigenvalues of the covariance matrix of x 
print(fitted.explained_variance_ratio_) # percentage of variance by each component 
print(fitted.n_features_) # we have 80 features that need to be 3   
print(fitted.n_samples_) # we have 200 samples



#print(output)
#covar = np.cov(output)
#np.savetxt(file2, dim, fmt='%1.3f', delimiter=" ")
#np.savetxt(file2, covar, fmt='%1.3f', delimiter=",")




