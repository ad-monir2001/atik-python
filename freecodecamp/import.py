from random import choice,randint,random
# rando=choice(['Atikur','rahman','kinder','garden'])
# print(rando)
# coin=choice(['head','tails'])
# print(coin)
import random
# cards=['jack','queen','king']
# random.shuffle(cards)
# for i in range(2+1):
#     print(cards[i])
    
    
import statistics as s
# print(s.mean([1,2,3,4,5]))#*average number

from fractions import Fraction as F
# print(s.mean([F(1,2),F(4,5),F(21,15)]))
# print(F(20,8))

import sys
if len(sys.argv)<1:
    sys.exit('too few a arguments')

elif len(sys.argv)>1:
    sys.exit('too many arguments')
print(f'hello the computer\'s file name is ,{sys.argv[0]}')

from decimal import Decimal as D
# print(s.mean([D('1.5'),D('.5'),D('.5')]))
# print(D('2.53'))
# print(D(.55))


# >>> from decimal import Decimal as D
# >>> mean([D("0.5"), D("0.75"), D("0.625"), D("0.375")])
# Decimal('0.5625')

        #   FRACTION
# (numerator: int | Rational = 0, denominator: int | Rational | None = None) -> Fraction
# >>> Fraction(10, -8)
# Fraction(-5, 4)
# >>> Fraction(Fraction(1, 7), 5)
# Fraction(1, 35)
# >>> Fraction(Fraction(1, 7), Fraction(2, 3))
# Fraction(3, 14)
# >>> Fraction('314')
# Fraction(314, 1)
# >>> Fraction('-35/4')
# Fraction(-35, 4)
# >>> Fraction('3.1415') # conversion from numeric string
# Fraction(6283, 2000)
# >>> Fraction('-47e-2') # string may include a decimal exponent
# Fraction(-47, 100)
# >>> Fraction(1.47)  # direct construction from float (exact conversion)
# Fraction(6620291452234629, 4503599627370496)
# >>> Fraction(2.25)
# Fraction(9, 4)
# >>> Fraction(Decimal('1.47'))
# Fraction(147, 100)

# import cowsay
# print(cowsay.cow('hello Atikur Rahman how are your?'))
# print(cowsay.trex('hello Atikur Rahman how are your?'))


# import pyfiglet

# text = "Hello, ASCII art!"
# ascii_art = pyfiglet.figlet_format(text)
# print(ascii_art)

# from art import *

# text = "Hello ASCII Art!"
# ascii_art = text2art(text)
# print(ascii_art)


# from artistic import Artist

# artist = Artist()
# artist.fromfile("example.jpg")
# artist.display()

from termcolor import colored

text = colored('atikur','green')
print(text)

from colorama import init, Fore
from googletrans import Translator

translator = Translator()
original_text = "Defaulting to user installation because normal site-packages is not writeable"
translated_text = translator.translate(original_text, src='en', dest='bn').text

print(translated_text)

init()


print(Fore.RED + "This text is red.")
print(Fore.GREEN + "This text is green.")
print(Fore.BLUE + "This text is blue.")

# import pyqrcode
# from pyqrcode import QRCode

# # Create a QR code instance
# url = "https://www.example.com"
# qr = pyqrcode.create(url)

# # Save the QR code as an SVG file
# qr.svg("example.svg", scale=8)

import requests
import sys
if len(sys.argv)==1:
    sys.exit()
requests.get("https://www.example.com")