#!/usr/bin/env python
# -*- coding: utf-8 -*-
from email.mime.text import MIMEText
import cgi
import smtplib
from time import gmtime, strftime
import json

SMTP_SERVER = "mail.example.com"
SMTP_PORT = 25

EMAIL_FROM = "no-reply@example.com"
EMAIL_BCC = "send-a-copy-here@example.com"
EMAIL_SUBJECT = "Solita Dojo registration received"

REGISTRATIONS_FILE = '/tmp/path-to-ilmo.txt'
REGISTRATIONS_LIMIT = 30

form = cgi.FieldStorage()
show_stats = form.getvalue('stats', '0') == '1'

print "Content-Type: text/plain;charset=utf-8\n"

if show_stats:
    with  open(REGISTRATIONS_FILE, 'r') as f:
        lines = f.readlines()
        print json.dumps({'registrations': len(lines), 'registrations_limit': REGISTRATIONS_LIMIT})

else:
    name = form.getvalue('name')
    company = form.getvalue('company')
    email = form.getvalue('email')
    allergies = form.getvalue('allergies')

    log_entry = strftime("%Y-%m-%d-%H-%M", gmtime()) + ";" + name + ";" + company + ";" + email + ";" + allergies + "\n"
    with open(REGISTRATIONS_FILE, 'a') as f:
        f.write(log_entry)

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

    print "Registration OK"
