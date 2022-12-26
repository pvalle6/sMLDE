#import csv
import pandas as pd
MSALIBRARY = R"C:\Users\valle\OneDrive\Desktop\WitmannData\msa_transformer_with_combo.csv"
TRAININGCOMBO = R"C:\Users\valle\OneDrive\Documents\EP-DE\data\pull_pred_test\MSA_Stuff_Again\x4Mx_R2_Training_List.txt"
OUTPUT = R"C:\Users\valle\OneDrive\Documents\EP-DE\data\pull_pred_test\MSA_Stuff_Again\x4Mx_R3P_Sequence_Only.csv"
def remove_train_rehead(library, trainSeq, outputfile):
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
remove_train_rehead(MSALIBRARY, TRAININGCOMBO, OUTPUT)
