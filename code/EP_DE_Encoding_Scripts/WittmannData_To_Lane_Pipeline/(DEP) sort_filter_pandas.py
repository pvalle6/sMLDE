import pandas as pd 
import csv
comboFile = None
test_library = None
selected_encodings_output = None
comboListDF = pd.read_csv(comboFile, names = ['combo'])

df = pd.read_csv(test_library, header = None)

df = df.set_index([0])
df = df.reindex(index=comboListDF['combo'])
print(df.head())
df.to_csv(selected_encodings_output,  header=False)
