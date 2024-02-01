from datasets import load_dataset
from transformers import AutoTokenizer
import pandas as pd
import os

def concatenate_csv_files(folder_path):
    # Iterate over all files in the folder
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.csv'):
            # Construct the full path to the CSV file
            print('file_name-', file_name)
            csv_file_path = os.path.join(folder_path, file_name)

            # Read the CSV file into a dataframe
            dataframe = pd.read_csv(csv_file_path)
            yield dataframe.iloc[:, 0]

folder_path = '../language_modeling/data'
old_tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
training_corpus = concatenate_csv_files(folder_path)
new_tokenizer = old_tokenizer.train_new_from_iterator(training_corpus, 30000)
new_tokenizer.save_pretrained("code-search-net-tokenizer_uncased")
