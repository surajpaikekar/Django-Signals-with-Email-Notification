# email_helper.py
from django.core.mail import EmailMessage, get_connection
from django.conf import settings

def send_email(subject, message, to_email):
    try:
        email = EmailMessage(subject, message, to=[to_email])
        email.send()
    except Exception as e:
        print(f"failed to send email because of {e}")
