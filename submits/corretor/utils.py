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
    # https://stackoverflow.com/questions/62347194/youtube-api-get-all-playlist-id-from-a-channel-python
    youtube = build("youtube", "v3", developerKey=YOUTUBE_API)
    request = youtube.playlistItems().list(
    part = "snippet",
    playlistId = playlist_id,
    maxResults = 50
)
    response = request.execute()

    playlist_items = []
    while request is not None:
        response = request.execute()
        playlist_items += response["items"]
        request = youtube.playlistItems().list_next(request, response)

    print(f"total: {len(playlist_items)}")
    print(playlist_items)
    

def hello():
    yield '{"start": 1}' 
    for i in range(1, 11):
        time.sleep(0.2)
        yield '{"value": ' + str(i) + ' }' 

def clean_submit_scripts():
    pass