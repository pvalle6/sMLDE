"""reads in the pickle file to a csv
to be used in add combo column"""
import pandas as pd
IMPORT = None #pickle file to csv
EXPORT = None #encodings
df2 = pd.read_pickle(IMPORT)
for key, value in df2.items():
    print(key)
