from flask import Flask, jsonify
import requests

app = Flask(__name__)

servers = ["http://localhost:8000", "http://localhost:8001", "http://localhost:8002"]
current_server_index = 0

def get_server():
    global current_server_index
    server = servers[current_server_index]
    current_server_index = (current_server_index + 1) % len(servers)
    return server

@app.route('/')
def index():
    server = get_server()
    try:
        response = requests.get(server)
        return response.text
    except requests.RequestException as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
