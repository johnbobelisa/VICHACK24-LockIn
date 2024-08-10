from src.generate_scenario import generate_scenario, create_unique_filename
from src.generate_audio_from_text import generate_audio_from_text
from moviepy.editor import AudioFileClip, concatenate_audioclips
import os
import json

# Sample transcript text
transcript = """
    Simple Linear Regression | An Easy Introduction & Examples
    Published on February 19, 2020 by Rebecca Bevans. Revised on June 22, 2023.

    Simple linear regression is used to estimate the relationship between two quantitative variables. You can use simple linear regression when you want to know:

    How strong the relationship is between two variables (e.g., the relationship between rainfall and soil erosion).
    The value of the dependent variable at a certain value of the independent variable (e.g., the amount of soil erosion at a certain level of rainfall).
    Regression models describe the relationship between variables by fitting a line to the observed data. Linear regression models use a straight line, while logistic and nonlinear regression models use a curved line. Regression allows you to estimate how a dependent variable changes as the independent variable(s) change.

    Simple linear regression example
    You are a social researcher interested in the relationship between income and happiness. You survey 500 people whose incomes range from 15k to 75k and ask them to rank their happiness on a scale from 1 to 10.
    Your independent variable (income) and dependent variable (happiness) are both quantitative, so you can do a regression analysis to see if there is a linear relationship between them.

    If you have more than one independent variable, use multiple linear regression instead.

    Table of contents
    Assumptions of simple linear regression
    How to perform a simple linear regression
    Interpreting the results
    Presenting the results
    Can you predict values outside the range of your data?
    Other interesting articles
    Frequently asked questions about simple linear regression
    Assumptions of simple linear regression
    Simple linear regression is a parametric test, meaning that it makes certain assumptions about the data. These assumptions are:

    Homogeneity of variance (homoscedasticity): the sizfe of the error in our prediction doesn’t change significantly across the values of the independent variable.
    Independence of observations: the observations in the dataset were collected using statistically valid sampling methods, and there are no hidden relationships among observations.
    Normality: The data follows a normal distribution.
    Linear regression makes one additional assumption:

    The relationship between the independent and dependent variable is linear: the line of best fit through the data points is a straight line (rather than a curve or some sort of grouping factor).
    If your data do not meet the assumptions of homoscedasticity or normality, you may be able to use a nonparametric test instead, such as the Spearman rank test.

    Example: Data that doesn’t meet the assumptions
    You think there is a linear relationship between cured meat consumption and the incidence of colorectal cancer in the U.S. However, you find that much more data has been collected at high rates of meat consumption than at low rates of meat consumption, with the result that there is much more variation in the estimate of cancer rates at the low range than at the high range. Because the data violate the assumption of homoscedasticity, it doesn’t work for regression, but you perform a Spearman rank test instead.
    If your data violate the assumption of independence of observations (e.g., if observations are repeated over time), you may be able to perform a linear mixed-effects model that accounts for the additional structure in the data.
"""

response = generate_scenario(transcript)
if response:
    json_response = json.loads(response)
    audio_paths = []
    for scene in json_response['scenes']:
        audio_path = generate_audio_from_text(scene['script'], scene['id'])
        if audio_path:
            audio_paths.append(audio_path)
            print(f"Generated audio for scene {scene['id']}")
        else:
            print(f"Failed to generate audio for scene {scene['id']}")

    # Concatenate all the audio clips
    if audio_paths:
        audio_clips = [AudioFileClip(path) for path in audio_paths]
        final_audio = concatenate_audioclips(audio_clips)

        # Creating a unique filename for the final audio file
        final_audio_path = create_unique_filename("audio", "final_audio")   
        final_audio.write_audiofile(final_audio_path)
        print(f"Final audio created: {final_audio_path}")

        # Remove individual scene files
        for path in audio_paths:
            os.remove(path)
            print(f"Removed {path}")
else:
    print("Failed to generate scenario")
