from Crypto.Cipher import Salsa20
from parser import parse_test_vectors

# ---------------------------------
# Load all official test vectors
# ---------------------------------

vectors = parse_test_vectors(
    "test_vectors/salsa20-256.64-verified.test-vectors"
)

passed = 0
failed = 0

print("=" * 60)
print("VERIFYING SALSA20 IMPLEMENTATION")
print("=" * 60)
print()

# ---------------------------------
# Verify every test vector
# ---------------------------------

for vector in vectors:

    key = bytes.fromhex(vector["key"])
    nonce = bytes.fromhex(vector["iv"])

    cipher = Salsa20.new(
        key=key,
        nonce=nonce
    )

    # Generate first 64-byte keystream block
    generated = cipher.encrypt(bytes(64)).hex()

    expected = vector["expected"].lower()

    if generated == expected:

        print(
            f"[PASS] Set {vector['set']} "
            f"Vector {vector['vector']}"
        )

        passed += 1

    else:

        print(
            f"[FAIL] Set {vector['set']} "
            f"Vector {vector['vector']}"
        )

        print("Expected:")
        print(expected)

        print("\nGenerated:")
        print(generated)
        print()

        failed += 1

print()
print("=" * 60)
print("VERIFICATION SUMMARY")
print("=" * 60)

print(f"Vectors Tested : {len(vectors)}")
print(f"Passed         : {passed}")
print(f"Failed         : {failed}")

if failed == 0:
    print("\n✅ Salsa20 implementation verified successfully.")
else:
    print("\n❌ Verification failed.")

#OLD CODE
# from Crypto.Cipher import Salsa20

# key = bytes.fromhex(
#     "8000000000000000000000000000000000000000000000000000000000000000"
# )

# nonce = bytes.fromhex("0000000000000000")

# cipher = Salsa20.new(key=key, nonce=nonce)

# keystream = cipher.encrypt(bytes(64))

# print("Key:")
# print(key.hex())

# print("\nNonce:")
# print(nonce.hex())

# print("\nKeystream (64 bytes):")
# print(keystream.hex())


# print("\nLength:")
# print(len(keystream))