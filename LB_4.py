import hashlib

def crack(hash_to_crack):
    for pin in range(100000):
        pin_str = str(pin).zfill(5)
        hash_attempt = hashlib.md5(pin_str.encode()).hexdigest()

        if hash_attempt == hash_to_crack:
            return pin_str
