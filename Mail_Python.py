import smtplib
import datetime

gmail_user = 'Sender@gmail.com'
gmail_password = 'SenderPassword'

Machine_ID = 10256

currentTime = datetime.datetime.now()

Message = "Machine Started " + str(currentTime)

sent_from = gmail_user
to = ['Receiver@gmail.com']
subject = Machine_ID

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (gmail_user, ", ".join(to), subject, Message)

try:
    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_server.ehlo()
    smtp_server.login(gmail_user, gmail_password)
    smtp_server.sendmail(gmail_user, to, email_text)
    smtp_server.close()
    print ("Email sent successfully!")
except Exception as ex:
    print ("Something went wrong….",ex)
