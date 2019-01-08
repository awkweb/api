from Crypto.Cipher import AES
from Crypto import Random
from base64 import b64encode, b64decode
from os import environ


def gen_iv():
    iv = Random.new().read(AES.block_size)
    return b64encode(iv).decode()


def init_cipher(iv):
    secret_key = environ["DJ_SECRET_KEY"]
    return AES.new(secret_key[:16], AES.MODE_CFB, iv)


def encrypt(string, iv):
    cipher = init_cipher(iv)
    return b64encode(cipher.encrypt(string)).decode()


def decrypt(string, iv):
    cipher = init_cipher(iv)
    return cipher.decrypt(b64decode(string)).decode()
