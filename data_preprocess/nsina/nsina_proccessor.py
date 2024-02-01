import os
import json
import csv


def read_json_files_and_write_to_csv(outer_folder, csv_output_file):
    all_data = []  # List to store data from all JSON files

    # Iterate over all files and subdirectories in the outer folder
    for root, dirs, files in os.walk(outer_folder):
        for file in files:
            # Check if the file has a .json extension
            if file.endswith('.json'):
                # Construct the full path to the JSON file
                json_file_path = os.path.join(root, file)

                # Read the JSON file
                with open(json_file_path, 'r', encoding='utf-8') as json_file:
                    try:
                        # Load the JSON data
                        data = json.load(json_file)

                        # Append the data to the list
                        all_data.append(data)

                    except json.JSONDecodeError as e:
                        print(f"Error decoding JSON in {json_file_path}: {e}")

    # Write the collected data to a CSV file
    with open(csv_output_file, 'w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)

        # Write header (assuming each JSON file has the same structure)
        if all_data:
            # Write data
            for data in all_data:
                csv_writer.writerow({data['News Content'].strip()})


# Example usage
outermost_folder = 'nsina_data'
csv_output_file = '../../experiments/language_modeling/data/nsina.csv'
read_json_files_and_write_to_csv(outermost_folder, csv_output_file)
