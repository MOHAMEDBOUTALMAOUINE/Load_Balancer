from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

servers = ["http://localhost:8000", "http://localhost:8001", "http://localhost:8002"]
current_server_index = 0
sticky_sessions = {}

def get_server():
    global current_server_index
    server = servers[current_server_index]
    current_server_index = (current_server_index + 1) % len(servers)
    return server

@app.route('/')
def index():
    client_ip = request.remote_addr
    if client_ip in sticky_sessions:
        server = sticky_sessions[client_ip]
    else:
        server = get_server()
        sticky_sessions[client_ip] = server
    try:
        response = requests.get(server)
        return response.text
    except requests.RequestException as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
