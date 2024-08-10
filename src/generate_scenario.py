import json
from dotenv import load_dotenv
import os
from openai import OpenAI

# Load environment variables
load_dotenv()

# Get API keys from environment variables
openai_api_key = os.getenv("OPEN_API_KEY")

# Function to generate scenarios using OpenAI API
def generate_scenario(json_input: str):
    data = json.loads(json_input)
    lecture_title = data['lecture_title']
    topics = data['topics']

    # Summarize each topic and combine into a single script
    combined_summary = " ".join([topic['summary'] for topic in topics])
    print("Combined Summary:")
    print(combined_summary)

    word_limit = 120

    # Create the OpenAI client
    client = OpenAI(api_key=openai_api_key)

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"Lecture on {lecture_title}. {combined_summary} Limit the script to no more than {word_limit} words. Please frequently link/add your teaching with funny Gen-Z jokes."}
            ],
            max_tokens=word_limit,
            temperature=0.5,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )

        script = response.choices[0].message.content.strip()

        # Ensure the generated script is within the word limit
        words = script.split()
        if len(words) > word_limit:
            script = ' '.join(words[:word_limit])

        output_json = {
            "lecture_title": lecture_title,
            "script": script
        }

        return json.dumps(output_json, indent=2)

    except Exception as e:
        print(e)
        return None
