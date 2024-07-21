import random

from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# List of backend servers
servers = [
    'http://localhost:5001',
    'http://localhost:5002',
    'http://localhost:5003',
    'http://localhost:5004',
    'http://localhost:5005'
]

# Variable to keep track of which server to use
current_server = 0


def get_next_server():
    global current_server
    server = servers[current_server]
    current_server = (current_server + 1) % len(servers)
    return server


def get_next_server_random():
    server = servers[random.randint(0, 4)]
    return server


@app.route('/')
def load_balancer():
    server = get_next_server_random()
    try:
        response = requests.get(server)
        return response.text
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 503


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
