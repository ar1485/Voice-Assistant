import speech_recognition as sr
from flask import Flask, request, jsonify
from gtts import gTTS
import os

app = Flask(__name__)

@app.route('/process_voice', methods=['POST'])
def process_voice():
    if 'audio' not in request.files:
        return jsonify({"error": "No audio file found"}), 400
    
    audio_file = request.files['audio']
    recognizer = sr.Recognizer()

    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)
        
        try:
            # Use Google's speech recognition
            text = recognizer.recognize_google(audio)
            return jsonify({"command": text})
        except sr.UnknownValueError:
            return jsonify({"error": "Speech not recognized"}), 400

if __name__ == '__main__':
    app.run(debug=True)
