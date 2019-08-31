#!/usr/bin/env python3
########################################################################
# Filename    : piOff.py
# Description : test bouton extinction Raspberry Pi
# auther      : papsdroid.fr
# modification: 2019/08/31
########################################################################

import time
import RPi.GPIO as GPIO
from buttonQuit import Button_quit

class Application:
    def __init__(self):
        print ('Program is starting ... ')
        GPIO.setmode(GPIO.BOARD)                        # identification des GPIOs par location physique
        self.buttonQuit = Button_quit(powerOff=True)    # mettre powerOff=False pour des tests sans extinction du rpi

    #boulce principale du prg
    def loop(self):
        while True :
            #todo ... code du programme à ajouter ici  ... 
            time.sleep(1)  # attend une seconde: à retirer

    #méthode de destruction    
    def destroy(self):
        print ('bye')
        GPIO.cleanup()
        #todo code à ajouter ici avant de sortir du programme
        
    
if __name__ == '__main__':
    appl=Application()
    try:
        appl.loop()
    except KeyboardInterrupt:  # interruption clavier CTRL-C: appel à la méthode destroy() de appl.
        appl.destroy()
