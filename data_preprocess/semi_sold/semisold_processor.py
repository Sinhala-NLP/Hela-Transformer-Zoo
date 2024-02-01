from datasets import load_dataset
import csv

csv_file_path = "../../experiments/language_modeling/data/semi_sold.csv"
dataset = load_dataset("sinhala-nlp/SemiSOLD", cache_dir='C:\cacheNew\\')

with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    # Write the data to the CSV file
    for row in dataset["train"]:
        writer.writerow([row.get('text').strip()])

