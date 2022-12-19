# PREPARES A SET OF DATA TO BE USED TO TEST THE ML MODEL BY REMOVING ANY TRAINING DATA FROM THE SET TO AVOID BIASING THE MODEL
import pandas as pd 
import csv 


msa_library = R"C:\Users\valle\OneDrive\Desktop\WitmannData\msa_transformer_with_combo.csv"
#msa_test_library1 = (R"C:\Users\valle\OneDrive\Documents\EP-DE\data\inferenceRemoval\test_db.csv")
training_combo = R"C:\Users\valle\OneDrive\Documents\EP-DE\data\pull_pred_test\MSA_Stuff_Again\x4Mx_R2_Training_List.txt"
#training_combo1 = R"C:\Users\valle\OneDrive\Documents\EP-DE\data\inferenceRemoval\test_removal.txt"
#output_ = R"C:\Users\valle\OneDrive\Documents\EP-DE\data\inferenceRemoval\msa_database_without_training_with_proper_heading.csv"
output_ = R"C:\Users\valle\OneDrive\Documents\EP-DE\data\pull_pred_test\MSA_Stuff_Again\x4Mx_R3P_Sequence_Only.csv"

def removeTrainAndAddHead(library, trainSeq, outputfile):
	df = pd.read_csv(library, header = None)
	df = df.set_index([0])	
	with open(trainSeq) as file:
		for line in file:
			df.drop(line.strip(), inplace=True)
	df = df.reset_index()
	columnNames= []
	#need to change to iterrows for more efficient run
	for column,k in (enumerate(df)):
		columnNames.append(f"msa{k}")
	columnNames[0] = 'id'
	df.columns = columnNames
	print(df.head())
	df.to_csv(outputfile, index = False)

removeTrainAndAddHead(msa_library, training_combo, output_)
