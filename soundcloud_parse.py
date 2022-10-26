#!/usr/bin/env python

#Parses soundcloud data and returns a list of track names
import os
import requests
from dotenv import load_dotenv

load_dotenv()

uri1 = f"https://api-v2.soundcloud.com/search?q=" # Soundcloud API search query
uri2 = f"&variant_ids=2540&facet=model&user_id=789836-829924-580721-487683&client_id={os.getenv('SOUNDCLOUD_CLIENT_ID')}" # Soundcloud API search query part 2 electric boogaloo


def soundcloud_parse(link, play: bool):
    if play:
        return "Not yet implemented" # Playlist issues
    else:
        link = link.split("/")[-1] # Get the track URI from the link
        track = requests.get(f"{uri1}{link.replace(' ','%20')}{uri2}").json() # Make a request to the Soundcloud API
        return f"{track.get('collection')[0].get('title')} - {track.get('collection')[0].get('user').get('username')}"  # Get the track name and artist name from the track
