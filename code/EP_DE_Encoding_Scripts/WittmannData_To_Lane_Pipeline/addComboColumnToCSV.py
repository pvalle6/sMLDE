import csv
import pandas as pd 
inputfile = R"C:\Users\valle\OneDrive\Documents\EP-DE\data\test\tests_encodings\msa_transformer.csv"
outputfile = R"C:\Users\valle\OneDrive\Documents\EP-DE\data\test\tests_encodings\msa_transformer_with_combo.csv"
comboFile = R"C:\Users\valle\OneDrive\Documents\EP-DE\data\test\tests_encodings\combosForWittman.csv"

comboLibrary = pd.read_csv(comboFile, names = ['combo'])

df = pd.read_csv(inputfile, header = None, index_col=0)
#
df_merge = pd.concat([comboLibrary.reset_index(drop=True), df.reset_index(drop=True)], axis=1)
df_merge.to_csv(outputfile, index=False,  header=False)