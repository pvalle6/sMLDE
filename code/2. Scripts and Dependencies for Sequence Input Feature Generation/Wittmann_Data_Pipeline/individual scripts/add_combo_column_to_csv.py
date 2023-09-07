"""Script that reads in the Encodings from
the Wittman Dataset and adds the pickle file
with the Combinations"""

import pandas as pd

INPUTFILE = None #add big wittman transformer
OUTPUTFILE = None #new location
COMBOFILE = None # combinations from the pickle file

""" takes in the msa transformer csv given in the wittman caltech data,
	adds in the combo in the left column
	allowing for sorting in the by sort_filter_pandas """
	
comboLibrary = pd.read_csv(COMBOFILE, names = ['combo'])
df = pd.read_csv(INPUTFILE, header = None, index_col=0)
df_merge = pd.concat([comboLibrary.reset_index(drop=True), df.reset_index(drop=False)], axis=1)
print(df_merge.head())
df_merge.to_csv(OUTPUTFILE, index=False,  header=False)
