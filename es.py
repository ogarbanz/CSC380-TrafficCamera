import os
from datetime import date
from datetime import datetime
import smtplib, ssl
import re
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage


regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'

def check(email):
    if re.search(regex, email):
        return True
    else:
        return False


def send_email(receiver_email, measured_speed, location, frame):
    global user_email
    port = 465
    smtp_server = "smtp.gmail.com"
    sender_email = "sunytrafficcamera@gmail.com"
    password = "OmarJonMichael380"
    time = str(datetime.time(datetime.now()).hour) + ":" + str(datetime.time(datetime.now()).minute)

    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Speed Infraction"
    msg['From'] = "SUNY Traffic Camera"
    msg['To'] = "you"
    img_data = open(frame, 'rb').read()
    html = f"""\
    <html>
    <center>
        <h1><b>SPEED LIMIT EXCEEDED</b></h1>
        <body>
            <p>
            TIME OF INFRACTION: <b>{time}</b> <br> <br>
            LOCATION OF INFRACTION: <b>{location}</b> <br> <br>
            SPEED OF VEHICLE: <b>{measured_speed}</b>
            </p>
        </body>
    </center>
    </html>"""

    message = MIMEText(html, 'html')
    msg.attach(message)
    image = MIMEImage(img_data, name=os.path.basename(frame))
    msg.attach(image)

    if check(receiver_email):
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
            server.quit()
        return True
    else:
        print("Invalid Email")
        return False
