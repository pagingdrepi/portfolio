from flask import Flask, render_template
from requests import get
import json

app = Flask(__name__)

@app.route('/')
def home():
    lanyard = json.loads(requests.get('https://api.lanyard.rest/v1/users/1005856471122198558').text)
    commits = json.loads(requests.get('https://api.github.com/repos/pagingdrepi/portfolio/commits').text)
    
    spotify = lanyard['data']['spotify']
    title=None
    artist=None
    if spotify:
        title = spotify['song']
        artist = spotify['artist'].split(';')[0]
    status = lanyard['discord_status']

    message = commits[0]['commit']['message']
    
    return render_template('index.html', spotify=spotify, title=title, artist=artist, commit=message)

@app.route('/about')
def about():
    return 'About'
