import os
import pandas as pd
import json

# Set up paths
input_path = "data/News_Category_Dataset_v2.json"  # or .csv
output_folder = "data/articles/"
os.makedirs(output_folder, exist_ok=True)

# Load dataset
with open(input_path, "r", encoding="utf-8") as f:
    data = [json.loads(line) for line in f]

# Save each article as a .txt file
for i, entry in enumerate(data):
    text = entry.get("headline", "") + "\n" + entry.get("short_description", "")
    with open(f"{output_folder}article_{i}.txt", "w", encoding="utf-8") as out_file:
        out_file.write(text)
