from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os

def encrypt_ctr(plaintext, key, nonce):
    cipher = AES.new(key, AES.MODE_CTR, nonce=nonce)
    return cipher.encrypt(plaintext.encode())

def decrypt_ctr(ciphertext, key, nonce):
    cipher = AES.new(key, AES.MODE_CTR, nonce=nonce)
    return cipher.decrypt(ciphertext).decode()

key = get_random_bytes(16) 
nonce = os.urandom(8) 
plaintext = "Hello, AES in CTR mode!"

encrypted_data = encrypt_ctr(plaintext, key, nonce)

decrypted_data = decrypt_ctr(encrypted_data, key, nonce)

print(f"Original: {plaintext}")
print(f"Encrypted: {encrypted_data}")
print(f"Decrypted: {decrypted_data}")
