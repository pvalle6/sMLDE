"""reads in the pickle file to a csv
to be used in add combo column"""
import pandas as pd
IMPORT = None #pickle file to csv
EXPORT = None #encodings
dic = pd.read_pickle(IMPORT)
df = pd.DataFrame.from_dict(dic,orient='index')
#print(df)
df.to_csv(EXPORT)