import os
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_mail(grade, out_of, subject):

    text = "Bonjour Darlann, Une nouvelle note est arrivée sur Pronote."
    with open('mail-note.html', 'r') as file:
        html = file.read()
    html = html.replace('VAR_SUBJECT', subject)
    html = html.replace('VAR_GRADE', grade)
    html = html.replace('VAR_OUTOF', out_of)
    html = html.replace('VAR_FIRSTNAME', os.environ['firstname'])

    # Record the MIME types of both parts - text/plain and text/html.

    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls
    sender_email = "didoub74.fr@gmail.com"
    receiver_email = "darlann@banache.fr"
    password = "vqpilgmhfzxuwjog"
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Nouvelle note pronote"
    msg['From'] = sender_email
    msg['To'] = receiver_email
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')
    msg.attach(part1)
    msg.attach(part2)
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:

        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        print('Mail sended !')
