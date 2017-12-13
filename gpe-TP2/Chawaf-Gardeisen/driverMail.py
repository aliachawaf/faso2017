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
    SUBJECT = "Votre courrer a ete recupere <3"
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






def send_mail_attach_files():


	gmail_user = "bali.rasp30@gmail.com"
    	gmail_pwd = "balirasp30"
    	FROM = "bali, votre amour"
    	TO = "bali.rasp30@gmail.com"
    	SUBJECT = "Votre courrer a ete recupere <3"
    	TEXT = """\
		Vous avez releve votre courrier ! Et réinitialiser votre boite aux lettres

		XXXX
	Bali, votre boite aux lettres intelligente à votre service.
	Qui vous aime.
	"""



	part = MIMEApplication(open("graphe.png"),"rb").read()
	part.add_header('Content-Disposition', 'attachment', filename="plot.png")
        msg.attach(part)




	    # Prepare actual message
	message = """From: %s\nTo: %s\nSubject: %s\n\n%s""" % (FROM, ", ".join(TO), SUBJECT, TEXT)
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




