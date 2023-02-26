"""Library for use in smlde"""
import pandas
import pandas as pd
import numpy as np
from pandas import DataFrame


def grab_pickle(import_file):
    """reads in the pickle file to a csv
    to be used in add combo column

    Keyword arguments:
    import_file: pickle file to csv

    Returns to console
    """
    df = pd.read_pickle(import_file)
    for key, value in df.items():
        print(key)


# def filter_select_encodings(selection, library) -> DataFrame:
#     """Pulls encodings from Wittmann data
#
#     Keyword arguments:
#     selection: list of encodings
#     library: selected encoding library
#
#     Returns Pandas Dataframe
#     """
#
#     combo_list_df = pd.read_csv(selection, names=['combo']
#     df = library.set_index([0])
#     df = df.reindex(index=combo_list_df['combo'])
#     print(df.head())
#     return df


def pull_preds(selection, predictions):
    """Outputs a csv of selected fitness prediction scores from csv file with prediction scores

    Keyword arguments:
    selection: CSV of sequences
    predictions: CSV of predictions from model
    """

    combo_list = pd.read_csv(selection, names=['combo'])
    df = pd.read_csv(predictions, header=None)
    df = df.set_index([0])
    df = df.reindex(index=combo_list['combo'])
    print(df.head())
    return df


def add_combo_column_to_csv(index_df, addition):
    """Script that reads in the Encodings from
    the Wittman Dataset and adds the pickle file
    with the Combinations

    Takes in the msa transformer csv given in the
        Wittman Caltech data,
        adds in the combo in the left column
        allowing for sorting in the by sort_filter_pandas
    input_file: big wittman transformer
    combo_file: Combinations from the pickle file

    Returns Pandas DF
    """
    df_merge = pd.concat([index_df.reset_index(drop=True), addition.reset_index(drop=False)], axis=1)
    print(df_merge.head())
    return df


def read_np(filepath_):
    """Reads numpy and prints out"""
    return pd.read_numpy(filepath_)



def remove_train_rehead(library, train_seq):
    """function called to remove sequences used in training dta
    Library: CSV file path
    train_seq: CSV file of sequences for training model

    Returns Pandas Dataframe
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
