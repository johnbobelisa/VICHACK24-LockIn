import os
from flask import Flask, render_template, request

app = Flask(__name__)

VIDEO_DIRECTORY = 'static/videos/'
ALLOWED_EXTENSIONS = ['mp4', 'webm', 'ogg']

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('index.html')


@app.route('/upload/')
def uploadclips():
    return render_template('upload.html')

@app.route('/clips/')
def clips():
    # List all video files in the directory
    videos = [f for f in os.listdir(VIDEO_DIRECTORY) if allowed_file(f)]
    return render_template('clips.html', videos=videos, video_dir=VIDEO_DIRECTORY)

@app.route('/upload', methods=['POST'])
def upload():
    if 'video' not in request.files:
        return 'No video file found'
    video = request.files['video']
    if video.filename == "":
        return 'No video file selected'
    if video and allowed_file(video.filename):
        video.save('static/videos/' + video.filename)
        return render_template('clips.html', video_name=video.filename)
    return 'invalid file type'


if __name__ == '__main__':
    app.run(debug=True)
