#!/usr/bin/env python
import os
from dotenv import load_dotenv
import spotipy                                               # Boilerplate Spotify API imports
from spotipy.oauth2 import SpotifyClientCredentials
load_dotenv()

client_credentials_manager = SpotifyClientCredentials(client_id=os.getenv("SPOTIFY_CLIENT_ID"), client_secret=os.getenv("SPOTIFY_CLIENT_SECRET"))
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)   # Boilerplate Spotify API stuff

def spotify_parse(link, playlist: bool):
    if playlist:
        playlist_URI = link.split("/")[-1].split("?")[0] # Get the playlist URI from the link
        ids = []
        results = sp.playlist(playlist_URI)
        for item in results['tracks']['items']:
            ids.append(f"{item['track']['name']} - {item['track']['artists'][0]['name']}") # Get the track name and artist name from the playlist
        return ids
    else:
        track_URI = sp.track(link.split("/")[-1].split("?")[0]) # Get the track URI from the link
        return f"{track_URI['name']} - {track_URI['artists'][0]['name']}"   # Get the track name and artist name from the track
