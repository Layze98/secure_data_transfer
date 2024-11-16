from cryptography.fernet import Fernet

def generate_key():
    """Generuje klucz i zapisuje go do pliku."""
    key = Fernet.generate_key()
    with open("server_key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    """Wczytuje klucz z pliku."""
    with open("server_key.key", "rb") as key_file:
        return key_file.read()

def encrypt_data(data, key):
    """Szyfruje dane przy użyciu podanego klucza."""
    fernet = Fernet(key)
    return fernet.encrypt(data.encode())

def decrypt_data(encrypted_data, key):
    """Odszyfrowuje dane przy użyciu podanego klucza."""
    fernet = Fernet(key)
    return fernet.decrypt(encrypted_data).decode()
