"""Needed to run script inference_remove_rehead
through HPC because of the slow nature of searching
the massive data for specific sequences"""
import pandas as pd

MSA_LIB = None  # msa_transformer_with_combo.csv
TRAIN_ONE = None
TRAIN_TWO = None

OUT_ONE = None
OUT_TWO = None


def remove_train_rehead(library, train_seq, output_file):
    """function called to rehead"""
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
    dataframe.to_csv(output_file, index=False)


remove_train_rehead(MSA_LIB, TRAIN_ONE, OUT_ONE)
remove_train_rehead(MSA_LIB, TRAIN_TWO, OUT_TWO)
