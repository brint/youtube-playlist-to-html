youtube-playlist-to-text
------------------------

Convert a YouTube playlists a HTML list of videos for easy copy/paste into sites like Confluence.

YouTube updates their APIs somewhat regularly, so there's a good chance this breaks in the near future.

## Requirements
- Python 3 & pip
- Dependencies installed via `pip install -r requirements.txt`
- Google API enabled for querying the [YouTube Data API v3](https://console.developers.google.com/apis/library/youtube.googleapis.com)
- Once you've enabled the API, setup an [API Key](https://console.developers.google.com/apis/api/youtube.googleapis.com/credentials)
- Set your YouTube API key in your environment as `YOUTUBE_API_KEY`

## Setup

### Run locally
- Use a virtual environment if you can
```
mkvirtualenv ytpl -p python3
pip install -U pip
pip install -r requirements.txt
export YOUTUBE_API_KEY=12345...
flask run
```

To use the service: http://127.0.0.1:5000/playlistid/PLh7fu4nOXs14tPWMzGHC4z2Q0-RGXAY7W

## Run in Docker

### Run out of Docker hub

```
export YOUTUBE_API_KEY=12345...
docker run --rm -p 5000:5000 --env YOUTUBE_API_KEY=$YOUTUBE_API_KEY brint/ytpl-to-html:0.0
```

### build

```
docker build -t brint/ytpl-to-html:0.0 .
```

### Run it

```
export YOUTUBE_API_KEY=12345...
docker run --rm -p 5000:5000 --env YOUTUBE_API_KEY=$YOUTUBE_API_KEY brint/ytpl-to-html:0.0
```

To use the service: http://127.0.0.1:5000/playlistid/PLh7fu4nOXs14tPWMzGHC4z2Q0-RGXAY7W
