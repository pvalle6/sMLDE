"""Library for use in sMLDE"""
import pandas as pd
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
