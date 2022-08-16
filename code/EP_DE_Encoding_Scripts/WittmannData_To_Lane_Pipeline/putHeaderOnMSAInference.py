import pandas as pd 
import csv 

inference = R"C:\Users\valle\OneDrive\Documents\EP-DE\data\inferenceRemoval\msa_database_without_training.csv"

columnNames= []
df = pd.read_csv(inference,nrows = 10, header = None)
for column,k in (enumerate(df)):
	columnNames.append(f"msa{k}")
columnNames[0] = 'id'
df.columns = columnNames
print(df.head())