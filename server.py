from flask import Flask, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("\emotionDetector", methods=['GET'])
def emotion_detector():
    if "textToAnalyze" in request.args:
        textToAnalyze = request.args.get("textToAnalyze")
        output = emotion_detector(textToAnalyze)
        anger = output["anger"]
        disgust = output["disgust"]
        fear = output["fear"]
        joy = output["joy"]
        sadness = output["sadness"]
        dominant_emotion = output["dominant_emotion"]

        infostr = f"""For the given statement, the system response
        is 'anger': {anger}, 'disgust': {disgust}, 'fear': {fear},
        'joy': {joy} and 'sadness': {sadness}. The dominant emotion
        is {dominant_emotion}.
        """
        return infostr
    
    return "No correct input or error in code"