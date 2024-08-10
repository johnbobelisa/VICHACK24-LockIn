import sys
import os

# Add the project root directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.generate_audio_from_text import generate_audio_from_text

# Example usage
json_input = """
{
  "lecture_title": "Introduction to Machine Learning",
  "topics": [
    {
      "topic": "Welcome to the Introduction to",
      "start_time": "00:00:05",
      "end_time": "00:00:30",
      "summary": "Welcome to the Introduction to Machine Learning lecture. Today we will cover several important topics including Linear Regression and Neural Networks.",
      "script": "Hey there, tech-savvy peeps! Welcome to the Introduction to Machine Learning lecture! Get ready to dive into the exciting world of data, algorithms, and some seriously cool stuff. Today's agenda? Linear Regression and Neural Networks, because who doesn't love a good brain workout, am I right?Now, Linear Regression might sound like a fancy term for lining up your ducks in a row, but trust me, it's all about predicting the future like a boss. And hey, if you've ever wondered how your favorite apps know exactly what you want, well,"
    },
    {
      "topic": "Linear regression is a statistical",
      "start_time": "00:05:01",
      "end_time": "00:20:00",
      "summary": "Linear regression is a statistical method used to model the relationship between a dependent variable and one or more independent variables. The lecture covers the basic concepts, assumptions, and applications of linear regression in predictive analysis.",
      "script": "Hey there, fellow data enthusiasts! Today, we're diving into the world of linear regression – a statistical superhero in the realm of predictive analysis.\\n\\nPicture this: linear regression is like trying to find the perfect match between a dependent variable and a bunch of independent variables. It's the ultimate matchmaker in the data world!\\n\\nNow, let's break it down in Gen-Z terms. Linear regression is basically the OG relationship status on social media – it's all about defining the connection between the main character (dependent variable) and its squad (independent variables).But wait, there's more! Linear"
    }
  ]
}
"""

audio_paths = generate_audio_from_text(json_input)
print(f"Audio generated at: {audio_paths}")