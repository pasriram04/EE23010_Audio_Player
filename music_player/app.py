from flask import Flask, render_template, request, jsonify, send_file
import os
import random

app = Flask(__name__)

# Replace with your songs folder path
songs_folder = "/sdcard/Documents/EE23010/music_player/music_files/"
songs = [f for f in os.listdir(songs_folder) if f.endswith('.mp3')]

# Initialize the shuffled songs
shuffled_songs = random.sample(songs, len(songs))

# Store the current playing song index
current_song_index = -1

@app.route('/')
def index():
    return render_template('index.html', songs=shuffled_songs)

@app.route('/play', methods=['GET', 'POST'])  # Allow both GET and POST
def play():
    global current_song_index

    if request.method == 'GET':
        song_index = int(request.args.get('song_index'))
        current_song_index = song_index  # Store the current song index
        song_path = os.path.join(songs_folder, shuffled_songs[song_index])
        return send_file(song_path, as_attachment=True)

    if request.method == 'POST':
        if current_song_index != -1:
            current_song_index = -1
            audioPlayer.pause()  # Pause the currently playing song

@app.route('/control', methods=['POST'])
def control():
    action = request.form['action']

    if action == 'pause':
        current_song_index = -1
        return jsonify({'action': 'pause'})
    elif action == 'next':
        current_song_index = -1
        return jsonify({'action': 'next'})

@app.route('/shuffle', methods=['POST'])
def shuffle_songs():
    global shuffled_songs
    random.shuffle(shuffled_songs)  # Shuffle the songs list
    return jsonify({'action': 'shuffle'})

if __name__ == '__main__':
    app.run(debug=True)
