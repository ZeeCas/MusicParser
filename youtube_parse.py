#!/usr/bin/env python

#Parses youtube playlist and returns a list of video ids


import os
import json
import google_auth_oauthlib.flow
import googleapiclient.discovery   # Boilerplate Youtube API imports
import googleapiclient.errors
from dotenv import load_dotenv
load_dotenv()

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

api_service_name = "youtube"
api_version = "v3"
youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey=os.getenv("YOUTUBE_API_KEY")) # Boilerplate Youtube API stuff

def youtube_parse(link, playlist: bool):
    if playlist:
        ids = []
        songs = []
        request = youtube.playlistItems().list(
            part="contentDetails",
            playlistId=link.split("=")[-1],     # Get the playlist content from the link
            maxResults=100
        )
        response = request.execute()
        for item in response['items']:
            ids.append(item['contentDetails']['videoId']) # Get the video id from the playlist
        for id in ids:
            request = youtube.search().list(
                part="snippet",
                maxResults=1,
                q=id)                       # Youtube API search query
            response = request.execute()
            for item in response['items']:
                song = item['snippet']['title']
                artist = item['snippet']['channelTitle']
                songs.append(f"{song} - {artist} : https://www.youtube.com/watch?v={id}") # Get the song name and artist name from the video id
        return songs
    else:
        return [link.split("=")[-1]] # Get the video id from the link