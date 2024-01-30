import shutil
import torch
import argparse
import csv

from hela_transformers.text_classification.transformer_models.args.model_args import LanguageModelingArgs
from hela_transformers.language_modeling.language_modeling_model import LanguageModelingModel


parser = argparse.ArgumentParser(
    description='''evaluates multiple models  ''')
parser.add_argument('--model_name', required=False, help='model name', default="bert-large-cased")
parser.add_argument('--model_type', required=False, help='model type', default="bert")
parser.add_argument('--cuda_device', required=False, help='cuda device', default=0)
arguments = parser.parse_args()

with open('data/nsina_5.csv', 'rb') as csvfile, open('output_file.txt', 'w', encoding='utf-8') as txtfile:
    # Decode the content of the CSV file using utf-8
    csv_content = csvfile.read().decode('utf-8')  # 'utf-8-sig' removes the BOM

    # Use csv.reader to handle CSV content
    csv_reader = csv.reader(csv_content.splitlines())

    for row in csv_reader:
        # Convert each row to a string and write to the text file
        txtfile.write(','.join(row) + '\n')

with open('output_file.txt', encoding='utf-8') as f:
    lines = f.read().splitlines()

train_lines = lines[:int(len(lines)*.8)]
test_lines = lines[int(len(lines)*.8):len(lines)]

with open('train.txt', 'w', encoding='utf-8') as f:
    # write each integer to the file on a new line
    for line in train_lines:
        f.write(str(line) + '\n')

with open('test.txt', 'w', encoding='utf-8') as f:
    # write each integer to the file on a new line
    for line in test_lines:
        f.write(str(line) + '\n')


model_args = LanguageModelingArgs()
model_args.reprocess_input_data = True
model_args.overwrite_output_dir = True
model_args.num_train_epochs = 1
model_args.dataset_type = "simple"
model_args.train_batch_size = 16
model_args.eval_batch_size = 32
model_args.learning_rate = 3e-5
model_args.evaluate_during_training = True
model_args.evaluate_during_training_steps = 30000
model_args.save_eval_checkpoints = True
model_args.save_best_model = True
model_args.save_recent_only = True
model_args.wandb_project = "LM"
model_args.use_multiprocessing = False
model_args.use_multiprocessing_for_evaluation = False


MODEL_TYPE = arguments.model_type
MODEL_NAME = arguments.model_name
cuda_device = int(arguments.cuda_device)

train_file = "train.txt"
test_file = "test.txt"

model = LanguageModelingModel(MODEL_TYPE, MODEL_NAME, args=model_args,
                            use_cuda=torch.cuda.is_available(),
                            cuda_device=cuda_device)

# Train the model
model.train_model(train_file, eval_file=test_file)

# Evaluate the model
result = model.eval_model(test_file)

