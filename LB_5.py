def encode(string):
    ascii_values = []
    for char in string:
        ascii_values.append(ord(char))
    binary_values = []
    for value in ascii_values:
        binary_values.append(format(value, '08b'))
    tripled_bits = ''
    for bit in ''.join(binary_values):
        tripled_bits += bit * 3
       
    return tripled_bits

def decode(bits):
    grouped_bits = []
    for i in range(0, len(bits), 3):
        grouped_bits.append(bits[i:i+3])
    corrected_bits = []
    for group in grouped_bits:
        if group.count('0') > group.count('1'):
            corrected_bits.append('0')
        else:
            corrected_bits.append('1')
    binary_values = []
    for i in range(0, len(corrected_bits), 8):
        binary_values.append(''.join(corrected_bits[i:i+8]))
    ascii_values = []
    for binary in binary_values:
        ascii_values.append(int(binary, 2))
    decoded_string = ''
    for value in ascii_values:
        decoded_string += chr(value)

    return decoded_string
