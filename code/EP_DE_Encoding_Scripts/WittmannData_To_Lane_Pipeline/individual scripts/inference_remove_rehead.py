"""Script for removing the sequences used
to train the ML Model from the
inference stage to avoid bias"""
import pandas as pd

MSALIBRARY = None
TRAININGCOMBO = None
OUTPUT = None


def remove_train_rehead(library, train_seq, output_file):
    """function called to remove training sequences"""
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
    dataframe.to_csv(output_file, index=False)


remove_train_rehead(MSALIBRARY, TRAININGCOMBO, OUTPUT)
