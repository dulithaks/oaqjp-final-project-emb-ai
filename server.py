"""
Server
"""
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    """
    index
    """
    return render_template("index.html")

@app.route('/emotionDetector')
def get_emotion_by_text():
    """
    get emotion by text
    """
    text_to_analyze = request.args.get('textToAnalyze')
    res = emotion_detector(text_to_analyze)

    if res["dominant_emotion"] is None:
        return {"message": "Invalid text! Please try again!"}

    return res

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
