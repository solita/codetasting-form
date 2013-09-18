#!/usr/bin/env python
# -*- coding: utf-8 -*-
from email.mime.text import MIMEText
import cgi, cgitb, smtplib
from time import gmtime, strftime

SMTP_SERVER = "mail-host-here"
SMTP_PORT = 587

EMAIL_FROM = "no-reply@solita.fi"
EMAIL_SUBJECT = "Solita Dojo registration received"

##Write form to file
form = cgi.FieldStorage()
name = form.getvalue('name')
company = form.getvalue('company')
email = form.getvalue('email')
allergies = form.getvalue('allergies')
data = strftime("%Y-%m-%d-%H-%M", gmtime()) + ";" + name + ";" + company + ";" + email + ";" + allergies + "\n"
f = open('~/ilmot.txt','a')
f.write(data)
f.close()

msg = MIMEText("Name: " + name + "\n" +
    "Company: " + company + "\n" +
    "Email: " + email + "\n" +
    "Allergies " + allergies + "\n" +
    "\n" +
    "See you soon!\n\n - Solita Developers")
msg['Subject'] = EMAIL_SUBJECT
msg['To'] = email
msg['From'] = EMAIL_FROM
msg.set_charset('utf-8')
mail = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
mail.sendmail(EMAIL_FROM, email, msg.as_string())
mail.quit()
