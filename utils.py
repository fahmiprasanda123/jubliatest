from models import db, Email
from datetime import datetime
import time

def send_emails():
    while True:
        now = datetime.utcnow()
        emails = Email.query.filter(Email.timestamp <= now).all()
        for email in emails:
            # Logic to send email
            print(f'Sending email: {email.email_subject}')
            db.session.delete(email)
            db.session.commit()
        time.sleep(60)
