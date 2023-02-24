"""Library for use in sMLDE"""
import pandas as pd

def pickle_to_csv(import):
    """reads in the pickle file to a csv
    to be used in add combo column
    IMPORT: pickle file to csv

    Returns to console
    """
    df2 = pd.read_pickle(IMPORT)
    for key, value in df2.items():
        print(key)

def filter_select_encodings(selection, library, e_type):
    """pulls encodings from Wittmann data
    Selection: list of encodings
    library: selected encoding library
    Returns Pandas Dataframe
    """
    combo_list_dataframe = pd.read_csv(selection, names = ['combo'])
    df = pd.read_csv(library, header = None)
    df = df.set_index([0])
    df = df.reindex(index=combo_list_dataframe['combo'])
    print(df.head())
    return df
# filter_select_encodings(COMBO,GEORGIEV,R'_Georgiev')
# #filter_select_encodings(COMBO,ONEHOT,R'_ONEHOT')



def remove_train_rehead(library, train_seq):
    """
    Script for removing the sequences used
    to train the ML Model from the
    inference stage to avoid bias

    Returns Pandas Dataframe
    """
    dataframe = pd.read_csv(library, header=None)
    dataframe = dataframe.set_index([0])
    with open(train_seq) as file:
        for line in file:
            dataframe.drop(line.strip(), inplace=True)
            dataframe = dataframe.reset_index()
    column_names = []
    # using iterrows may be more efficient
    # #for column,k in enumerate(dataframe):
    for k in enumerate(dataframe):
        column_names.append(f"msa{k}")
    column_names[0] = 'id'
    dataframe.columns = column_names
    print(dataframe.head())
    return dataframe


remove_train_rehead(MSALIBRARY, TRAININGCOMBO, OUTPUT)

def add_combo_column_to_csv(INPUTFILE, COMBOFILE):
    """
    Script that reads in the Encodings from
    the Wittman Dataset and adds the pickle file
    with the Combinations"""
    """ 
    takes in the msa transformer csv given in the Wittman Caltech data,
    adds in the combo in the left column
    allowing for sorting in the by sort_filter_pandas 
    INPUTFILE: Big Wittman transformer
    COMBOFILE: Combinations from the pickle file
    
    Returns Pandas DF 
    """
    comboLibrary = pd.read_csv(COMBOFILE, names=['combo'])
    df = pd.read_csv(INPUTFILE, header=None, index_col=0)
    df_merge = pd.concat([comboLibrary.reset_index(drop=True), df.reset_index(drop=False)], axis=1)
    print(df_merge.head())
    return df


def remove_train_rehead(library, train_seq):
    """function called to rehead and return Pandas Dataframe
    Library: CSV file path
    train_seq: CSV file of sequences for training model
    """

    dataframe = pd.read_csv(library, header=None)
    dataframe = dataframe.set_index([0])
    with open(train_seq) as file:
        for line in file:
            dataframe.drop(line.strip(), inplace=True)
    dataframe = dataframe.reset_index()
    column_names = []
    # need to change to iterrows for more efficient run
    # for column,k in (enumerate(dataframe)):
    for k in enumerate(dataframe):
        column_names.append(f"msa{k}")
    column_names[0] = 'id'
    dataframe.columns = column_names
    print(dataframe.head())
    return dataframe
