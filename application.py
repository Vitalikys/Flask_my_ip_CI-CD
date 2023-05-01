import requests
from flask import Flask, render_template
import socket  # for IP address

app = Flask(__name__)


@app.route('/')
def index():
    try:
        ip_address = requests.get('https://ident.me').text
        ip_identme = ip_address.strip()
        # ip_identme = ip_address.decode('utf-8'))
        print(f"Public IP address: {ip_address}")
    except Exception as e:
        return str(e)

    return render_template('index.html', ip_identme=ip_identme)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)
