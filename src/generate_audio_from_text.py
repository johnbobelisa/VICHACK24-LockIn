import requests
import os
elevenlabs_api_key = os.getenv("ELVEN_LABS_API_KEY3")
def generate_audio_from_text(text, scene_id, voice_id="21m00Tcm4TlvDq8ikWAM"):
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
        # Save audio in "audio" directory
        audio_path = os.path.join("audio", f"scene_{scene_id}.mp3")
        with open(audio_path, "wb") as f:
            f.write(response.content)
        return audio_path
    else:
        print(f"Failed to generate audio for scene {scene_id}: {response.text}")
        return None