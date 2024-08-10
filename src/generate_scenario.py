import requests
import json
from dotenv import load_dotenv
import os
from summarize_transcript import summarize
from openai import OpenAI
from datetime import datetime

# Load environment variables
load_dotenv()

# Get API keys from environment variables
openai_api_key = os.getenv("OPEN_API_KEY")
elevenlabs_api_key = os.getenv("ELVEN_LABS_API_KEY3")

# Function to create a unique filename based on the current timestamp
def create_unique_filename(base_path, filename):
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")  # Generates a timestamp
    unique_filename = f"{filename}_{timestamp}.mp3"  # Appends timestamp to the filename
    return os.path.join(base_path, unique_filename)

# Function to generate scenarios using OpenAI API
def generate_scenario(transcript):
    summary = summarize(transcript)
    print("Transcript Summary:")
    print(summary)

    word_limit = 120

    client = OpenAI(api_key=openai_api_key)

    tools = [
        {
            "name": "get_scenes",
            "description": "Get the scenes for an audio script without scene descriptions",
            "parameters": {
                "type": "object",
                "properties": {
                    "scenes": {
                        "type": "array",
                        "description": "The scenes for the audio script",
                        "items": {
                            "type": "object",
                            "properties": {
                                "id": {"type": "integer"},
                                "script": {"type": "string", "description": "The script for the scene. MUST include only the text that will be spoken by the narrator"},
                            },
                        },
                    },
                },
            },
        }
    ]

    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are an educational influencer and lecturer. Please frequently use Gen-Z slang."
                        "Your goal is to ensure that your viewers thoroughly understand the given topic. "
                        "Provide clear explanations and use simple examples to illustrate complex ideas. "
                        "Engage the audience by explaining concepts in an easily digestible manner, "
                        "focusing on clarity and understanding. Limit the script to no more than "
                        f"{word_limit} words to ensure it fits within a 1-minute audio duration."
                    )
                },
                {"role": "user", "content": f"Transcript Summary: {summary}"},
            ],
            functions=tools,
            function_call={
                "name": "get_scenes",
            },
        )
        # Loading the response as a JSON object
        json_response = json.loads(response.choices[0].message.function_call.arguments)

        # Ensure each scene script is within the word limit
        for scene in json_response['scenes']:
            scene_script = scene['script']
            words = scene_script.split()
            if len(words) > word_limit:
                scene['script'] = ' '.join(words[:word_limit])
        
        return response.choices[0].message.function_call.arguments
    except Exception as e:
        print(e)
        return None

