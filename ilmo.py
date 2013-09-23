#!/usr/bin/env python
# -*- coding: utf-8 -*-
from email.mime.text import MIMEText
import cgi, cgitb, smtplib
from time import gmtime, strftime

SMTP_SERVER = "mail.example.com"
SMTP_PORT = 25

EMAIL_FROM = "no-reply@example.com"
EMAIL_BCC = "send-a-copy-here@example.com"
EMAIL_SUBJECT = "Solita Dojo registration received"

##Write form to file
form = cgi.FieldStorage()
name = form.getvalue('name')
company = form.getvalue('company')
email = form.getvalue('email')
allergies = form.getvalue('allergies')
data = strftime("%Y-%m-%d-%H-%M", gmtime()) + ";" + name + ";" + company + ";" + email + ";" + allergies + "\n"
f = open('/tmp/path-to-ilmo.txt','a')
f.write(data)
f.close()

msg = MIMEText("Name: " + name + "\n" +
    "Company: " + company + "\n" +
    "Email: " + email + "\n" +
    "Allergies: " + allergies + "\n" +
    "\n" +
    "Thank you for registration. See you soon!\n\n - Solita Developers")
msg['Subject'] = EMAIL_SUBJECT
msg['To'] = email
msg['From'] = EMAIL_FROM
msg.set_charset('utf-8')
mail = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
mail.sendmail(EMAIL_FROM, [email, EMAIL_BCC], msg.as_string())
mail.quit()

print "Content-Type: text/plain;charset=utf-8"
print
