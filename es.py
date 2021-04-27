from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from datetime import datetime
from email import encoders
import smtplib
import ssl
import os


def send_email(receiver_email, measured_speed, location, img_filename, vid_filename):
    port = 465
    smtp_server = "smtp.gmail.com"
    sender_email = "sunytrafficcamera@gmail.com"
    password = "OmarJonMichael380"
    time = str(datetime.now().strftime("%H:%M"))

    msg = MIMEMultipart('mixed')
    msg['Subject'] = "Speed Infraction"
    msg['From'] = "SUNY Traffic Camera"
    msg['To'] = receiver_email
    vid_data = MIMEBase('application', 'octet-stream')
    vid_data.set_payload(open(vid_filename, 'rb').read())
    encoders.encode_base64(vid_data)
    vid_data.add_header('Content-Disposition', 'attachment', filename=vid_filename)
    img_data = open(img_filename, 'rb').read()
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
    msg.attach(MIMEImage(img_data, name=os.path.basename(img_filename)))
    msg.attach(vid_data)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        try:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
            os.remove(img_filename)
            os.remove(vid_filename)
        except smtplib.SMTPException:
            return
        finally:
            server.quit()
