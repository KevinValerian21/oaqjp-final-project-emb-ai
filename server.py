"""
A Flask application for detecting emotions from text input.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector", methods=["GET"])
def sent_analyzer():
    """
    Analyze the emotional content of the provided text.

    Returns:
        A formatted response string containing emotion analysis results
        or an error message if the input is invalid.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    # Validate input
    if not text_to_analyze or text_to_analyze.strip() == "":
        return "Invalid text! Please try again!."

    # Analyze emotions
    response = emotion_detector(text_to_analyze)
    emotions = response
    dominant_emotion = emotions["dominant_emotion"]

    # Check response validity
    if dominant_emotion is None:
        return "Invalid text! Please try again!."
    # Format and return the response
    formatted_response = (
        f"For the given statement, the system response is "
        f"'anger': {emotions['anger']}, 'disgust': {emotions['disgust']}, "
        f"'fear': {emotions['fear']}, 'joy': {emotions['joy']}, and "
        f"'sadness': {emotions['sadness']}. "
        f"The dominant emotion is <b>{dominant_emotion}</b>."
    )
    return formatted_response

@app.route("/")
def render_index_page():
    """
    Render the index page for the web application.

    Returns:
        Rendered HTML content of the index page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
