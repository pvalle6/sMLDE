"""Script that reads the first 10 lines of a
MSA Combination CSV and saves them to
be used as a test dataset """
import pandas as pd
MSA_COMBO = R"C:\Users\valle\OneDrive\Desktop\WitmannData\msa_transformer_with_combo.csv" #MSA Combination file
TEST = None
database = pd.read_csv(MSA_COMBO, nrows = 10, header = None)
print(database)
#database.to_csv(TEST, index = None, header=False)
