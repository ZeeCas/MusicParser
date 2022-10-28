#!/usr/bin/env python

import os
from dotenv import load_dotenv
import spotipy                                               # Boilerplate Spotify API imports
from spotipy.oauth2 import SpotifyOAuth
import time
from yaspin import yaspin
load_dotenv()

USERNAME = os.getenv("SPOTIFY_USERNAME")
CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
SCOPE = "playlist-modify-public"                            # Scope for creating a playlist


def create_spotify():
    auth_manager = SpotifyOAuth(
        scope=SCOPE,
        username=USERNAME,
        redirect_uri='http://localhost:8888/callback',
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET)

    spotify = spotipy.Spotify(auth_manager=auth_manager)

    return auth_manager, spotify

# Auth refreshing borrowed from : https://stackoverflow.com/questions/48883731/refresh-token-spotipy

def refresh_spotify(auth_manager, spotify):
    token_info = auth_manager.cache_handler.get_cached_token()
    if auth_manager.is_token_expired(token_info):
        auth_manager, spotify = create_spotify()
    return auth_manager, spotify
    

def search_spotify(spotify, track):
    results = spotify.search(q=track, limit=1)
    return results['tracks']['items'][0]['id'] # Get the track URI from the link

@yaspin(text="Creating playlist...")
def make_playlist_spotify(playlist_name, playlist_description, playlist_tracks):
    auth_manager, spotify = create_spotify()
    user_id = spotify.me()['id']
    playlist = spotify.user_playlist_create(user_id, playlist_name, public=True, description=playlist_description)
    playlist_id = playlist['id']
    track_ids = []
    for track in playlist_tracks:
        track_ids.append(search_spotify(spotify, track))
    spotify.playlist_add_items(playlist_id, track_ids)
    return playlist['external_urls']['spotify']
