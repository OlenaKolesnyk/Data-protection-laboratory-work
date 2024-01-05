def decode_message(encoded):
    freq = [0] * 26
    for c in encoded:
        if c.isalpha():
            freq[ord(c.upper()) - ord('A')] += 1

    english_freq_order = "ETAOINSHRDLCUMWFGYPBVKJXQZ"
    decoded_message = None
    max_match_count = -1

    for i in range(len(english_freq_order)):
        shift = (get_max_freq_index(freq) - (ord(english_freq_order[i]) - ord('A'))) % 26
        shifted_message = apply_shift(encoded, shift)
        match_count = get_match_count(shifted_message)

        if match_count > max_match_count:
            max_match_count = match_count
            decoded_message = shifted_message

    return decoded_message

def get_max_freq_index(freq):
    return freq.index(max(freq))

def apply_shift(encoded, shift):
    decoded = []
    for c in encoded:
        if c.isalpha():
            base = 'A' if c.isupper() else 'a'
            shifted = chr((ord(c) - ord(base) - shift) % 26 + ord(base))
            decoded.append(shifted)
        else:
            decoded.append(c)
    return ''.join(decoded)

def get_match_count(message):
    match_count = 0
    for c in message:
        if c.isalpha() and "ETAOINSHRDLCUMWFGYPBVKJXQZ".find(c.upper()) < 6:
            match_count += 1
    return match_count

message = input()

print(decode_message(message))
