
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import os

def encrypt_file(file_data): 
    key = os.urandom(32)
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()


    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(file_data) + padder.finalize()


    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()

    return iv + key + encrypted_data

def decrypt_file(encrypted_data): 
    iv = encrypted_data[:16]
    key = encrypted_data[16:48]
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()

    unpadder = padding.PKCS7(128).unpadder()
    decrypted_padded_data = decryptor.update(encrypted_data[48:]) + decryptor.finalize()
    decrypted_data = unpadder.update(decrypted_padded_data) + unpadder.finalize()
    return decrypted_data
