YOUR_API_KEY = '094894ef-ddfd-43fd-bcec-c69f098387c2'
from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# Replace 'YOUR_API_KEY' with your actual FutDB API key
FUTDB_API_KEY = 'YOUR_API_KEY'
FUTDB_API_URL = 'https://futdb.app/api'

# Function to get player data from FutDB API
def get_player_data(player_id):
    headers = {
        'X-AUTH-TOKEN': FUTDB_API_KEY
    }
    response = requests.get(f'{FUTDB_API_URL}/players/{player_id}', headers=headers)
    return response.json()

@app.route('/')
def home():
    return 'Welcome to the FutDB API Flask App!'

@app.route('/player/<int:player_id>', methods=['GET'])
def player(player_id):
    data = get_player_data(player_id)
    if 'error' in data:
        return jsonify({'error': 'Player not found'}), 404
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
