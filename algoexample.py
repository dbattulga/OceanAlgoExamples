import os

INPUT_DIR = "/data/inputs"
OUTPUT_DIR = "/data/outputs"

total_words = 0

for root, dirs, files in os.walk(INPUT_DIR):
    for file in files:
        path = os.path.join(root, file)

        with open(path, "r", encoding="utf-8") as f:
            text = f.read()
            total_words += len(text.split())

os.makedirs(OUTPUT_DIR, exist_ok=True)

with open(os.path.join(OUTPUT_DIR, "result.txt"), "w") as f:
    f.write(f"Total words: {total_words}")

print("Done.")
