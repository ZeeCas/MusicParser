#!/usr/bin/env python

import os
import json
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from dotenv import load_dotenv
load_dotenv()

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

api_service_name = "youtube"
api_version = "v3"

youtube = googleapiclient.discovery.build(
    api_service_name, api_version, developerKey=os.getenv("YOUTUBE_API_KEY"))


def format_track(music_data: list or string, youtube_output: bool = False):
    tracklist = []
    if youtube_output:
        for track in music_data:
            artist = track.split(" - ")[1]
            song = track.split(" - ")[0]
            request = youtube.search().list(
                part="snippet",
                maxResults=25,
                q="{} {}".format(song, artist)
            )
            response = request.execute()
            for item in response['items']:
                if item['id']['kind'] == "youtube#video":
                    tracklist.append(f"{song} - {artist} : https://www.youtube.com/watch?v={item['id']['videoId']}")
                    break
            
        return tracklist
    else:
        return music_data