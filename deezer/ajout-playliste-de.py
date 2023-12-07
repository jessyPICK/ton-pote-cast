import requests
fichier = 'salam'
songs_id = '-3089102891'
access_token = 'frxOvB5nfLuWiUxOSIw3vKS1DaezRvsT7ULPVIKwF7NFb3yrWX'
url = f"https://api.deezer.com/playlist/12076425051/tracks?access_token={access_token}&songs={songs_id}"

# Assurez-vous d'avoir le fichier que vous voulez télécharger dans le même répertoire que votre script


response = requests.post(url)

print(response.text)