import smtplib
import ssl
from email.message import EmailMessage

subject = "Mail od firmy"
body = "Podaj swoje hasło do konta bankowego"
sender_email = "bussinespythonfreelancer@gmail.com"
password = input('Podaj hasło: ')

context = ssl.create_default_context()

print('Wysyłanie maila: ')

with open('mailer/maile.txt', 'r', encoding="UTF-8") as f:
    plik = f.readlines()

    for i in range(1):
        for receiver_email in plik:
            message = EmailMessage()
            message["From"] = sender_email
            message["To"] = receiver_email.strip()
            message['Subject'] = subject
            message.set_content(body)

            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, message.as_string())
        
    print('Success')