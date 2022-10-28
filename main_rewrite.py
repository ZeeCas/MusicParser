#!/usr/bin/env python

from youtube_parse import youtube_parse
from spotify_parse import spotify_parse
from tidal_parse import tidal_parse     
from track_format import format_track
from make_playlist_spotify import make_playlist_spotify
import inquirer

def main():
    choice = inquirer.list_input('What would you like to do?',choices=['Convert a playlist', 'Convert a track', 'Exit'])
    if choice == 'Convert a playlist':
        playlist_choice = inquirer.list_input('What service is your playlist on?', choices=['Youtube', 'Tidal'])
        if playlist_choice == 'Youtube':
            youtube_playlist = inquirer.text('Enter the Youtube playlist url')
            playlist_name = inquirer.text('Enter the name of the playlist')
            print(make_playlist_spotify(playlist_name, "Playlist converted using Music Parse", youtube_parse(youtube_playlist, True)))

        elif playlist_choice == 'Tidal':
            tidal_playlist = inquirer.text('Enter the Tidal playlist url')
            playlist_name = inquirer.text('Enter the name of the playlist')
            print(make_playlist_spotify(playlist_name, "Playlist converted using Music Parse", format_track(tidal_parse(tidal_playlist, True))))
        else:
            print('Please enter a valid playlist url')
    elif choice == 'Convert a track':
        track_choice = inquirer.list_input('What service is your track on?', choices=['Youtube', 'Spotify', 'Tidal'])
        if track_choice == 'Youtube':
            youtube_track = inquirer.text('Enter the Youtube track url')
            print(format_track(youtube_parse(youtube_track, False), True))
        elif track_choice == 'Spotify':
            spotify_track = inquirer.text('Enter the Spotify track url')
            print(format_track(spotify_parse(spotify_track, False), True))
        elif track_choice == 'Tidal':
            tidal_track = inquirer.text('Enter the Tidal track url')
            print(format_track(tidal_parse(tidal_track, False), True))
        else:
            print('Please enter a valid track url')


if __name__ == '__main__':
    main()