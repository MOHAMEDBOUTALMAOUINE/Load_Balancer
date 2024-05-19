from flask import Flask, jsonify
import requests

app = Flask(__name__)

servers = {
    "http://localhost:8000": 0,
    "http://localhost:8001": 0,
    "http://localhost:8002": 0
}

def get_server():
    return min(servers, key=servers.get)

@app.route('/')
def index():
    server = get_server()
    try:
        response = requests.get(server)
        servers[server] += 1
        return response.text
    except requests.RequestException as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)


