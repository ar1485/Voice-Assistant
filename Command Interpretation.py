@app.route('/interpret_command', methods=['POST'])
def interpret_command():
    data = request.get_json()
    command = data.get('command')

    # Interpret the command and generate a response
    if "weather" in command:
        response = "It's sunny outside."
    elif "send email" in command:
        response = "Email sent successfully."
    else:
        response = "I'm sorry, I didn't understand that."

    # Use gTTS to convert the response to speech
    tts = gTTS(response)
    tts.save("response.mp3")
    
    return jsonify({"response": response})
