from Crypto.Cipher import Salsa20

# -------- Official Test Vector Inputs --------

key_hex = "8000000000000000000000000000000000000000000000000000000000000000"
nonce_hex = "0000000000000000"

key = bytes.fromhex(key_hex)
nonce = bytes.fromhex(nonce_hex)

cipher = Salsa20.new(key=key, nonce=nonce)

# Generate first 64 bytes of keystream
generated = cipher.encrypt(bytes(64)).hex()

print("=" * 60)
print("SALSA20 TEST VECTOR VERIFICATION")
print("=" * 60)

print("\nKey:")
print(key_hex)

print("\nNonce:")
print(nonce_hex)

print("\nGenerated Keystream:")
print(generated)

expected = (
    "e3be8fdd8beca2e3ea8ef9475b29a6e7"
    "003951e1097a5c38d23b7a5fad9f6844"
    "b22c97559e2723c7cbbd3fe4fc8d9a07"
    "44652a83e72a9c461876af4d7ef1a117"
)

print("\nExpected Keystream:")
print(expected)

if generated == expected:
    print("\n✅ TEST VECTOR PASSED")
else:
    print("\n❌ TEST VECTOR FAILED")