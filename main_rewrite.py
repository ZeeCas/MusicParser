#!/usr/bin/env python

from youtube_parse import youtube_parse
from spotify_parse import spotify_parse
from tidal_parse import tidal_parse     
from track_format import format_track
from make_playlist_spotify import make_playlist_spotify
from soundcloud_parse import soundcloud_parse
import inquirer

def main():
    choice = inquirer.list_input('What would you like to do?',choices=['Convert a playlist', 'Convert a track', 'Exit'])
    if choice == 'Convert a playlist':
        destinate = inquirer.list_input('Where would you like to convert to?',choices=['Spotify','Youtube Links', 'Exit'])
        if destinate == 'Spotify':
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
        elif destinate == 'Youtube Links':
            playlist_choice = inquirer.list_input('What service is your playlist on?', choices=['Spotify', 'Tidal'])
            if playlist_choice == 'Spotify':
                filename = inquirer.text('Enter the name of the file') # Get the name of the file to write to
                spotify_playlist = inquirer.text('Enter the Spotify playlist url')
                with open(filename, "w") as f: # Open the file to write to
                    for track in format_track(spotify_parse(spotify_playlist, True), True):
                        f.write(f"{track}\n")
            elif playlist_choice == 'Tidal':
                tidal_playlist = inquirer.text('Enter the Tidal playlist url')
                filename = inquirer.text('Enter the name of the file') # Get the name of the file to write to
                with open(filename, "w") as f: # Open the file to write to
                    for track in format_track(tidal_parse(tidal_playlist, True), True):
                        f.write(f"{track}\n")
    elif choice == 'Convert a track':
        track_choice = inquirer.list_input('What service is your track on?', choices=['Youtube', 'Spotify', 'Tidal', 'Soundcloud'])
        if track_choice == 'Youtube':
            youtube_track = inquirer.text('Enter the Youtube track url')
            print(format_track(youtube_parse(youtube_track, False), True)
            .replace('[', '')
            .replace(']', '')
            .replace("'", ''))
        elif track_choice == 'Spotify':
            spotify_track = inquirer.text('Enter the Spotify track url')
            print(format_track(spotify_parse(spotify_track, False), True)
            .replace('[', '')
            .replace(']', '')
            .replace("'", ''))
        elif track_choice == 'Tidal':
            tidal_track = inquirer.text('Enter the Tidal track url')
            print(str(format_track(tidal_parse(tidal_track, False), True))
            .replace('[', '')
            .replace(']', '')
            .replace("'", ''))
        elif track_choice == 'Soundcloud':
            soundcloud_track = inquirer.text('Enter the Soundcloud track url')
            print(str(format_track(soundcloud_parse(soundcloud_track, False), True))
            .replace('[', '')
            .replace(']', '')
            .replace("'", ''))
        else:
            print('Please enter a valid track url')


if __name__ == '__main__':
    main()