# SCRIPT USED TO ADD COMBO COLUMN TO CSV
import csv
import pandas as pd 
inputfile = R"C:\Users\valle\OneDrive\Desktop\WitmannData\msa_transformer.csv"
outputfile = R"C:\Users\valle\OneDrive\Desktop\WitmannData\msa_transformer_with_combo.csv"
comboFile = R"C:\Users\valle\OneDrive\Documents\EP-DE\data\test\tests_encodings\combosForWittman.csv"


# takes in the msa transformer csv given in the wittman caltech data, adds in the combo in the left column
#    allowing for sorting in the by sort_filter_pandas.py
comboLibrary = pd.read_csv(comboFile, names = ['combo'])
df = pd.read_csv(inputfile, header = None, index_col=0)
#
df_merge = pd.concat([comboLibrary.reset_index(drop=True), df.reset_index(drop=False)], axis=1)
print(df_merge.head())
df_merge.to_csv(outputfile, index=False,  header=False)