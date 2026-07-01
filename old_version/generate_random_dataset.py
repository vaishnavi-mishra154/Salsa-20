#old code
# from Crypto.Random import get_random_bytes
# import csv

# # -----------------------------
# # Number of samples to generate
# # -----------------------------
# NUM_SAMPLES = 100

# # -----------------------------
# # Output CSV file
# # -----------------------------
# output_file = "datasets/random.csv"

# with open(output_file, mode="w", newline="") as csv_file:

#     writer = csv.writer(csv_file)

#     # Header
#     writer.writerow([
#         "Sample_ID",
#         "Key",
#         "Nonce",
#         "Counter",
#         "Keystream"
#     ])

#     # Generate samples
#     for sample_id in range(1, NUM_SAMPLES + 1):

#         # Generate 64 random bytes
#         random_bytes = get_random_bytes(64)

#         writer.writerow([
#             sample_id,
#             "N/A",
#             "N/A",
#             "N/A",
#             random_bytes.hex()
#         ])

# print("=" * 40)
# print("Dataset Generated Successfully!")
# print(f"Total Samples : {NUM_SAMPLES}")
# print(f"Saved to      : {output_file}")
# print("=" * 40)