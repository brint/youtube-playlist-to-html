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

#### Run it on k8s locally
Docker Desktop licensing [changed](https://www.techrepublic.com/article/docker-launches-new-business-plan-with-changes-to-the-docker-desktop-license/). To be careful/safe since I do work at a larger company, I've removed Docker Desktop and moved to [Racher Desktop](https://rancherdesktop.io/). This could be turned into a helm chart and be done better. I just needed this working real quick to generate a playlist, I know it's ugly.

```
# Create your deployment
kubectl create deployment --image=brint/ytpl-to-html:0.0 ytpl-to-html

# Set your environment variable for the YouTube API key
kubectl set env deployment/ytpl-to-html YOUTUBE_API_KEY=$YOUTUBE_API_KEY

# Expose the port
kubectl expose deployment ytpl-to-html --port=5000 --name=ytpl-to-html-http

# Do a port forward so you can hit localhost:5000
kubectl port-forward service/ytpl-to-html-http 5000:5000
```
