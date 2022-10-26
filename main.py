#!/usr/bin/env python
# Start : 10/29/22 8:00pm


# This is INCREDIBLY rudimentary. Hoping for better formatting as the project continues. Biggest issue right now is soundcloud playlists and youtube API quotas.

from youtube_parse import youtube_parse
from spotify_parse import spotify_parse
from tidal_parse import tidal_parse     
from track_format import format_track
import argparse

parser = argparse.ArgumentParser(description='Parse youtube and spotify playlists')

parser.add_argument('-yp', '--youtube', help='Youtube playlist url', required=False)
parser.add_argument('-sp', '--spotify', help='Spotify playlist url', required=False)
parser.add_argument('-tp', '--tidal', help='Tidal playlist url', required=False)
parser.add_argument('-yt', '--youtubetrack', help='Youtube track url', required=False)
parser.add_argument('-st', '--spotifytrack', help='Spotify track url', required=False)
parser.add_argument('-tt', '--tidaltrack', help='Tidal track url', required=False)

args = parser.parse_args()

if args.youtube:
    for track in format_track(youtube_parse(args.youtube, True)):
        print(track)
elif args.spotify:
    for track in format_track(spotify_parse(args.spotify, True)):
        print(track)
elif args.tidal:
    for track in tidal_parse(args.tidal, True):
        print(track)
elif args.youtubetrack:
    print(format_track(youtube_parse(args.youtubetrack, False)))
elif args.spotifytrack:
    print(format_track(spotify_parse(args.spotifytrack, False)))
elif args.tidaltrack:
    print(tidal_parse(args.tidaltrack, False))
else:
    print("No arguments provided")