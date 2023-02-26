"""Provides fitness scores"""
import pandas as pd

PULL = R"C:\Users\valle\OneDrive\Desktop\seq_req.csv"
# put the msa_with combination file below <- Actually, I think its a different file
PREDS = R"C:\Users\valle\OneDrive\Desktop\WitmannData\msa_transformer_with_combo.csv"
OUT = R"C:\Users\valle\OneDrive\Desktop\seq_req_75.csv"


def pull_preds(selection, predictions, output_file):
    """Outputs a csv of selected fitness prediction scores from csv file with prediction scores"""
    combo_list = pd.read_csv(selection, names=['combo'])
    dataframe = pd.read_csv(predictions, header=None)
    dataframe = dataframe.set_index([0])
    dataframe = dataframe.reindex(index=combo_list['combo'])
    print(dataframe.head())
    dataframe.to_csv(output_file, header=False)


pull_preds(PULL, PREDS, OUT)
