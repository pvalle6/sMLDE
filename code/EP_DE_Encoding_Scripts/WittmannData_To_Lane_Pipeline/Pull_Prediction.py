import pandas as pd 
import csv 

# comboFile needs to have one column with each line being the list of comboinations in the desiresd order 
pull = R"C:\Users\valle\OneDrive\Documents\EP-DE\data\Sequence Encodings for GB1\x1xx\x1xx Sequences.txt"
# put the msa_with combination file below 
preds = R"C:\Users\valle\OneDrive\Documents\EP-DE\data\pull_pred_test\Open_Github_Task_Files\Fitness Score - Peter Testing.xlsx"

outfile = R"C:\Users\valle\OneDrive\Documents\EP-DE\data\Sequence Encodings for GB1\x1xx\x1xx_preds.txt"

def pull_preds(selection, predictions):
	comboListDF = pd.read_csv(selection, names = ['combo'])
	df = pd.read_csv(predictions, header = None)
	df = df.set_index([0])
	df = df.reindex(index=comboListDF['combo'])
	print(df.head())
	df.to_csv(outfile, header=False)

pull_preds(pull, preds)


