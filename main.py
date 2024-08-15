import sys
import requests
import ast
import smtplib
import os
from dotenv import load_dotenv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from prepare_html import newsletter_html


load_dotenv()

def send_email(data, n):
    port = 587
    smtp_server = "smtp.gmail.com"
    password = os.getenv("MY_PASSWORD")

    sender_email = os.getenv("MY_EMAIL")
    receiver_email = os.getenv("MY_RECEIVING_EMAIL")

    # Email content
    subject = "HTML Email without Attachment"
    html = newsletter_html(data, n)

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    message.attach(MIMEText(html, "html"))

    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())








def main():
    raw_data = requests.get("https://hacker-news.firebaseio.com/v0/topstories.json").content
    decoded_data = raw_data.decode("utf-8")

    # convert the string to a Python list 
    # length of 500
    data = ast.literal_eval(decoded_data)
    n = int(sys.argv[1])
    send_email(data, n)
    print("Sent")



if __name__ == "__main__":
    main()