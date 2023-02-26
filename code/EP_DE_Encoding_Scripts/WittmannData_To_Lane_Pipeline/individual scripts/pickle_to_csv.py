"""reads in the pickle file to a csv
to be used in add combo column"""
import pandas as pd
IMPORT = "B:\HardDrive_Files\Wittmann Data\MldeData\SimulationTrainingData\FilteredComboToInd.pkl" #pickle file to csv
EXPORT = "B:\HardDrive_Files\Wittmann Data\MldeData\SimulationTrainingData\FilteredComboToInd.txt" #encodings
df = pd.read_pickle(IMPORT)
for key, value in df.items():
    print(key)
pd.to_csv.
