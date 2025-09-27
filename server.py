"""
Emotion Detection Web Application
This Flask app provides a web interface and an API endpoint to analyze emotions
from user-submitted text using IBM Watson NLP Emotion Detection service.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Initialize Flask application
app = Flask('Emotion Detection')

@app.route('/emotionDetector')
def sent_detector():
    """
    API endpoint to detect emotions from a given text.
    Retrieves the 'textToAnalyze' query parameter, sends it to the emotion_detector,
    and returns a formatted string of emotion scores and the dominant emotion.
    If the input is invalid or blank, returns an error message.
    """

    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    formatted_response = (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )

    return formatted_response

@app.route('/')
def render_index_page():
    """
    Renders the homepage of the Emotion Detection web application.
    """

    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
