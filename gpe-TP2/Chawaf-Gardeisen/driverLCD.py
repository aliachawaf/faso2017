#coding: utf-8

import smbus

bus = smbus.SMBus(1)	# pour I2C-1 (port 1 du shield)


DISPLAY_RGB_ADDR = 0x62		#adresse du shield
DISPLAY_TEXT_ADDR = 0x3e 	#adresse de l'écran LCD



def lcd_couleur(rouge, vert, bleu):
#affiche sur l'écran une couleur obtenue par mélange du degré du rouge, vert et bleu choisis

	bus.write_byte_data(DISPLAY_RGB_ADDR,0x00,0x00)
	bus.write_byte_data(DISPLAY_RGB_ADDR,0x01,0x00)
	bus.write_byte_data(DISPLAY_RGB_ADDR,0x02,bleu)
	bus.write_byte_data(DISPLAY_RGB_ADDR,0x03,vert)
	bus.write_byte_data(DISPLAY_RGB_ADDR,0x04,rouge)
	bus.write_byte_data(DISPLAY_RGB_ADDR,0x08,0xAA)



def lcd_commande(cmd):
#affiche un caractère sur l'écran

	bus.write_byte_data(DISPLAY_TEXT_ADDR,0x80,cmd)



def lcd_message(string):
#fonction permettant d'afficher le texte recu en paramètre sur l'écran
	lcd_commande(0x01)
	lcd_commande(0x0F)
	lcd_commande(0x38)

	for c in string:
		bus.write_byte_data(DISPLAY_TEXT_ADDR,0x40,ord(c))



