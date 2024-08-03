from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from models import db, Email
import utils

app = Flask(__name__)
app.config.from_object('config.Config')
db.init_app(app)

@app.route('/save_emails', methods=['POST'])
def save_emails():
    data = request.json
    try:
        email = Email(
            event_id=data['event_id'],
            email_subject=data['email_subject'],
            email_content=data['email_content'],
            timestamp=datetime.strptime(data['timestamp'], "%d %b %Y %H:%M")
        )
        db.session.add(email)
        db.session.commit()
        return jsonify({"message": "Email saved successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/get_emails', methods=['GET'])
def get_emails():
    event_id = request.args.get('event_id')
    query = Email.query
    if event_id:
        query = query.filter_by(event_id=event_id)
    emails = query.all()
    email_list = []
    for email in emails:
        email_data = {
            'event_id': email.event_id,
            'email_subject': email.email_subject,
            'email_content': email.email_content,
            'timestamp': email.timestamp.strftime("%d %b %Y %H:%M")
        }
        email_list.append(email_data)
    return jsonify(email_list), 200

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple('localhost', 5000, app)


