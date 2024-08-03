from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Email(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, nullable=False)
    email_subject = db.Column(db.String, nullable=False)
    email_content = db.Column(db.String, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f'<Email {self.email_subject}>'
