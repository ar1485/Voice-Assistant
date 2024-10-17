from models import db, Commands

@app.route('/store_command', methods=['POST'])
def store_command():
    data = request.get_json()
    user_id = data.get('user_id')
    command = data.get('command')
    response = data.get('response')

    # Store the command in the database
    new_command = Commands(user_id=user_id, command=command, response=response)
    db.session.add(new_command)
    db.session.commit()

    return jsonify({"status": "success"})
