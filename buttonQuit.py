#!/usr/bin/env python3
########################################################################
# Filename    : buttonQuit.py
# Description : bouton extinction Raspberry Pi
# auther      : papsdroid.fr
# modification: 2019/08/31
########################################################################

import RPi.GPIO as GPIO
import time, os


class Button_quit():
    def __init__(self,powerOff=True, buttonPin=40):
        self.powerOff = powerOff        # True: extinction du raspberry, False=Raspberry reste allumé (pour faire des tests)
        self.buttonPin=buttonPin        # Pin GPIO connecté au bouton
        self.on=False                   # etat off au début: bouton non appuyé
        GPIO.setup(self.buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Set buttonPin's mode is input, and pull up to high level(3.3V)
        GPIO.add_event_detect(self.buttonPin,GPIO.FALLING,callback=self.buttonEvent, bouncetime=300)

    def buttonEvent(self,channel): #méthode exécutée lors de l'appui sur le bouton
        self.on = True
        print('button quit pressed, etat=', self.on)
        GPIO.cleanup()
        if self.powerOff:
           print('Extinction Raspberry...')
           os.system('sudo halt')
        raise SystemExit



        
