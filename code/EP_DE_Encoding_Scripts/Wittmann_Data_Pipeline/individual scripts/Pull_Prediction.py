"""Provides fitness scores"""
import pandas as pd

PULL = None
#seq_req.csv"
PREDS = None
#"Fitness.csv"
OUT = None
# "seq_req_75.csv"


def pull_preds(selection, predictions, output_file):
    """Outputs a csv of selected fitness prediction scores from csv file with prediction scores"""
    combo_list = pd.read_csv(selection, names=['combo'])
    dataframe = pd.read_csv(predictions, header=None)
    dataframe = dataframe.set_index([0])
    dataframe = dataframe.reindex(index=combo_list['combo'])
    print(dataframe.head())
    dataframe.to_csv(output_file, header=False)


pull_preds(PULL, PREDS, OUT)
