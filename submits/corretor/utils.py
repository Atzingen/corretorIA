from logging import exception
import time, random, string
from googleapiclient.discovery import build
from corretorIA.settings import YOUTUBE_API

def make_salt(size=16, chars=None):
    if not chars:
        chars = ''.join(
            [string.ascii_uppercase, 
             string.ascii_lowercase]
        )
    return ''.join(random.choice(chars) for x in range(size))


def list_videos(playlist_id):
    youtube = build("youtube", "v3", developerKey=YOUTUBE_API)
    request = youtube.playlistItems().list(
        part = "snippet",
        playlistId = playlist_id,
        maxResults = 50
    )
    response = request.execute()
    videos_data = []
    for video_data in response["items"]:
        try:
            if "standard" in video_data['snippet']['thumbnails']:
                key = "standard"
            else:
                key = "default"

            videos_data.append({
                'title': video_data['snippet']['title'],
                'image': video_data['snippet']['thumbnails'].get(key, '').get("url", ''),
                'url': 'https://www.youtube.com/watch?v=' +
                       video_data['snippet']['thumbnails'].get(key, '').get("url", '').split("/")[-2]
            })
        except:
            pass
    return videos_data



def clean_submit_scripts():
    pass
