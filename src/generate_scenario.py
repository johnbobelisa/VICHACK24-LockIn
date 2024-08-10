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

    word_limit = 120  # Set a word limit for each topic's script

    # Create the OpenAI client
    client = OpenAI(api_key=openai_api_key)

    # Process each topic individually
    for topic in topics:
        topic_title = topic['topic']
        topic_summary = topic['summary']

        try:
            # Generate script for each topic
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"Create a 60-second script for a narrator based on the topic '{topic_title}' and its summary: {topic_summary}. Please include some Gen-Z jokes to make it engaging. The script must only contain the text for the narrator to speak, without any background instructions, music cues, or scene descriptions. Focus solely on the CONTENT and what the narrator will say to the audience. NO special characters other than conversation symbols like '?, !, ., etc.'"}
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

            # Add the script to the topic
            topic['script'] = script

        except Exception as e:
            print(f"Error generating script for topic '{topic_title}':", e)
            topic['script'] = "Error generating script."

    # Create the output JSON structure
    output_json = {
        "lecture_title": lecture_title,
        "topics": topics
    }

    return json.dumps(output_json, indent=2)
