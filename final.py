from gtts import gTTS
from flask import send_file

@app.route('/speak_response', methods=['GET'])
def speak_response():
    tts = gTTS('Hello, this is a test response')
    tts.save('response.mp3')
    return send_file('response.mp3')
