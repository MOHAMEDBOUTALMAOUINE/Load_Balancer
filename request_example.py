import requests
import threading
import matplotlib.pyplot as plt

# URL du load balancer
LOAD_BALANCER_URL = "http://localhost:5000"

# Nombre total de requêtes à envoyer
NUM_REQUESTS = 20

# Dictionnaire pour stocker le nombre de requêtes envoyées à chaque serveur
requests_count = {"Server 1": 0, "Server 2": 0, "Server 3": 0}

# Verrou pour garantir la cohérence lors de la modification de requests_count
lock = threading.Lock()

# Fonction pour envoyer une requête au load balancer
def send_request():
    try:
        # Envoyer une requête GET au load balancer
        response = requests.get(LOAD_BALANCER_URL)
        # Convertir le contenu de la réponse en texte
        response_text = response.text.strip()
        # Vérifier si le contenu de la réponse correspond à un nom de serveur connu
        for server_name in requests_count.keys():
            if server_name in response_text:
                # Mettre à jour le nombre de requêtes pour le serveur correspondant
                with lock:
                    requests_count[server_name] += 1
                break  # Sortir de la boucle une fois qu'un serveur est identifié
    except requests.RequestException as e:
        print(f"Une erreur est survenue lors de la requête : {e}")

# Créer une liste pour stocker les threads
threads = []

# Lancer les threads pour envoyer les requêtes
for _ in range(NUM_REQUESTS):
    thread = threading.Thread(target=send_request)
    thread.start()
    threads.append(thread)

# Attendre que tous les threads se terminent
for thread in threads:
    thread.join()

# Afficher le nombre de requêtes envoyées à chaque serveur
print("Répartition des requêtes sur les serveurs :")
for server, count in requests_count.items():
    print(f"{server}: {count}")

# Créer un graphique pour visualiser la répartition des requêtes
plt.bar(requests_count.keys(), requests_count.values())
plt.xlabel('Serveurs')
plt.ylabel('Nombre de requêtes')
plt.title('Répartition des requêtes sur les serveurs')
plt.show()
