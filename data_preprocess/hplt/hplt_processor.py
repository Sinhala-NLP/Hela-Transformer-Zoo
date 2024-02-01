import csv
import subprocess
import json

# downloading data
# url = "https://data.hplt-project.org/one/monotext/cleaned/si/si_1.jsonl.zst"
# subprocess.run(["powershell", "Invoke-WebRequest", "-Uri", url, "-OutFile", "test_file"])

# for Linux commandline
# wget -i https://data.hplt-project.org/one/monotext/cleaned/si/si_1.jsonl.zst

# for windows powershell
# Invoke-WebRequest -Uri "https://data.hplt-project.org/one/monotext/cleaned/si/si_1.jsonl.zst" -OutFile "output_file.jsonl_1.zst"


file_path = 'output_file.jsonl_1'

with open(file_path, "r", encoding='utf-8') as file, open('../../experiments/language_modeling/data/hplt.csv', 'w', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    for line in file:
        data = json.loads(line)
        data_text = data['text']
        para = '.'.join(data_text.split('\n'))
        writer.writerow([para.strip()])

