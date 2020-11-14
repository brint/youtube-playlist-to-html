import os

from flask import Flask
from yattag import Doc
import requests


api_key = os.environ['YOUTUBE_API_KEY']
YOUTUBE_V3_API = "https://www.googleapis.com/youtube/v3"
YOUTUBE_BASE_URL = "https://www.youtube.com"

app = Flask(__name__)


def generate_playlist_url(playlist_id):
    return("%s/playlist?list=%s" % (YOUTUBE_BASE_URL, playlist_id))


def generate_video_url(video_id, playlist_id):
    return("%s/watch?v=%s&list=%s" % (YOUTUBE_BASE_URL, video_id, playlist_id))


def get_playlist_information(playlist_id):
    payload = {'key': api_key,
               'id': playlist_id,
               'part': 'snippet'}
    r = requests.get(("%s/playlists") % (YOUTUBE_V3_API), params=payload)

    return({'playlist_id': playlist_id,
            'playlist_title': str(r.json()['items'][0]['snippet']['title']),
            'playlist_items': []})


def get_items_information(items):
    items_info = []
    for item in items:
        items_info.append({'video_id': str(item['snippet']['resourceId']['videoId']), # noqa
                           'video_title': str(item['snippet']['title'])})

    return(items_info)


def get_playlist_items(playlist_id, page_token=None):
    playlist_items = []
    payload = {'key': api_key,
               'playlistId': playlist_id,
               'maxResults': 50,
               'part': 'snippet',
               'pageToken': page_token}
    r = requests.get(("%s/playlistItems") % (YOUTUBE_V3_API), params=payload)
    playlist_items = playlist_items + get_items_information(r.json()['items'])
    if 'nextPageToken' in r.json():
        next_page_token = r.json()['nextPageToken']
        playlist_items = playlist_items + get_playlist_items(playlist_id,
                                                             next_page_token)
    return playlist_items


def print_playlist_html(contents):
    playlist_id = contents['playlist_id']
    doc, tag, text = Doc().tagtext()
    with tag('html'):
        text("Full playlist: ")
        with tag('a', href=generate_playlist_url(playlist_id)):
            text(contents['playlist_title'])
        with tag('ul'):
            for item in contents['playlist_items']:
                with tag('li'):
                    with tag('a', href=generate_video_url(item['video_id'], playlist_id)): # noqa
                        text(item['video_title'])

    return(doc.getvalue())


@app.route('/playlistid/<string:playlist_id>', methods=['GET'])
def get_playlist(playlist_id):
    contents = get_playlist_information(playlist_id)

    contents['playlist_items'] = get_playlist_items(playlist_id)

    return(print_playlist_html(contents))
