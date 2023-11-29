#!/usr/bin/python

import argparse
import os
import sys  # Add this import statement

import google.oauth2.credentials
import google_auth_oauthlib.flow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow

CLIENT_SECRETS_FILE = 'client_secret.json'
SCOPES = ['https://www.googleapis.com/auth/youtube']
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'

def get_authenticated_service():
    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
    credentials = flow.run_console()
    return build(API_SERVICE_NAME, API_VERSION, credentials=credentials)

def update_video(youtube, args):
    videos_list_response = youtube.videos().list(
        id=args.video_id,
        part='snippet'
    ).execute()

    if not videos_list_response['items']:
        print('Video "%s" was not found.' % args.video_id)
        sys.exit(1)

    videos_list_snippet = videos_list_response['items'][0]['snippet']

    if args.title:
        videos_list_snippet['title'] = args.title
    if args.description:
        videos_list_snippet['description'] = args.description

    if 'tags' not in videos_list_snippet:
        videos_list_snippet['tags'] = []
    if args.tags:
        videos_list_snippet['tags'] = args.tags.split(',')
    elif args.add_tag:
        videos_list_snippet['tags'].append(args.add_tag)

    print(videos_list_snippet)

    videos_update_response = youtube.videos().update(
        part='snippet',
        body=dict(
            snippet=videos_list_snippet,
            id=args.video_id
        )).execute()

    print('The updated video metadata is:\n' +
          'Title: ' + videos_update_response['snippet']['title'] + '\n')
    if videos_update_response['snippet']['description']:
        print('Description: ' +
              videos_update_response['snippet']['description'] + '\n')
    if videos_update_response['snippet']['tags']:
        print('Tags: ' + ','.join(videos_update_response['snippet']['tags']) + '\n')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--video_id', help='ID of video to update.',
                        required=True)
    parser.add_argument('--tags',
                        help='Comma-separated list of tags relevant to the video. This argument ' +
                             'replaces the existing list of tags.')
    parser.add_argument('--add_tag', help='Additional tag to add to video. ' +
                                          'This argument does not affect current tags.')
    parser.add_argument('--title', help='Title of the video.')
    parser.add_argument('--description', help='Description of the video.')
    args = parser.parse_args()

    youtube = get_authenticated_service()
    try:
        update_video(youtube, args)
    except HttpError as e:  # Corrected syntax for catching exceptions
        print('An HTTP error %d occurred:\n%s' % (e.resp.status, e.content))
        print('Tag "%s" was added to video id "%s".' % (args.add_tag, args.video_id))

"""
delete	DELETE /playlistItems	Supprime un élément de la playlist.
insert	POST /playlistItems	Ajoute une ressource à une playlist.
list	GET /playlistItems	Renvoie une collection d'éléments de playlist correspondant aux paramètres de requête API. Vous pouvez récupérer tous les éléments d'une playlist spécifique ou un ou plusieurs éléments d'une playlist en fonction de leur identifiant unique.
update	PUT /playlistItems	Modifie un élément de la playlist. Par exemple, vous pouvez modifier la position de l'élément dans la playlist.

URI relatifs à https://www.googleapis.com/youtube/v3
set	POST /thumbnails/set	Met en ligne une miniature de vidéo personnalisée sur YouTube et la définit pour une vidéo.

Méthode	Requête HTTP	Description
URI relatifs à https://www.googleapis.com/youtube/v3
insert	POST /videos	Met en ligne une vidéo sur YouTube et définit éventuellement ses métadonnées.
list	GET /videos	Affiche une liste de vidéos qui correspondent aux paramètres de requête API.
delete	DELETE /videos	Supprime une vidéo YouTube.
update	PUT /videos	Met à jour les métadonnées d'une vidéo.
rate	POST /videos/rate	Ajoutez une note sur "J'aime" ou "Je n'aime pas" à une vidéo, ou supprimez la note attribuée à une vidéo.
getRating	GET /videos/getRating	Récupère les notes que l'utilisateur autorisé a attribuées à une liste de vidéos spécifiées.
reportAbuse	POST /videos/reportAbuse	Signaler une vidéo pour son contenu abusif.

"""