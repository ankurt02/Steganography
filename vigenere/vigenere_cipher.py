import string

def generate_key(password, length):
    password = password.lower()
    key = ''
    for i in range(length):
        key += password[i % len(password)]
    return key

def encrypt(plaintext, key):
    encrypted_text = ''
    for i in range(len(plaintext)):
        char = plaintext[i]
        if char.isalpha():
            shift = ord(key[i]) - ord('a')
            if char.islower():
                encrypted_char = chr((ord(char) + shift - ord('a')) % 26 + ord('a'))
            else:
                encrypted_char = chr((ord(char) + shift - ord('A')) % 26 + ord('A'))
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(ciphertext, key):
    decrypted_text = ''
    for i in range(len(ciphertext)):
        char = ciphertext[i]
        if char.isalpha():
            shift = ord(key[i]) - ord('a')
            if char.islower():
                decrypted_char = chr((ord(char) - shift - ord('a')) % 26 + ord('a'))
            else:
                decrypted_char = chr((ord(char) - shift - ord('A')) % 26 + ord('A'))
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text


