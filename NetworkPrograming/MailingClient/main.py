from cgitb import text
import email
from email.mime.multipart import MIMEMultipart
from http import server
import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase

server = smtplib.SMTP('smtp.gmail.com',465)

with open('password.txt', 'r') as f:
    password = f.read()

server.starttls()
server.login('kingslayer14101998@gmail.com', password)

msg = MIMEMultipart()
msg['From'] = 'kingslayer14101998'
msg['minhthang14101998@gmail.com']
msg['Subject'] = 'Test Mailing client'

with open('message.txt', 'r') as f:
    message = f.read()
    
msg.attach(MIMEText(message, 'plain'))

filename = 'avatar.jpg'
attachment = open(filename, 'rb')

p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header('Content-Disposition', f'attachment; filename={filename}')
msg.attach(p)

text = msg.as_string()
server.sendmail('kingslayer14101998@gmail.com', 'minhthang14101998@gmail.com', text)