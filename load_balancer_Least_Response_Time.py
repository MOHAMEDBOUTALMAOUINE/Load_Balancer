from flask import Flask, request
import time

app = Flask(__name__)

# Dictionnaire pour stocker les temps de réponse de chaque serveur
response_times = {
    "Server 1": 1,
    "Server 2": 0.8,
    "Server 3": 1.2
}

@app.route('/')
def load_balancer():
    # Trouver le serveur avec le temps de réponse le plus bas
    min_response_time = min(response_times.values())
    selected_server = [server for server, time in response_times.items() if time == min_response_time][0]
    return f"La requête a été dirigée vers : {selected_server}"

if __name__ == '__main__':
    app.run(debug=True)
