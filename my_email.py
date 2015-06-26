# -*- coding: utf-8 -*-
from email.mime.base import MIMEBase

import smtplib
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate


class MySender:
    def __init__(self, smtp_server, smtp_port, user, password):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.user = user
        self.password = password

    def __path_leaf(self, path):
        head, tail = ntpath.split(path)
        return tail or ntpath.basename(head)

    def send_mail(self, email):
        msg = MIMEMultipart('alternative')
        msg['From'] = email.sender
        msg['To'] = email.receivers
        msg['Date'] = formatdate(localtime=True)
        msg['Subject'] = email.subject
        msg.attach(MIMEText(email.body))

        part = MIMEBase('application', "octet-stream")
        part.set_payload(open(email.attachment, "rb").read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="{0}"'.format(self.__path_leaf(email.attachment)))
        msg.attach(part)

        try:
            print msg.as_string()
            smtp_obj = smtplib.SMTP_SSL(self.smtp_server, self.smtp_port)
            smtp_obj.ehlo()
            smtp_obj.login(self.user, self.password)
            smtp_obj.sendmail(email.sender, email.receivers, msg.as_string())
            smtp_obj.close()

            return True
        except smtplib.SMTPException:
            import traceback
            traceback.print_exc()

        return False


class MyEmail:
    def __init__(self, sender, receivers, subject, body):
        self.sender = sender
        self.receivers = receivers
        self.subject = subject
        self.body = body
        self.attachment = ""

    def set_attachment(self, attachment):
        self.attachment = attachment


import ntpath


