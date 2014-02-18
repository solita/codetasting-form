#!/usr/bin/env python
# -*- coding: utf-8 -*-
from email.mime.text import MIMEText
import cgi
import smtplib
from time import gmtime, strftime
import json
import textwrap

SMTP_SERVER = "mail1.sigmatic.fi"
SMTP_PORT = 587

EMAIL_FROM = "dojo@solita.fi"
EMAIL_BCC = EMAIL_FROM
EMAIL_SUBJECT = "Developer Garage registration received"

REGISTRATIONS_FILE = '/home/ilmo/dojo-ilmo.txt'
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

    msg = MIMEText(textwrap.dedent(
        """
        You have registered to Developer Garage which is to be held on Wednesday 5.3.2014 17:00
        at Solita's office in Arkadiankatu 2, Helsinki.

        If you want to change something regarding your registration, for example if you cannot make it,
        please contact {EMAIL_BCC}

        Name: {name}
        Company: {company}
        Email: {email}
        Allergies: {allergies}

        See you soon!

        - Solita Developers
        http://dev.solita.fi
        """.format(**locals())).strip())
    msg['Subject'] = EMAIL_SUBJECT
    msg['To'] = email
    msg['From'] = EMAIL_FROM
    msg.set_charset('utf-8')
    mail = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    mail.sendmail(EMAIL_FROM, [email, EMAIL_BCC], msg.as_string())
    mail.quit()

    print "Registration OK"
