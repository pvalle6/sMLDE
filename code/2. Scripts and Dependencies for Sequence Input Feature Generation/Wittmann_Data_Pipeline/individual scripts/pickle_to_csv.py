"""reads in the pickle file to a csv
to be used in add combo column"""
import pandas as pd
IMPORT = R"C:\Users\valle\OneDrive\Desktop\WitmannData\Encodings\FilteredComboToInd.pkl" #pickle file to csv
EXPORT = R"C:\Users\valle\OneDrive\Desktop\WitmannData\Encodings\FilteredComboToInd.csv" #encodings
dic = pd.read_pickle(IMPORT)
df = pd.DataFrame.from_dict(dic,orient='index')
#print(df)
df.to_csv(EXPORT)