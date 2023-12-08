import csv

# Load the dataset from a text file
def load_dataset(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    corpus = [line.strip() for line in lines]
    return corpus

# Replace 'path/to/dataset.txt' with the actual path to your dataset file
dataset_path = 'txt/claudia.txt'
corpus_es = load_dataset(dataset_path)

# Create a CSV file and write the data to a single column
csv_file_path = 'csv/claudia.csv'
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    for sample in corpus_es:
        csv_writer.writerow([sample])

print(f"Dataset has been converted and saved to {csv_file_path}")
