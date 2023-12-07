import requests

# Remplacez ces valeurs par vos clés d'API et le token d'accès obtenu
client_id = '5717998831'
client_secret = '3deb9b529eded51d158a4bb45160a27d'
access_token = 'frxOvB5nfLuWiUxOSIw3vKS1DaezRvsT7ULPVIKwF7NFb3yrWX'

# Point de terminaison pour créer une playlist
endpoint = 'https://api.deezer.com/user/me/playlists'

# Paramètres requis pour créer une playlist
params = {
    'access_token': access_token,
    'title': 'kaka',  # Remplacez par le nom de votre playlist
}

# Effectuer la requête POST
response = requests.post(endpoint, params=params)

# Vérifier la réponse
if response.status_code == 201:
    print('Playlist "kaka" créée avec succès!')
else:
    print('Erreur lors de la création de la playlist. Code d\'erreur :', response.status_code)