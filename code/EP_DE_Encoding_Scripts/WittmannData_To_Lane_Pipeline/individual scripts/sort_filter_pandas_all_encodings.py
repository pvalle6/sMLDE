"""Finds the encodings for chosen sequences"""
import pandas as pd

COMBO = None
MSA = None # put the msa_with combination file below
# GEORGIEV = None
# ONEHOT= None


#base path that will be added onto
BASE_DESTINATION = None

def filter_select_encodings(selection, library, e_type):
    """pulls encodings from wittmann data"""
    combo_list_dataframe = pd.read_csv(selection, names = ['combo'])
    dataframe = pd.read_csv(library, header = None)
    dataframe = dataframe.set_index([0])
    dataframe = dataframe.reindex(index=combo_list_dataframe['combo'])
    print(dataframe.head())
    dataframe.to_csv(BASE_DESTINATION+e_type+R'.csv',  header=False)

filter_select_encodings(COMBO,MSA,R'_MSA')
# filter_select_encodings(COMBO,GEORGIEV,R'_Georgiev')
# #filter_select_encodings(COMBO,ONEHOT,R'_ONEHOT')
