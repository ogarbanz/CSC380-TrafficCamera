import smtplib
import ssl


def send_email(user_email):
    port = 465
    smtp_server = "smtp.gmail.com"
    sender_email = "sunytrafficcamera@gmail.com"
    password = "OmarJonMichael380"
    message = "Subject: {}\n\n{}".format("Violation Report", "Test")

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, user_email, message)
        server.quit()
