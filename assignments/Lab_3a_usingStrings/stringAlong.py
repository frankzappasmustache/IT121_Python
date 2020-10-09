"""
    Project Name: IT121_Python
    Sub-project: Labs
    File Name: stringAlong.py
    Author: Dustin McClure
    Lab: Lab 3a - Using Strings
    Modified Date: 10/06/2020

    {Description of program here}
"""
# Import the class 'Fuck' from the library foaas
from foaas import Fuck
from io import StringIO
import json
from bs4 import BeautifulSoup
import requests
import re

fuck = Fuck()


def magicalFuck():
    print('''Find the most effective application
to tell whoever or whatever to 'fuck off' by
choosing from the following comprehensive list
of actions.\n''')

    print('Main Menu: ')
    for count, item in enumerate(fuck.actions, 0):
        fuckValues = ''.join(str(item))
        print(count, fuckValues)
    print('\n')
    fuckChoice = input('''Choose an Option
    From the Fucks Listed: [0-92] : ''')
    fuckChoice = int(fuckChoice)
    fuckingRequest = input("Please enter fuck options: " )
    return requests.post(fuckingRequest)

magicalFuck()
