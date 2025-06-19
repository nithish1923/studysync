
import smtplib
from email.mime.text import MIMEText
import streamlit as st

def send_email(to_address, subject, body):
    from_address = st.secrets["email"]["sender"]
    password = st.secrets["email"]["password"]

    msg = MIMEText(body, "plain")
    msg["Subject"] = subject
    msg["From"] = from_address
    msg["To"] = to_address

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(from_address, password)
            server.send_message(msg)
            return True
    except Exception as e:
        print("Error sending email:", e)
        return False
