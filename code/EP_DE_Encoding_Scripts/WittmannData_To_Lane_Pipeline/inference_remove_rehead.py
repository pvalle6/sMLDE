import pandas as pd 
import csv 

msa_library = R"C:\Users\valle\OneDrive\Desktop\WitmannData\msa_transformer_with_combo.csv"
#msa_test_library1 = (R"C:\Users\valle\OneDrive\Documents\EP-DE\data\inferenceRemoval\test_db.csv")
training_combo = R"C:\Users\valle\OneDrive\Documents\EP-DE\data\inferenceRemoval\x4xx\x4xx Sequences.txt"
#training_combo1 = R"C:\Users\valle\OneDrive\Documents\EP-DE\data\inferenceRemoval\test_removal.txt"
#output_ = R"C:\Users\valle\OneDrive\Documents\EP-DE\data\inferenceRemoval\msa_database_without_training_with_proper_heading.csv"
output_ = R"C:\Users\valle\OneDrive\Documents\EP-DE\data\inferenceRemoval\x4xx\x4xx_head_minus_96.csv"

def removeTrainAndAddHead(library, trainSeq, outputfile):
	df = pd.read_csv(library, header = None)
	df = df.set_index([0])	
	with open(trainSeq) as file:
		for line in file:
			df.drop(line.strip(), inplace=True)
	df = df.reset_index()
	columnNames= []
	for column,k in (enumerate(df)):
		columnNames.append(f"msa{k}")
	columnNames[0] = 'id'
	df.columns = columnNames
	print(df.head())
	df.to_csv(outputfile, index = False)

removeTrainAndAddHead(msa_library, training_combo, output_)
