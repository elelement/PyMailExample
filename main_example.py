#!/usr/bin/env python
# -*- coding: utf-8 -*-
sender = MySender("smtp.gmail.com", 465, "<your_gmail_user>", "<your_password>")

# Send only if the scan path exists
file_path = "<path_to_the_file_you_want_to_send>"
if os.path.exists(file_path):
  email.set_attachment(file_path)
  print """File %s attached""" % file_path
else:
  print 'Attachment file not found'
  
# Send the email
main_instance.send_email(sender, email)
