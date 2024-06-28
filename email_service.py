import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

APP_PASSWORD="bopz vpqr dpoc wbbq"
SENDER_EMAIL="grzegorzklimek77@gmail.com"


def send_email(recipient_email, subject, message_str):
    message = MIMEMultipart()
    message["From"] = SENDER_EMAIL
    message["To"] = recipient_email
    message["Subject"] = subject
    message.attach(MIMEText(message_str, "plain", "utf-8"))
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(SENDER_EMAIL, APP_PASSWORD)
        server.sendmail(SENDER_EMAIL, recipient_email, message.as_string())
        print(f"Email to {recipient_email} sent successfully")
