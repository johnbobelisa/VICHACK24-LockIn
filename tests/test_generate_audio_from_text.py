import sys
import os

# Add the project root directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.generate_audio_from_text import generate_audio_from_text

# Example usage
json_input = """
{
  "lecture_title": "Introduction to Machine Learning",
  "script": "Hey there, welcome to the Introduction to Machine Learning lecture! Let's dive into Linear Regression - it's like predicting your crush's next move based on their previous behavior, but with numbers instead of emojis! In simple terms, linear regression helps us understand how the change in one variable affects another - just like how adding avocado makes everything better. Remember, assumptions in linear regression are like assuming your phone battery will last all day - sometimes it works, sometimes it's a flop! So, buckle up and get ready to unravel the mysteries of predicting the future with linear regression - it's like being a psychic."
}
"""

audio_path = generate_audio_from_text(json_input)
print(f"Audio generated at: {audio_path}")
