#coding: utf-8
import smtplib
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from smtplib import SMTP
import sys


#pour le mail de reinitialisation de la boite
def send_email2():

	#declaration des variables utilise dans la suite
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
    	#Preparation du mail a envoyer
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT) 			##la description du message
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587) #le serveur que l'on utilise pour envoyer le mail

        server.ehlo() #pour se connecter a notre boite mail

        server.starttls() #pour crypter les commandes qui suivent (a cause du mot de passe)

        server.login(gmail_user, gmail_pwd) #notre boite mail 

        server.sendmail(FROM, TO, message) #pour  envoyer de mail

        server.close()
        print 'successfully sent the mail reinitialisation'
    except:
        print "failed to send mail"



#pour le mail de reception courrier
def send_email():

	#declaration des variables utilise dans la suite

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

	# Preparation du mail a envoyer


    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)			#la description du message
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)		#le serveur que l'on utilise pour envoyer le mail


        server.ehlo()			#pour se connecter a notre boite mail

        server.starttls() 		#pour crypter les commandes qui suivent (a cause du mot de passe)

        server.login(gmail_user, gmail_pwd) 	#notre boite mail 

        server.sendmail(FROM, TO, message) 	#pour  envoyer de mail

        server.close()
        print 'successfully sent the mail reception'

    except:
        print "failed to send mail"




#Pour l'envoi du bilan a la fin de chaque mois 
def send_Bilan():

		#declaration des variables utilise dans la suite

	gmail_user = "bali.rasp30@gmail.com"
	gmail_pwd = "balirasp30"
	FROM = "bali, votre amour"
	TO = "bali.rasp30@gmail.com"
	SUBJECT = "Voici le bilan mensuel de ce mois ci "
	TEXT = """\ envoie de la piece jointe """

		# Preparation du mail a envoyer

	msg = MIMEMultipart()
	msg['Subject']=SUBJECT 
	msg['From']=FROM
	
	part = MIMEApplication(open('graphique.png',"rb").read()) #pour chosir la piece jointe que l'on veut attacher et pouvoir l'ouvir
	part.add_header('Content-Disposition', 'attachment', filename='graphique.png') #pour aller la chercher (adressage)
	msg.attach(part) #pour le lier 
 

	server = smtplib.SMTP("smtp.gmail.com:587") 	#le serveur que l'on utilise pour envoyer le mail
	server.ehlo()		#pour se connecter a notre boite mail
	server.starttls()	#pour crypter les commandes qui suivent (a cause du mot de passe)
	server.login(gmail_user, gmail_pwd ) #notre boite mail 

 
	server.sendmail(msg['From'], TO , msg.as_string())	#pour  envoyer de mail
	print "successfully sent  mail with attach files"




#Pour l'envoi du bilan de Demo
def send_BilanDemo():

		#declaration des variables utilise dans la suite
        gmail_user = "bali.rasp30@gmail.com"
        gmail_pwd = "balirasp30"
        FROM = "bali, votre amour"
        TO = "bali.rasp30@gmail.com"
        SUBJECT = "Voici le graphique de demonstration "
        TEXT = """\ envoie de la piece jointe """

		 # Preparation du mail a envoyer

        msg = MIMEMultipart()
        msg['Subject']=SUBJECT 
        msg['From']=FROM

        part = MIMEApplication(open('Demo/DemoGraphique.png',"rb").read()) #pour chosir la piece jointe que l'on veut attacher et pouvoir l'ouvir
        part.add_header('Content-Disposition', 'attachment', filename='DemoGraphique.png') #pour aller la chercher (adressage)
        msg.attach(part) #pour le lier
 

        server = smtplib.SMTP("smtp.gmail.com:587") #le serveur que l'on utilise pour envoyer notre mail
        server.ehlo() 	#pour se connecter a la boite mail qui va envoyer le mail
        server.starttls() #pour cripter les prochaines instructions SMTP
        server.login(gmail_user, gmail_pwd)	#notre boite mail
 
        server.sendmail(msg['From'], TO , msg.as_string())	 #pour  envoyer de mail
	print "successfully sent mail DEMO with attach files"


