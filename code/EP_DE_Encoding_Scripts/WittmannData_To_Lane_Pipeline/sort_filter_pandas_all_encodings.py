import pandas as pd 
import csv 

# comboFile needs to have one column with each line being the list of comboinations in the desiresd order 
comboFile = R"C:\Users\valle\OneDrive\Documents\EP-DE\data\MSA_Encodings_List\Round 3 x6Mx List Randomly Selected 1098.txt"
# put the msa_with combination file below 
msa_test_library = R"C:\Users\valle\OneDrive\Desktop\WitmannData\msa_transformer_with_combo.csv"
georgiev_test_library = R"C:\Users\valle\OneDrive\Desktop\WitmannData\georgiev.csv"
one_hot_library= R"C:\Users\valle\OneDrive\Desktop\WitmannData\onehot.csv"
# csv file with the desired output encodings in the format needed for Lane's ML 
# output file 
# msa out put

#base path that will be added onto 
base_destination = R"C:\Users\valle\OneDrive\Documents\EP-DE\data\MSA_Encodings_List\x6Mx"


def filter_select_encodings(selection, library, Etype):
	comboListDF = pd.read_csv(selection, names = ['combo'])
	df = pd.read_csv(library, header = None)
	df = df.set_index([0])
	df = df.reindex(index=comboListDF['combo'])
	print(df.head())
	df.to_csv(base_destination+Etype+R'.csv',  header=False)

filter_select_encodings(comboFile,msa_test_library,R'_MSA')
#filter_select_encodings(comboFile,georgiev_test_library,R'_Georgiev')
#filter_select_encodings(comboFile,one_hot_library,R'_ONEHOT')

