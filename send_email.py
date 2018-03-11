# import necessary packages

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

# create message object instance
msg = MIMEMultipart()

message = "Who might that be?"

# setup the parameters of the message
with open ("credential.txt", "r") as credentialFile:
    credentials = credentialFile.readlines()
    email = credentials[0].replace('\n', '')
    password = credentials[1].replace('\n', '')

msg['From'] = email
msg['To'] = email
msg['Subject'] = "Someone rings the doorbell"

# add in the message body
msg.attach(MIMEText(message, 'plain'))

#create server
server = smtplib.SMTP('smtp.gmail.com: 587')

server.starttls()

# Login Credentials for sending the mail
server.login(msg['From'], password)

# send the message via the server.
server.sendmail(msg['From'], msg['To'], msg.as_string())

server.quit()

print "successfully sent email to %s:" % (msg['To'])
