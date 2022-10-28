#!/usr/bin/env python
# Start : 10/29/22 8:00pm


###################################
# [DEPRECATED]
###################################
# This is INCREDIBLY rudimentary. Hoping for better formatting as the project continues. Biggest issue right now is soundcloud playlists and youtube API quotas.

from youtube_parse import youtube_parse
from spotify_parse import spotify_parse
from tidal_parse import tidal_parse     
from track_format import format_track
from make_playlist_spotify import make_playlist_spotify
import argparse

parser = argparse.ArgumentParser(description='Parse youtube and spotify playlists')

parser.add_argument('-yp', '--youtube', help='Youtube playlist url', required=False)
parser.add_argument('-sp', '--spotify', help='Spotify playlist url', required=False)
parser.add_argument('-tp', '--tidal', help='Tidal playlist url', required=False)
parser.add_argument('-yt', '--youtubetrack', help='Youtube track url', required=False)
parser.add_argument('-st', '--spotifytrack', help='Spotify track url', required=False)
parser.add_argument('-tt', '--tidaltrack', help='Tidal track url', required=False)
parser.add_argument('-p', '--playlist', help='Playlist name', required=False) # This is the name of the playlist that will be created on Spotify

args = parser.parse_args()

if args.youtube:
    if args.playlist:
        print(make_playlist_spotify(args.playlist, "Playlist converted using Music Parse", youtube_parse(args.youtube, True)))
    else:
        print(youtube_parse(args.youtube, True))
elif args.spotify:
    if args.playlist:
        print(make_playlist_spotify(args.playlist, "Playlist converted using Music Parse", format_track(spotify_parse(args.spotify, True))))
    else:
        print(spotify_parse(args.spotify, True)) # This is the name of the playlist that will be created on Spotify
elif args.tidal:
    if args.playlist:
        print(make_playlist_spotify(args.playlist, "Playlist converted using Music Parse", format_track(tidal_parse(args.tidal, True))))
    else:
        print(format_track(tidal_parse(args.tidal, True), True)) # This is the name of the playlist that will be created on Spotify
elif args.youtubetrack:
    print(format_track(youtube_parse(args.youtubetrack, False), True)) # This is the name of the playlist that will be created on Spotify
elif args.spotifytrack:
    print(format_track(spotify_parse(args.spotifytrack, False), True)) # This is the name of the playlist that will be created on Spotify
elif args.tidaltrack:
    print(format_track(tidal_parse(args.tidaltrack, False), True)) # This is the name of the playlist that will be created on Spotify
else:
    print("Please enter a valid playlist or track url")
