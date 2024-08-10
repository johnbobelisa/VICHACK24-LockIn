import sys
import os

# Add the project root directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.generate_scenario import generate_scenario

# Example usage:
json_input = '''
{
  "lecture_title": "Introduction to Machine Learning",
  "topics": [
    {
      "topic": "Topic related to 00:00:05 - 00:00:30",
      "start_time": "00:00:05",
      "end_time": "00:00:30",
      "summary": "Welcome to the Introduction to Machine Learning lecture. Today we will cover several important topics including Linear Regression."
    },
    {
      "topic": "Topic related to 00:05:01 - 00:20:00",
      "start_time": "00:05:01",
      "end_time": "00:20:00",
      "summary": "Linear regression is a statistical method used to model the relationship between a dependent variable and one or more independent variables. The lecture covers the basic concepts, assumptions, and applications of linear regression in predictive analysis."
    }
  ]
}
'''

# Call the function
output = generate_scenario(json_input)
print(output)

"""
Resulting output:
{
  "lecture_title": "Introduction to Machine Learning",
  "script": "Hey there, welcome to the Introduction to Machine Learning lecture! Let's dive into Linear Regression - it's like predicting your crush's next move based on their previous behavior, but with numbers instead of emojis! In simple terms, linear regression helps us understand how the change in one variable affects another - just like how adding avocado makes everything better. Remember, assumptions in linear regression are like assuming 
your phone battery will last all day - sometimes it works, sometimes it's a flop! So, buckle up and get ready to unravel the mysteries of predicting the future with linear regression - it's like being a psychic"
}
"""