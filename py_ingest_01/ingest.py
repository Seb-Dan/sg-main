import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os
import pandas as pd

# looks for .env in the main directory
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '../config/.env'))  


# Set up the Spotify client
sp = spotipy.Spotify(
        auth_manager=
            SpotifyOAuth(
                client_id = os.getenv("client_id"),
                client_secret = os.getenv("client_secret"),
                redirect_uri="http://127.0.0.1:8000/callback",
                scope="user-read-recently-played"
            )
)

# Save the data to a file
results = sp.current_user_recently_played(limit=50)

data = [
    {
    'played_at': item['played_at'],
    'track_name': item['track']['name'],
    'artist': item['track']['artists'][0]['name'],
    'album': item['track']['album']['name'],
    'duration_ms': item['track']['duration_ms'],
    'track_id': item['track']['id']
    } 
    for item in results['items']
]

print(data)

df = pd.DataFrame(data)

df.to_csv('recently_played.csv', index=False)