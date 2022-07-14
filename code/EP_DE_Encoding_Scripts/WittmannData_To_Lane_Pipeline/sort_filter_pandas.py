import pandas as pd 
import csv 

# comboFile needs to have one column with each line being the list of comboinations in the desiresd order 
comboFile = R"C:\Users\valle\OneDrive\Documents\EP-DE\data\test\tests_encodings\five_combo_request.csv" #
test_library = R"C:\Users\valle\OneDrive\Documents\EP-DE\data\test\tests_encodings\test_pandas.csv"
# csv file with the desired output encodings in the format needed for Lane's ML 
selected_encodings_output =  R"C:\Users\valle\OneDrive\Documents\EP-DE\data\test\tests_encodings\5_combo_sorted.csv" 

comboListDF = pd.read_csv(comboFile, names = ['combo'])
# to avoid reading in the dataframe with the index from the csv, use pandas.drop [search it]

df = pd.read_csv(test_library, index_col=0)

df = df.set_index('0')
df = df.reindex(index=comboListDF['combo'])
print(df.head())
df.to_csv(selected_encodings_output,  header=False)