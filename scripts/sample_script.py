import pandas as pd
import os

large_csv_path = "data/raw/nyc_collisions_2020-2025.csv"
sample_csv_path = "data/raw/nyc_collisions_sample.csv"

if not os.path.isdir("data/raw"):
    raise FileNotFoundError("Ensure data/raw/ directory exists.")

chunk_size      = 200_000       # rows per chunk
sample_fraction = 0.05          # 5% sample from each chunk

sampled_chunks = []
for chunk in pd.read_csv(large_csv_path, chunksize=chunk_size):
    sampled_chunk = chunk.sample(frac=sample_fraction, random_state=42)
    sampled_chunks.append(sampled_chunk)

df_sample = pd.concat(sampled_chunks, ignore_index=True)

df_sample.to_csv(sample_csv_path, index=False)

#Summarizes new sample dataset:
num_rows = len(df_sample)
size_kb  = os.path.getsize(sample_csv_path) // 1024
print(f"Sampled rows: {num_rows}")
print(f"Sample size: {size_kb} KB")