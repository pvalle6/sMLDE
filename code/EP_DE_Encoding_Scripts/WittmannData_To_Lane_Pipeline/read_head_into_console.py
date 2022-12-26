"""Script that reads the first 10 lines of a MSA Combination CSV and saves them to be used as a test dataset """
import pandas as pd
MSA_COMBO = None #MSA Combination file
TEST = None
database = pd.read_csv(MSA_Combo, nrows = 10, header = None)

database.to_csv(TEST, index = None, header=False)