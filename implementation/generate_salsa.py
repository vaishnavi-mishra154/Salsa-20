from Crypto.Cipher import Salsa20
from Crypto.Random import get_random_bytes
from utils import bytes_to_bit_list
import csv

# ---------------------------------
# Configuration
# ---------------------------------

NUM_SAMPLES = 10000
OUTPUT_FILE = "datasets/salsa2.csv"

print("=" * 60)
print("Generating Salsa20 Dataset...")
print("=" * 60)

with open(OUTPUT_FILE, mode="w", newline="") as csv_file:

    writer = csv.writer(csv_file)

    for sample in range(NUM_SAMPLES):

        # Generate random 256-bit key
        key = get_random_bytes(32)

        # Generate random 64-bit nonce
        nonce = get_random_bytes(8)

        cipher = Salsa20.new(
            key=key,
            nonce=nonce
        )

        # Generate first 64-byte Salsa20 keystream
        keystream = cipher.encrypt(bytes(64))

        # Convert bytes -> list of bits
        bits = bytes_to_bit_list(keystream)

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