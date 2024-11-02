from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

@app.route('/')
def home():
    try:
        
        # Fetch data from the GitHub API
        commits_response = requests.get('https://api.github.com/repos/pagingdrepi/portfolio/commits')
        commits_response.raise_for_status()  # Raise an exception for HTTP errors
        commits = commits_response.json()

        # Extract the latest commit message
        message = commits[0]['commit']['message'] if commits else 'No commits found'

        # Render the template with the extracted data
        return render_template('index.html', commit=message)
    
    except requests.RequestException as e:
        # Handle exceptions related to network or HTTP errors
        return f"An error occurred: {e}", 500

if __name__ == '__main__':
    app.run(debug=True)
