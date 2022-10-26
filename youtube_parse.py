#!/usr/bin/env python

#Parses youtube playlist and returns a list of video ids


#Test-ID : PLWKMfwNQwG2MQvxQCJ-osck7omjWcUcp9

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

def youtube_parse(link, playlist: bool):
    if playlist:
        ids = []
        request = youtube.playlistItems().list(
            part="contentDetails",
            playlistId=link.split("=")[-1],
            maxResults=100
        )
        response = request.execute()

        for item in response['items']:
            ids.append(item['contentDetails']['videoId'])
        return ids
    else:
        return [link.split("=")[-1]]