"""Library for use in sMLDE"""
import pandas as pd
import numpy as np

def pickle_to_csv(import):
    """reads in the pickle file to a csv
    to be used in add combo column
    IMPORT: pickle file to csv

    Returns to console
    """
    df = pd.read_pickle(import)
    for key, value in df.items():
        print(key)

def filter_select_encodings(selection, library, e_type):
    """pulls encodings from Wittmann data
    Selection: list of encodings
    library: selected encoding library
    Returns Pandas Dataframe
    """
    combo_list_df = pd.read_csv(selection, names = ['combo'])
    df = pd.read_csv(library, header = None)
    df = df.set_index([0])
    df = df.reindex(index=combo_list_df['combo'])
    print(df.head())
    return df

def remove_train_rehead(library, train_seq):
    """
    Script for removing the sequences used
    to train the ML Model from the
    inference stage to avoid bias

    Returns Pandas Dataframe
    """
    df = pd.read_csv(library, header=None)
    df = df.set_index([0])
    with open(train_seq) as file:
        for line in file:
            df.drop(line.strip(), inplace=True)
            df = df.reset_index()
    column_names = []
    # using iterrows may be more efficient
    # #for column,k in enumerate(df):
    for k in enumerate(df):
        column_names.append(f"msa{k}")
    column_names[0] = 'id'
    df.columns = column_names
    print(df.head())
    return df

def pull_preds(selection, predictions):
    """
    Outputs a csv of selected fitness prediction scores from csv file with prediction scores
    selection: CSV of sequences
    predictions: CSV of predictions from model
    """
    combo_list = pd.read_csv(selection, names=['combo'])
    df = pd.read_csv(predictions, header=None)
    df = df.set_index([0])
    df = df.reindex(index=combo_list['combo'])
    print(df.head())
    return df

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

    df = pd.read_csv(library, header=None)
    df = df.set_index([0])
    with open(train_seq) as file:
        for line in file:
            df.drop(line.strip(), inplace=True)
    df = df.reset_index()
    column_names = []
    # need to change to iterrows for more efficient run
    # for column,k in (enumerate(df)):
    for k in enumerate(df):
        column_names.append(f"msa{k}")
    column_names[0] = 'id'
    df.columns = column_names
    print(df.head())
    return df
