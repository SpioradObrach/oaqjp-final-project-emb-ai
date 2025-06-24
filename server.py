"""Flask server configuration script for the emotion detector setup.
"""
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def render_index_page():
    """Render the `index` page.
    """
    return render_template('index.html')

@app.route("/emotionDetector")
def query_emotion_detector() -> str:
    """Query the `emotion_detector` function from the `EmotionDetection` 
    module.

    Returns:
      infostr (str): String with the information returned by 
      `emotion_detector`.
    """
    text_to_analyze = request.args.get("textToAnalyze")
    output = emotion_detector(text_to_analyze)
    anger = output["anger"]
    disgust = output["disgust"]
    fear = output["fear"]
    joy = output["joy"]
    sadness = output["sadness"]
    dominant_emotion = output["dominant_emotion"]

    if dominant_emotion is None:
        infostr = "Invalid text! Please try again!"
        return infostr

    infostr = f"""For the given statement, the system response
    is 'anger': {anger}, 'disgust': {disgust}, 'fear': {fear},
    'joy': {joy} and 'sadness': {sadness}. The dominant emotion
    is {dominant_emotion}."""
    return infostr
    

if __name__ == '__main__':
    app.run()