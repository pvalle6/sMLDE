import pandas as pd

database = pd.read_csv(R"C:\Users\valle\OneDrive\Documents\EP-DE\data\test\tests_encodings\msa_transformer_with_combo.csv", nrows = 10, header = None,)
test = (R"C:\Users\valle\OneDrive\Documents\EP-DE\data\test\tests_encodings\test_pandas.csv")
#print(database.columns)
print(database.head())
#database.to_csv(test)