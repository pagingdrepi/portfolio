from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

@app.route('/')
def home():
    try:
        # Fetch data from the Lanyard API
        lanyard_response = requests.get('https://api.lanyard.rest/v1/users/1005856471122198558')
        lanyard_response.raise_for_status()  # Raise an exception for HTTP errors
        lanyard = lanyard_response.json()
        
        # Fetch data from the GitHub API
        commits_response = requests.get('https://api.github.com/repos/pagingdrepi/portfolio/commits')
        commits_response.raise_for_status()  # Raise an exception for HTTP errors
        commits = commits_response.json()

        # Extract Spotify information
        spotify = lanyard.get('data', {}).get('spotify')
        title = None
        artist = None
        if spotify:
            title = spotify.get('song').lower()
            artist = spotify.get('artist', '').split(';')[0].lower()

        # Extract Discord status
        status = lanyard.get('data', {}).get('discord_status')

        # Extract the latest commit message
        message = commits[0]['commit']['message'] if commits else 'No commits found'

        # Render the template with the extracted data
        return render_template('index.html', spotify=spotify, title=title, artist=artist, commit=message, status=status)
    
    except requests.RequestException as e:
        # Handle exceptions related to network or HTTP errors
        return f"An error occurred: {e}", 500

if __name__ == '__main__':
    app.run(debug=True)
