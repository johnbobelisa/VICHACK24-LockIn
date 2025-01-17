import sys
import os

# Add the project root directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.summarize_transcript import summarize

# Example usage:
json_input = '''
{
  "lecture_title": "Introduction to Machine Learning",
  "topics": [
    {
      "topic": "Welcome to the Introduction to",
      "start_time": "00:00:05",
      "end_time": "00:00:30",
      "summary": "Welcome to the Introduction to Machine Learning lecture. Today we will cover several important topics including Linear Regression and Neural Networks."
    },
    {
      "topic": "Linear regression is a statistical",
      "start_time": "00:05:01",
      "end_time": "00:20:00",
      "summary": "Linear regression is a statistical method used to model the relationship between a dependent variable and one or more independent variables. The lecture covers the basic concepts, assumptions, and applications of linear regression in predictive analysis."
    }
  ]
}
'''

# Call the function
summarized_output = summarize(json_input)
print(summarized_output)

"Resulting Output:"
"""
{
  "lecture_title": "Introduction to Machine Learning",
  "topics": [
    {
      "topic": "Welcome to the Introduction to",
      "start_time": "00:00:05",
      "end_time": "00:00:30",
      "summary": "Welcome to the Introduction to Machine Learning lecture. Today we will cover several important topics including Linear Regression and Neural Networks."
    },
    {
      "topic": "Linear regression is a statistical",
      "start_time": "00:05:01",
      "end_time": "00:20:00",
      "summary": "Linear regression is a statistical method used to model the relationship between a dependent variable and one or more independent variables. The lecture covers the basic concepts, assumptions, and applications of linear regression in predictive analysis."
    }
  ]
}

"""