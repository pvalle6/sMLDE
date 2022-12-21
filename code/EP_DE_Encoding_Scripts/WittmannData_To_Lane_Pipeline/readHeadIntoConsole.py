# WORK IN PROGRESS SCRIPT THAT USED TO BE USED TO ENSURE PANDAS DF WAS PROPERLY FORMATTED
import pandas as pd

database = pd.read_csv(R"C:\Users\valle\OneDrive\Desktop\WitmannData\msa_transformer_with_combo.csv", nrows = 10, header = None)
#database1 = pd.read_csv(R"C:\Users\valle\OneDrive\Desktop\WitmannData\msa_transformer.csv", nrows = 10, header = None,)
test = (R"C:\Users\valle\OneDrive\Documents\EP-DE\data\inferenceRemoval\test_db.csv")
#print(database.columns)
print(database.head())

database.to_csv(test, index = None, header=False)