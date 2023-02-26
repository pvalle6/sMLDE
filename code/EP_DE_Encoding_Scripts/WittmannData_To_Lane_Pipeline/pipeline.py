import smlde
from smlde import functions

index = smlde.functions.grab_pickle(R"B:\HardDrive_Files\Wittmann Data\MldeData\SimulationTrainingData\FilteredComboToInd.pkl")
scores = smlde.functions.read_np(R"B:\HardDrive_Files\Wittmann Data\MldeData\SimulationTrainingData\Fitness.npy")
encodings_msa = smlde.functions.read_np(R"B:\HardDrive_Files\Wittmann Data\MldeData\SimulationTrainingData\Encodings\msa_transformer.npy")

index_scores = smlde.functions.add_combo_column_to_csv(index, scores)
training_data_df = smlde.functions.add_combo_column_to_csv(index_scores, encodings_msa)

selected_seq = smlde.functions.pull_preds(R"C:\Users\Hotsauce141\Downloads\seven.csv", training_data_df)