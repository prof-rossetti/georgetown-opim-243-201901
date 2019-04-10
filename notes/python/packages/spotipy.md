# The `spotipy` Package

The `spotipy` package provides an interface into the Spotify API.

## References

The Spotify API:

  + https://developer.spotify.com/documentation/web-api/
  + https://developer.spotify.com/documentation/general/guides/authorization-guide
  + https://developer.spotify.com/documentation/general/guides/scopes/

The `spotipy` Package:

  + https://github.com/plamere/spotipy
  + https://github.com/plamere/spotipy#quick-start
  + https://spotipy.readthedocs.io/en/latest/
  + https://spotipy.readthedocs.io/en/latest/#client-credentials-flow
  + https://spotipy.readthedocs.io/en/latest/#authorization-code-flow

## Installation

First install the package, if necessary:

```sh
pip install spotipy
```

## Setup

Create a [Spotify API Client application](https://developer.spotify.com/dashboard/applications/), note its credentials, then store them in environment variables called `SPOTIPY_CLIENT_ID` and `SPOTIPY_CLIENT_SECRET`, respectively.

If your app doesn't need to make authenticated requests on behalf of the user, this setup should be sufficient. Feel free to move on to the "Unauthenticated Usage" example below.

### User Authentication

However if your app does need to make authenticated requests on behalf of the user, there are a few more setup steps involved.

First, in your client application's developer settings, you'll need to specify a redirect URL. If you're not sure which URL to designate, feel free to choose your GitHub repository URL, or a local URL like `http://localhost:5000/auth/spotify/callback`. Store the value in an environment variable called `SPOTIPY_REDIRECT_URL`.

Note your Spotify username, and store in an environment varible called `SPOTIFY_USERNAME`.

After setting the redirect URL and username, setup the code provided in the "Authenticated Usage" section below, invoke the provided `get_token()` function to obtain an access token, and store the result in an environment variable called `SPOTIFY_AUTH_TOKEN`.

> NOTE: this step also seems to download a file called `.cache-USERNAME` to the root directory of the repo. it looks like this:
>
> ```json
> {
>     "access_token": "_____",
>     "token_type": "Bearer",
>     "expires_in": 3600,
>     "refresh_token": "______",
>     "scope": "playlist-read-private",
>     "expires_at": 1554651631
> }
> ```
>
> Since this file contains secret credentials, ignore it from version control by adding an entry like `.cache-*` to your repository's ".gitignore" file.

After setting these additional environment variables, you should be able to issue requests on behalf of the user (see the provided `get_playlists()` function below).

## Usage

### Unauthenticated Usage

Example request which doesn't require authentication (i.e. a song search):

```py
# adapted from: https://github.com/s2t2/my-spotify-app-py/blob/master/list_songs.py

from dotenv import load_dotenv
import os

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

load_dotenv() # load environment variables

print("CLIENT ID:", os.environ.get("SPOTIPY_CLIENT_ID"))
print("CLIENT SECRET:", os.environ.get("SPOTIPY_CLIENT_SECRET"))

client_credentials_manager = SpotifyClientCredentials()
client = spotipy.Spotify(client_credentials_manager=client_credentials_manager) # checks for env vars SPOTIPY_CLIENT_ID and SPOTIPY_CLIENT_SECRET by default

results = client.search(q="Springsteen on Broadway", limit=20)
for i, track in enumerate(results['tracks']['items']):
    print(' ', i, track['name'])
```

### Authenticated Usage

Example request which requires authentication (i.e. listing a user's playlists):

```py
# adapted from: https://github.com/s2t2/playlist-service-py/blob/4db80cd3f8f2ed018f64bc2a97629d2af105acc3/app/spotify_service.py

import os
from dotenv import load_dotenv

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util

load_dotenv() # load environment variables

CLIENT_ID = os.environ.get("SPOTIPY_CLIENT_ID", "OOPS")
CLIENT_SECRET = os.environ.get("SPOTIPY_CLIENT_SECRET", "OOPS")
REDIRECT_URL = os.environ.get("SPOTIPY_REDIRECT_URI", "OOPS")
USERNAME = os.environ.get("SPOTIFY_USERNAME", "OOPS")
AUTH_TOKEN = os.environ.get("SPOTIFY_AUTH_TOKEN", "OOPS")

# requires user interaction
# do this initially to get a valid token, then store that token in an env var called SPOTIFY_AUTH_TOKEN to enable programmatic usage
def get_token():
    AUTH_SCOPE = "playlist-read-private"
    token = util.prompt_for_user_token(USERNAME, AUTH_SCOPE)
    # alternatively specify where the credentials file should be stored...
    #user_credentials_filepath = os.path.join(os.path.dirname(__file__), "..", "credentials", "spotify_user.json")
    #token = util.prompt_for_user_token(USERNAME, AUTH_SCOPE, cache_path=user_credentials_filepath)
    return token

# requires user auth
# and requires token configuration, i.e. get_token() and setting result as SPOTIFY_USER_AUTH_TOKEN env var
def get_playlists():
    client = spotipy.Spotify(auth=AUTH_TOKEN)

    playlists = client.current_user_playlists()

    while playlists:
        print(type(playlists))

        for i, playlist in enumerate(playlists['items']):
            print(f"{i + 1 + playlists['offset']} {playlist['uri']} {playlist['name']}")

        if playlists["next"]:
            playlists = client.next(playlists)
        else:
            playlists = None

if __name__ == "__main__":

    # get_token()

    get_playlists()
```
