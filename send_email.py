import smtplib
import os
from dotenv import load_dotenv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

load_dotenv()

port = 587
smtp_server = "smtp.gmail.com"
password = os.getenv("MY_PASSWORD")

sender_email = os.getenv("MY_EMAIL")
receiver_email = os.getenv("MY_RECEIVING_EMAIL")

# Email content
subject = "HTML Email without Attachment"
with open('main_template.html', 'r') as file:
    html = file.read()

message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject

message.attach(MIMEText(html, "html"))

with smtplib.SMTP(smtp_server, port) as server:
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())

print('Sent')