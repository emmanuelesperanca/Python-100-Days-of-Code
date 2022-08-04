import requests
from bs4 import BeautifulSoup

date = input('Type the date of the playlist in a YYYY-MM-DD format.')
url = f'https://www.billboard.com/charts/hot-100/{date}/'

response = requests.get(url)
website_html = response.text
soup = BeautifulSoup(website_html, 'html.parser')

top_100_songs = soup.find_all(name='h3', class_="a-no-trucate")
songs = [music_name.getText().replace('\n', '').replace('\t', '') for music_name in top_100_songs]

config_create_playlist = {
    "name": f"100 Days of Python - Billboard Top 100 - {date}",
    "description": "Playlist created via python and spotify API, for studying purpose.",
    "public": False
}

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": "Bearer your_key_here",
}

user_id = 'your_ID_here'
create_playlist_endpoint = f'https://api.spotify.com/v1/users/{user_id}/playlists'

# create playlist
# response = requests.post(url=create_playlist_endpoint, json=config_create_playlist, headers=headers)

playlist_id = 'your_playlist_ID_here'
position = '0'

for track in songs:
    track_name = f"{track}"
    search_track_endpoint = f'https://api.spotify.com/v1/search?q={track_name}&type=track&limit=1'
    response = requests.get(url=search_track_endpoint, headers=headers)
    data = response.json()
    track_id = (data['tracks']['items'][0]['uri'].split(':')[2])
    add_song_to_playlist_endpoint = f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks?position={position}&uris=spotify%3Atrack%3A{track_id}'
    response = requests.post(url=add_song_to_playlist_endpoint, headers=headers)
