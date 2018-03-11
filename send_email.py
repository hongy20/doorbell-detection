# send_attachment.py
# import necessary packages
from email.mime.multipart import MIMEMultipart
from email.MIMEImage import MIMEImage
from email.mime.text import MIMEText
import smtplib
import glob
import os

def send():
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

    # find the latest image in folder images
    list_of_files = glob.glob('images/*.jpg') # * means all if need specific format then *.csv
    latest_file = max(list_of_files, key=os.path.getctime)
    print 'Image "%s" will be attached.' % latest_file

    # attach image to message body
    msg.attach(MIMEImage(file(latest_file).read()))

    #create server
    server = smtplib.SMTP('smtp.gmail.com: 587')

    server.starttls()

    # Login Credentials for sending the mail
    server.login(msg['From'], password)

    # send the message via the server.
    server.sendmail(msg['From'], msg['To'], msg.as_string())

    server.quit()

    print "successfully sent email to %s:" % (msg['To'])
