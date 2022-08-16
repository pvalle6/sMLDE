import pandas as pd 
import csv 

msa_test_library = R"C:\Users\valle\OneDrive\Desktop\WitmannData\msa_transformer_with_combo.csv"
#msa_test_library1 = (R"C:\Users\valle\OneDrive\Documents\EP-DE\data\inferenceRemoval\test_db.csv")
training_combo = R"C:\Users\valle\OneDrive\Documents\EP-DE\data\inferenceRemoval\x6Mx.txt"
#training_combo1 = R"C:\Users\valle\OneDrive\Documents\EP-DE\data\inferenceRemoval\test_removal.txt"
output_ = R"C:\Users\valle\OneDrive\Documents\EP-DE\data\inferenceRemoval\msa_database_without_training.csv"

df = pd.read_csv(msa_test_library)

def cutOutTraining(library, trainSeq, outputfile):
	
	df = pd.read_csv(library, header = None)
	df = df.set_index([0])
	#df = df.reindex(index=comboListDF['combo'])

	with open(trainSeq) as file:
		for line in file:
			df.drop(line.strip(), inplace=True)
	#df.to_csv(base_destination+Etype+R'.csv',  header=False)
	print(df.head())
	df.to_csv(outputfile, header=False)
cutOutTraining(msa_test_library, training_combo, output_)	


