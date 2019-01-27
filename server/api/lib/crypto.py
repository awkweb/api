from cryptography.fernet import Fernet


def gen_iv():
    iv = Fernet.generate_key()
    return iv.decode()


def encrypt(string, iv):
    cipher = Fernet(iv)
    data = string.encode()
    return cipher.encrypt(data).decode()


def decrypt(string, iv):
    cipher = Fernet(iv)
    data = string.encode()
    return cipher.decrypt(data).decode()

