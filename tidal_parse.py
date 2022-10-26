#!/usr/bin/env python

import tidalapi

session = tidalapi.Session()
with open("token.txt", "r") as f: # Read the token from token.txt
      token_type, access_token, refresh_token, expiry_time = f.read().splitlines()

session.load_oauth_session(token_type, access_token, refresh_token, expiry_time) # Load the token into the session

def tidal_parse(link, playlist: bool):
   if playlist:
      songs = []
      playlist = tidalapi.playlist.Playlist(session,link.split("/")[-1]) # Get the playlist from the link
      for track in playlist.tracks():
         songs.append(f"{track.name} - {track.artist.name}") # Get the track name and artist name from the playlist
      return songs
   else:
      return f"{tidalapi.Track(session,link.split('/')[-1]).name} - {tidalapi.Track(session,link.split('/')[-1]).artist.name}" # Get the track name and artist name from the track
