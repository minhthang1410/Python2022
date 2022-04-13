import email
from http import server
import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase

server = smtplib.SMTP('smtp.gmail.com', 25)

server.ehlo()

with open('password.txt', 'r') as f:
    password = f.read()
    
server.login('kingslayer14101998@gmail.com', password)

print(password)