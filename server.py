from flask import Flask, request, jsonify
import base64
from encryption import load_key, decrypt_data

app = Flask(__name__)

key = load_key()
transactions = []  # Lista do przechowywania przelewów

@app.route('/send_data', methods=['POST'])
def receive_data():
    if request.method == 'POST':
        encrypted_data_base64 = request.json.get('data')
        if not encrypted_data_base64:
            return jsonify({"error": "No data received"}), 400

        try:
            # Dekodowanie i odszyfrowanie danych
            encrypted_data = base64.b64decode(encrypted_data_base64)
            decrypted_data = decrypt_data(encrypted_data, key)
            
            # Przetwarzanie odszyfrowanych danych
            odbiorca, numer_konta, tytul, kwota = decrypted_data.split(';')
            transactions.append({
                "odbiorca": odbiorca,
                "numer_konta": numer_konta,
                "tytul": tytul,
                "kwota": kwota
            })
            return jsonify({"message": "Data received successfully"}), 200
        except Exception as e:
            return jsonify({"error": "Decryption failed"}), 500

@app.route('/')
def display_transactions():
    # Strona z listą przelewów
    html = "<h1>Lista przelewów</h1><table border='1'>"
    html += "<tr><th>Odbiorca</th><th>Numer konta</th><th>Tytuł</th><th>Kwota</th></tr>"
    for trans in transactions:
        html += f"<tr><td>{trans['odbiorca']}</td><td>{trans['numer_konta']}</td><td>{trans['tytul']}</td><td>{trans['kwota']}</td></tr>"
    html += "</table>"
    return html

if __name__ == "__main__":
    print("Uruchamianie serwera...")
    app.run(debug=False)
