"""

Een Flask-server voor het analyseren van emoties in tekst.
De server biedt twee routes:
1. "/" voor het weergeven van de indexpagina.
2. "/emotionDetector" voor het analyseren van emoties in een opgegeven tekst.

"""
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def render_index_page():
    """
    Endpoint voor de root-route '/'.

    Laadt en retourneert de indexpagina (index.html) die de gebruiker kan gebruiken voor emotie-analyse.

    Returns:
        str: HTML-pagina via Flask's render_template functie.
    """
    return render_template('index.html')

@app.route("/emotionDetector")
def emotion_detector_endpoint():
    """
    Endpoint voor het analyseren van emoties in een gegeven tekst.

    Query Parameters:
        textToAnalyze (str): De tekst die geanalyseerd moet worden.

    Returns:
        str: Een leesbare boodschap met de emotie scores of een foutmelding als de tekst leeg is.
    """

    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if response.get('dominant_emotion') is None:
        return "Invalid text! Please try again!"

    result_text = (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

    return result_text

if __name__ == "__main__":
    app.run(host="localhost", port=5000)
