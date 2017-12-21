#coding: utf-8
import smtplib
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from smtplib import SMTP
import sys





def send_email2():


    gmail_user = "bali.rasp30@gmail.com"
    gmail_pwd = "balirasp30"
    FROM = "bali, votre amour"
    TO = "bali.rasp30@gmail.com"
    SUBJECT = "Votre courrier a ete recupere <3"
    TEXT = """\
Vous avez releve votre courrier ! Et réinitialiser votre boite aux lettres

XXXX
Bali, votre boite aux lettres intelligente à votre service.
Qui vous aime.
"""
    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)

        server.ehlo()

        server.starttls()

        server.login(gmail_user, gmail_pwd)

        server.sendmail(FROM, TO, message)

        server.close()
        print 'successfully sent the mail'
    except:
        print "failed to send mail"

def send_email():


    gmail_user = "bali.rasp30@gmail.com"
    gmail_pwd = "balirasp30"
    FROM = "bali, votre amour"
    TO = "bali.rasp30@gmail.com"
    SUBJECT = "Courrier reçu <3"
    TEXT = """\
Vous avez reçu du courrier! Allez le récupérer !
Et n'oubliez pas d'appuyer sur le bouton pour les prochaines fois.

XXXX
Bali, votre boite aux lettres intelligente à votre service.
Qui vous aime.
"""


    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)

        server.ehlo()

        server.starttls()

        server.login(gmail_user, gmail_pwd)

        server.sendmail(FROM, TO, message)

        server.close()
        print 'successfully sent the mail'

    except:
        print "failed to send mail"




def send_Bilan():

	gmail_user = "bali.rasp30@gmail.com"
	gmail_pwd = "balirasp30"
	FROM = "bali, votre amour"
	TO = "bali.rasp30@gmail.com"
	SUBJECT = "Voici le bilan mensuel de ce mois ci "
	TEXT = """\ envoie de la piece jointe """

	msg = MIMEMultipart()
	msg['Subject']=SUBJECT 
	msg['From']=FROM
	
	part = MIMEApplication(open('graphique.png',"rb").read())
	part.add_header('Content-Disposition', 'attachment', filename='graphique.png')
	msg.attach(part)
 

	server = smtplib.SMTP("smtp.gmail.com:587")
	server.ehlo()
	server.starttls()
	server.login(gmail_user, gmail_pwd)
 
	server.sendmail(msg['From'], TO , msg.as_string())






