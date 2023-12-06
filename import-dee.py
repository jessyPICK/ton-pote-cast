import requests

url = "https://upload.deezer.com/?sid=fr51978ae83146e6fa40100b4af999faa6ee2bb3&id=0&resize=1&directory=user&type=audio&referer=FR&file=serieux_2.mp3"

# Assurez-vous d'avoir le fichier que vous voulez télécharger dans le même répertoire que votre script
files = {'file': open('serieux_2.mp3', 'rb')}

response = requests.post(url, files=files)

print(response.text)