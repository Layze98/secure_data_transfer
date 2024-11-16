import requests
import base64
from encryption import load_key, encrypt_data

server_url = "http://127.0.0.1:5000/send_data"

# Funkcja do wprowadzania danych przelewu
def get_transfer_details():
    odbiorca = input("Podaj nazwę odbiorcy: ")
    numer_konta = input("Podaj numer konta: ")
    tytul = input("Podaj tytuł przelewu: ")
    kwota = input("Podaj kwotę przelewu: ")
    
    # Tworzenie słownika z danymi
    transfer_data = {
        "odbiorca": odbiorca,
        "numer_konta": numer_konta,
        "tytul": tytul,
        "kwota": kwota
    }
    return transfer_data

def send_data(data):
    # Szyfrowanie danych
    key = load_key()
    data_str = f"{data['odbiorca']};{data['numer_konta']};{data['tytul']};{data['kwota']}"
    encrypted_data = encrypt_data(data_str, key)
    encrypted_data_base64 = base64.b64encode(encrypted_data).decode('utf-8')
    
    # Wysyłanie danych do serwera
    response = requests.post(server_url, json={"data": encrypted_data_base64})
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")

if __name__ == "__main__":
    data_to_send = get_transfer_details()
    send_data(data_to_send)
    print("Dane zostały pomyślnie wysłane.")
