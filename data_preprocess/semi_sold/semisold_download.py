from datasets import load_dataset

dataset = load_dataset("sinhala-nlp/SemiSOLD", cache_dir='C:\cacheNew\\')
for a in dataset["train"]:
    print(a)

