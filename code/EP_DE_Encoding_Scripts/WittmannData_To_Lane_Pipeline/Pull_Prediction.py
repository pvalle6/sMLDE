"""Provides fitness scores"""
import pandas as pd 
#import csv 
# comboFile needs to have one column with each line being the list of comboinations in the desiresd order 
PULL = None
# put the msa_with combination file below 
PREDS = None
OUT = None
def pull_preds(selection, predictions, outputFile):
	"""Outputs a csv of selected fitness prediction scores from csv file with prediction scores"""
	comboListDF = pd.read_csv(selection, names = ['combo'])
	df = pd.read_csv(predictions, header = None)
	df = df.set_index([0])
	df = df.reindex(index=comboListDF['combo'])
	print(df.head())
	df.to_csv(output, header=False)
pull_preds(PULL, PREDS, OUT)


