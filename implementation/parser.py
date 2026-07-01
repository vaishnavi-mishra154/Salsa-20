import re


def parse_test_vectors(filename):
    """
    Reads the official ECRYPT Salsa20 test vector file
    and extracts:

    - Set number
    - Vector number
    - Key
    - IV
    - stream[0..63]
    """

    with open(filename, "r") as file:
        lines = file.readlines()

    vectors = []

    i = 0

    while i < len(lines):

        line = lines[i]

        # ----------------------------
        # Beginning of a new test vector
        # ----------------------------
        match = re.match(r"Set\s+(\d+),\s+vector#\s+(\d+):", line)

        if match:

            set_number = int(match.group(1))
            vector_number = int(match.group(2))

            # ----------------------------
            # Read Key (2 lines)
            # ----------------------------

            key_line1 = lines[i + 1].split("=")[1].strip()
            key_line2 = lines[i + 2].strip()

            key = key_line1 + key_line2

            # ----------------------------
            # Read IV
            # ----------------------------

            iv = lines[i + 3].split("=")[1].strip()

            # ----------------------------
            # Read stream[0..63]
            # ----------------------------

            stream_line1 = lines[i + 4].split("=")[1].strip()
            stream_line2 = lines[i + 5].strip()
            stream_line3 = lines[i + 6].strip()
            stream_line4 = lines[i + 7].strip()

            stream = (
                stream_line1
                + stream_line2
                + stream_line3
                + stream_line4
            )

            vectors.append({
                "set": set_number,
                "vector": vector_number,
                "key": key,
                "iv": iv,
                "expected": stream
            })

        i += 1

    return vectors


if __name__ == "__main__":

    vectors = parse_test_vectors(
    "test_vectors/salsa20-256.64-verified.test-vectors"
    )

    print(f"Loaded {len(vectors)} test vectors.\n")

    print("First Vector")
    print(vectors[0])

    print("\nLast Vector")
    print(vectors[-1])