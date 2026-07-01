#old code
#  from Crypto.Cipher import Salsa20
# from Crypto.Random import get_random_bytes
# import csv

# # -----------------------------
# # Number of samples to generate
# # -----------------------------
# NUM_SAMPLES = 100

# # -----------------------------
# # Output CSV file
# # -----------------------------
# output_file = "datasets/salsa.csv"

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

#         # Generate random 256-bit key (32 bytes)
#         key = get_random_bytes(32)

#         # Generate random 64-bit nonce (8 bytes)
#         nonce = get_random_bytes(8)

#         # Counter = 0 (first Salsa20 block)
#         counter = 0

#         cipher = Salsa20.new(
#             key=key,
#             nonce=nonce
#         )

#         # Generate first 64-byte keystream block
#         keystream = cipher.encrypt(bytes(64))

#         writer.writerow([
#             sample_id,
#             key.hex(),
#             nonce.hex(),
#             counter,
#             keystream.hex()
#         ])

# print("=" * 40)
# print("Dataset Generated Successfully!")
# print(f"Total Samples : {NUM_SAMPLES}")
# print(f"Saved to      : {output_file}")
# print("=" * 40)