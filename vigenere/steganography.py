# steganography.py

import cv2
import os
from vigenere_cipher import encrypt, decrypt,generate_key

def hiding_data(img, msg, password):
    key = generate_key(password, len(msg))
    n, m, z = 0, 0, 0
    for i in range(len(msg)):
        img[n, m, z] = ord(encrypt(msg[i], key[i]))
        n += 1
        m += 1
        z = (z + 1) % 3
    img[n, m, z] = 0  # Append null character at the end
    return img


def extracting_data(img, password):
    n, m, z = 0, 0, 0
    message = ""
    while True:
        decrypted_char = decrypt(chr(img[n, m, z]), password[n % len(password)])
        if decrypted_char == '\0':
            break
        message += decrypted_char
        n += 1
        m += 1
        z = (z + 1) % 3
    return message


if __name__ == "__main__":
    img = cv2.imread("vigenere\\R2.png")

    password = input("Enter a password: ")
    msg = input("Enter your secret message: ")
    print()

    img = hiding_data(img, msg, password)
    cv2.imwrite("stegofileV.png", img)
    os.system("stegofileV.png")

    # Decrypting
    password_to_reveal = input("Enter the password: ")
    if password_to_reveal == password:
        revealed_msg = extracting_data(img, password)
        print("\nRevealed message:", revealed_msg)
    else:
        print("Incorrect password")
