#!/usr/bin/env python

#Parses soundcloud data and returns a list of track names
import os
import requests
from dotenv import load_dotenv

load_dotenv()

uri1 = f"https://api-v2.soundcloud.com/search?q="
uri2 = f"&variant_ids=2540&facet=model&user_id=789836-829924-580721-487683&client_id={os.getenv('SOUNDCLOUD_CLIENT_ID')}"


def soundcloud_parse(link, play: bool):
    if play:
        return "Not yet implemented"
    else:
        link = link.split("/")[-1]
        print(f"{uri1}{link.replace(' ','%20')}{uri2}")
        track = requests.get(f"{uri1}{link.replace(' ','%20')}{uri2}").json()
        return f"{track.get('collection')[0].get('title')} - {track.get('collection')[0].get('user').get('username')}"
