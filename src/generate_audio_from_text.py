import requests
import os
import json

elevenlabs_api_key = "sk_a0f542bc2eb34ce9ff31b8e0fc04eb5300559513d0c68d64"

def generate_audio_from_text(json_input:str):
    print("1")
    print(json_input)
    voice_id = "21m00Tcm4TlvDq8ikWAM"
    # Parse the JSON input
    data = json.loads(json_input)
    print("2")
    lecture_title = data['lecture_title']
    topics = data['topics']
    print("Im here")

    # Define the target directory for audio files
    audio_dir = os.path.join("data", "raw", "audios")
    os.makedirs(audio_dir, exist_ok=True)  # Create directory if it doesn't exist

    audio_paths = []  # List to store the paths of generated audio files

    # Iterate over each topic
    for i, topic in enumerate(topics, start=1):
        text = topic['script']

        # Use the lecture title and topic index for the audio file name
        audio_filename = f"{lecture_title.replace(' ', '_')}{i}.mp3"
        audio_path = os.path.join(audio_dir, audio_filename)

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
            "xi-api-key": elevenlabs_api_key,
            "Content-Type": "application/json"
        }

        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            with open(audio_path, "wb") as f:
                f.write(response.content)
            audio_paths.append(audio_path)  # Add the path to the list
            print(f"Audio generated for topic {i} at: {audio_path}")
        else:
            print(f"Failed to generate audio for topic {i} in lecture {lecture_title}: {response.text}")

    return audio_paths  # Return a list of all audio file paths