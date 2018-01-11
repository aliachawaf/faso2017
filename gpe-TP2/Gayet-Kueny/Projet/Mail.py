#!/usr/bin/env python
#-*- coding: utf-8 -*-

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

#envoie un mail conccernant le reservoir, pour l'instant elle envoie simplement un rappel
#par la suite on pourrais lui donner d'autre parramètre, telle que la date du dernier arosage, du premir mail envoyer a se sujet
def sendMailReservoirVide (destinataire):
	msg = MIMEMultipart() #on définie le type du message 
	msg['From'] = 'e-sprinkler'
	msg['To'] = destinataire 
	msg['Subject'] = 'e-sprinkler alerte' 
	message =''' Ce message vous est envoyé par votre e-sprinkler.

Bonjour
Le reservoir d\'eau du système est vide, e-sprinkler ne peut plus arroser il faut que vous le remplissiez.'''

	msg.attach(MIMEText(message))
	mailserver = smtplib.SMTP('smtp.gmail.com', 587) #on selectionne la boite mail de l'envoyeur gmail/yahou/orange
	mailserver.ehlo()
	mailserver.starttls()
	mailserver.ehlo()
	mailserver.login('gayet.kueny@gmail.com', 'projetfas') #on se connecte au compte de gmail de l'envoyeur
	mailserver.sendmail('gayet.kueny@gmail.com', destinataire, msg.as_string())
	mailserver.quit()

 
#envoie un mail conccernant les seuils de températures, pour l'instant elle envoie simplement un rappel
#par la suite on pourrais lui donner d'autre parramètre, comme les températures
def sendMailConditionCritique(destinataire):
	msg = MIMEMultipart() #on définie le type du message 
	msg['From'] = 'e-sprinkler'
	msg['To'] = destinataire 
	msg['Subject'] = 'e-sprinkler alerte' 
	message = '''Ce message vous est envoyé par votre e-sprinkler.

Bonjour
Votre plante est en train de subir des conditions critiques, les seuils de température que vous nous avez donnés on été dépassés.   ''' 
	msg.attach(MIMEText(message))
	mailserver = smtplib.SMTP('smtp.gmail.com', 587)  #on selectionne la boite mail de l'envoyeur gmail/yahou/orange
	mailserver.ehlo()
	mailserver.starttls()
	mailserver.ehlo()
	mailserver.login('gayet.kueny@gmail.com', 'projetfas') #on se connecte au compte de gmail de l'envoyeur 
	mailserver.sendmail('gayet.kueny@gmail.com', destinataire, msg.as_string())
	mailserver.quit()
