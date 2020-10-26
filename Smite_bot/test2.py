# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 21:01:37 2019

@author: beto_
"""

import sys
from random import randint

print("Hola Tony")
num1 = randint(1,10)
adivinar = False

while not adivinar:
    print("Dame un numero")
    adivinanza = input()
    if(int(adivinanza) > int(num1)):
        print("mas abajo")
    elif (int(adivinanza) < int(num1)):
        print("mas arriba")
    elif (int(adivinanza) == int(num1)):
        adivinar = True
        print("Felicidades! Adivinaste. El número era " + str(num1))