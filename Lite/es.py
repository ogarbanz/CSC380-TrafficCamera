from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from datetime import datetime
import smtplib
import ssl
import os


def send_email(receiver_email, measured_speed, location, img1_filename, img2_filename):
    port = 465
    smtp_server = "smtp.gmail.com"
    sender_email = "sunytrafficcamera@gmail.com"
    password = "OmarJonMichael380"
    time = str(datetime.now().strftime("%H:%M"))

    msg = MIMEMultipart('mixed')
    msg['Subject'] = "Speed Infraction"
    msg['From'] = "SUNY Traffic Camera"
    msg['To'] = receiver_email
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

    msg.attach(MIMEText(html, 'html'))
    msg.attach(MIMEImage(open(img1_filename, 'rb').read(), name=os.path.basename(img1_filename)))
    msg.attach(MIMEImage(open(img2_filename, 'rb').read(), name=os.path.basename(img2_filename)))

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        try:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
            os.remove(img1_filename)
            os.remove(img2_filename)
        except smtplib.SMTPException:
            return
        finally:
            server.quit()
