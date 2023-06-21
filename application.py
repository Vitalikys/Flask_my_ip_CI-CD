import requests
from flask import Flask, render_template
import socket      # for IP address
import subprocess  # run linux bash cmd

app = Flask(__name__)


def get_hostmname_I():
    """
    get IP from linux bash. Using subprocess module
    :return: Exception text or IP
    """
    try:
        command = 'hostname -I'
        return subprocess.check_output(command, shell=True).decode('utf-8')
    except Exception as e:
        return f"Got an exception when calling 'hostname -I'; \n {str(e)}"


@app.route('/')
def index():
    try:
        ip_address = requests.get('https://ident.me').text
        ip_identme = ip_address.strip()
        # ip_identme = ip_address.decode('utf-8'))
        ip = requests.get("http://checkip.amazonaws.com/").text
        print(f"Public IP address: {ip_address}")

        # get IP from linux bash
        ip_host = get_hostmname_I()
    except Exception as e:
        return str(e)

    return render_template('index.html', ip_identme=ip_identme, ip=ip, ip_host=ip_host)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)
