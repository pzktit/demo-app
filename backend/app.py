from flask import Flask, request
from datetime import datetime
import socket

app = Flask(__name__)

@app.route('/api')
def get_info():
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    try:
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
    except:
        ip_address = "Could not get IP"

    return f"Date: {current_time}, IP: {ip_address}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)