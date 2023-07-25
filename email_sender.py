from email.message import EmailMessage
from private import email_app_password
import ssl
import smtplib

email_sender = 'dominic.caggese@gmail.com'
email_password = email_app_password

email_receiver = 'dcaggese@live.com'

subject = 'Automated Test'

body = 'This is a automated email sent with python!'

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())