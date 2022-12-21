# SCRIPT USED ON HPC DUE TO LARGE RESOURCES REQUIRED, NEEDS TO BE OPTIMIZED
# RAN USING inference_run.sub ON HPC

import pandas as pd 
import csv 


msa_library = "/ddnA/project/jjung1/pvalle6/msa_transformer_with_combo.csv"
#msa_test_library1 = (R"C:\Users\valle\OneDrive\Documents\EP-DE\data\inferenceRemoval\test_db.csv")
training_combo_1 = "/ddnA/project/jjung1/pvalle6/inference_list/x4Mx_R2_Training_List.txt"
training_combo_2 = "/ddnA/project/jjung1/pvalle6/inference_list/x6Mx_R2_Training_List.txt"
#training_combo1 = R"C:\Users\valle\OneDrive\Documents\EP-DE\data\inferenceRemoval\test_removal.txt"
#output_ = R"C:\Users\valle\OneDrive\Documents\EP-DE\data\inferenceRemoval\msa_database_without_training_with_proper_heading.csv"
output_1 = "/ddnA/project/jjung1/pvalle6/inference_list/x4Mx_R2_out.txt"
output_2 = "/ddnA/project/jjung1/pvalle6/inference_list/x6Mx_R2_out.txt"

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

removeTrainAndAddHead(msa_library, training_combo_1, output_1)
removeTrainAndAddHead(msa_library, training_combo_2, output_2)
