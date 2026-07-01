#Here the 512 bits come directly from Python's cryptographically secure random number generator (CSPRNG).
from Crypto.Random import get_random_bytes
from utils import bytes_to_bit_list
import csv

# ---------------------------------
# Configuration
# ---------------------------------

NUM_SAMPLES = 10000
OUTPUT_FILE = "datasets/random.csv"

print("=" * 60)
print("Generating Random Dataset...")
print("=" * 60)

with open(OUTPUT_FILE, mode="w", newline="") as csv_file:

    writer = csv.writer(csv_file)

    for sample in range(NUM_SAMPLES):

        # Generate 64 cryptographically random bytes
        random_bytes = get_random_bytes(64)

        # Convert bytes -> list of bits
        bits = bytes_to_bit_list(random_bytes)

        # Write one row
        writer.writerow(bits)

        # Progress update every 1000 rows
        if (sample + 1) % 1000 == 0:
            print(f"{sample + 1} samples completed")

print()
print("=" * 60)
print("Dataset Generation Complete")
print("=" * 60)
print(f"Saved to : {OUTPUT_FILE}")
print(f"Rows     : {NUM_SAMPLES}")
print(f"Columns  : {len(bits)}")