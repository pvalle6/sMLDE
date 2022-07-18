import pandas as pd 
import csv 

# comboFile needs to have one column with each line being the list of comboinations in the desiresd order 
comboFile = R"C:\Users\valle\OneDrive\Documents\EP-DE\data\updated_Encoding_Data\7_15_2022_Sequence_Combo.csv"
# put the msa_with combination file below 
#msa library
#test_library = R"C:\Users\valle\OneDrive\Desktop\WitmannData\msa_transformer_with_combo.csv"
#georgiev library
#test_library = R"C:\Users\valle\OneDrive\Desktop\WitmannData\georgiev.csv"
#onehot library 
test_library = R"C:\Users\valle\OneDrive\Desktop\WitmannData\onehot.csv"
# csv file with the desired output encodings in the format needed for Lane's ML 
# output file 
# msa out put
#selected_encodings_output = R"C:\Users\valle\OneDrive\Documents\EP-DE\data\updated_Encoding_Data\7_15_22_MSAENC.csv"
# georgiev output 
#selected_encodings_output = R"C:\Users\valle\OneDrive\Documents\EP-DE\data\updated_Encoding_Data\7_15_22_georg_ENC.csv"
# one hot out put 
selected_encodings_output = R"C:\Users\valle\OneDrive\Documents\EP-DE\data\updated_Encoding_Data\7_15_22_oneHOT_ENC.csv"
comboListDF = pd.read_csv(comboFile, names = ['combo'])
# to avoid reading in the dataframe with the index from the csv, use pandas.drop [search it]

df = pd.read_csv(test_library, header = None)

df = df.set_index([0])
df = df.reindex(index=comboListDF['combo'])
print(df.head())
df.to_csv(selected_encodings_output,  header=False)