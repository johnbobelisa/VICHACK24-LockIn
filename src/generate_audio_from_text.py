import requests
import os
import json

elevenlabs_api_key = "ELEVENLABS_OPENAPI_KEY"

def generate_audio_from_text(json_input):
    voice_id="21m00Tcm4TlvDq8ikWAM"
    # Parse the JSON input
    data = json.loads(json_input)
    lecture_title = data['lecture_title']
    text = data['script']

    # Use the lecture title for the audio file name, replacing spaces with underscores
    audio_filename = lecture_title.replace(" ", "_")

    # URL and payload configuration for Eleven Labs API
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
    payload = {
        "model_id": "eleven_multilingual_v2",
        "voice": "Bella",
        "text": text,
        "voice_settings": {
            "similarity_boost": 0.5,
            "stability": 0.5,
        }
    }
    headers = {
        "xi-api-key": f"{elevenlabs_api_key}",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        # Define the target directory for audio files
        audio_dir = os.path.join("data", "raw", "audios")
        audio_path = os.path.join(audio_dir, f"{audio_filename}.mp3")
        with open(audio_path, "wb") as f:
            f.write(response.content)
        return audio_path
    else:
        print(f"Failed to generate audio for lecture {lecture_title}: {response.text}")
        return None
