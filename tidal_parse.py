#!/usr/bin/env python

import tidalapi

session = tidalapi.Session()
with open("token.txt", "r") as f:
      token_type, access_token, refresh_token, expiry_time = f.read().splitlines()

session.load_oauth_session(token_type, access_token, refresh_token, expiry_time)

def tidal_parse(link, playlist: bool):
   if playlist:
      songs = []
      playlist = tidalapi.playlist.Playlist(session,link.split("/")[-1])
      for track in playlist.tracks():
         songs.append(f"{track.name} - {track.artist.name}")
      return songs
   else:
      return f"{tidalapi.Track(session,link.split('/')[-1]).name} - {tidalapi.Track(session,link.split('/')[-1]).artist.name}"
