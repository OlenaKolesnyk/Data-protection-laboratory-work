operation = input()
pseudo_random_number = int(input())
rotors = [input() for _ in range(3)]
message = input()

def caesar_shift(char, shift):
    return chr((ord(char) - ord('A') + shift) % 26 + ord('A'))

def rotor_shift(char, rotor):
    return rotor[ord(char) - ord('A')]

def process_message(operation, pseudo_random_number, rotors, message):
    result = ''
    for i, char in enumerate(message):
        shift = pseudo_random_number + i
        if operation == 'ENCODE':
            shifted = caesar_shift(char, shift)
            for rotor in rotors:
                shifted = rotor_shift(shifted, rotor)
            result += shifted
        elif operation == 'DECODE':
            shifted = char
            for rotor in reversed(rotors):
                shifted = chr(ord('A') + rotor.index(shifted))
            shifted = caesar_shift(shifted, -shift)
            result += shifted
    return result

print(process_message(operation, pseudo_random_number, rotors, message))
