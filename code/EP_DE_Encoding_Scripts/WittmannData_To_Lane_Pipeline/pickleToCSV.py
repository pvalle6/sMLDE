import pickle as pkl
import pandas as pd
import pandas as pd 

importfile = R"C:\Users\valle\Downloads\MldeData\SimulationTrainingData\FilteredComboToInd.pkl"
exportfile = R"C:\Users\valle\OneDrive\Documents\EP-DE\data\test\tests_encodings"

df2 = pd.read_pickle(importfile)
for key, value in df2.items():
    print(key)