def bytes_to_bit_list(data):
    """
    Converts bytes into a list of bits.

    Example:
    b'\xE3'
    ->
    [1,1,1,0,0,0,1,1]
    """

    bits = []

    for byte in data:

        binary = format(byte, "08b")

        for bit in binary:
            bits.append(int(bit))

    return bits