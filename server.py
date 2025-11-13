from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/emotionDetector')
def get_emotion_by_text():
    text_to_analyze = request.args.get('textToAnalyze')
    return emotion_detector(text_to_analyze)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)