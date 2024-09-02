from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

@app.route('/')
def home():
    # Fetch data from the Lanyard API
    lanyard_response = requests.get('https://api.lanyard.rest/v1/users/1005856471122198558')
    lanyard = lanyard_response.json()

    # Fetch data from the GitHub API
    commits_response = requests.get('https://api.github.com/repos/pagingdrepi/portfolio/commits')
    commits = commits_response.json()

    # Extract Spotify information
    spotify = lanyard.get('data', {}).get('spotify')
    title = None
    artist = None
    if spotify:
        title = spotify.get('song')
        artist = spotify.get('artist', '').split(';')[0]

    # Extract Discord status
    status = lanyard.get('discord_status')

    # Extract the latest commit message
    message = commits[0]['commit']['message'] if commits else 'No commits found'

    # Render the template with the extracted data
    return render_template('index.html', spotify=spotify, title=title, artist=artist, commit=message)
    
if __name__ == '__main__':
    app.run(debug=True)
