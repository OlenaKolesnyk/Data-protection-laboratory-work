import sys

def xor_hex_strings(hex_str1, hex_str2):
    return format(int(hex_str1, 16) ^ int(hex_str2, 16), 'x')


message_1 = input()
message_2 = input()
message_3 = input()

intermediate_message = xor_hex_strings(message_1, message_2)

clear_message_hex = xor_hex_strings(intermediate_message, message_3)

clear_message_ascii = bytes.fromhex(clear_message_hex).decode('ascii')

print(clear_message_ascii)
