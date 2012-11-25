#!/usr/bin/env python
# -*- coding: utf-8 -*-
from email.mime.text import MIMEText
import cgi, cgitb, smtplib
from time import gmtime, strftime

SMTP_SERVER = "mail-host-here"
SMTP_PORT = 587

EMAIL_FROM = "no-reply@solita.fi"
EMAIL_SUBJECT = "Solita Code Tasting ilmoittautuminen vastaanotettu"
EMAIL_SPACE = ", "

##Write form to file
form = cgi.FieldStorage()
name = form.getvalue('name')
email = form.getvalue('email')
phone = form.getvalue('phone')
background = form.getvalue('background')
objectives = form.getvalue('objectives')
allergies = form.getvalue('allergies')
data = strftime("%Y-%m-%d-%H-%M", gmtime()) + ";" + name + ";" + email + ";" + phone + ";"  + background + ";" + objectives + ";" + allergies + "\n"
f = open('~/ilmot.txt','a')
f.write(data)
f.close()

msg = MIMEText("Nimi: " + name + "\n" + "Email: " + email + "\n" + "Puhelinnumero: " + phone + "\n" + "Tausta: " + background + "\n" "Tavoitteet: " + objectives + "\n" + "Erityisruokavalio " + allergies + "\n" + "\n" + "Kiitos ilmoittautumisestasi! Infoamme osallistujien valinnasta ilmoittautuneille perjantaina 16.11.2012. \n \n t. Solita Code Tasting Team")
msg['Subject'] = EMAIL_SUBJECT
msg['To'] = EMAIL_SPACE.join(EMAIL_TO)
msg['From'] = EMAIL_FROM
msg.set_charset('utf-8')
mail = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
mail.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())
mail.quit()
