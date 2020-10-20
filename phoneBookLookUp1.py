"""
    Project Name: IT121_Python
    Sub-project: Labs
    File Name: fuckstrings.py
    Author: Dustin McClure
    Lab: Lab 3a - Using Strings
    Modified Date: 10/10/2020

    Python Program that asks for name/phone number pairs,
    adds them to a map, and then provides a lookup function for the user to
    look this info up.
"""
import pprint
import copy
from collections import namedtuple

phone_book = {}

def contacts():
    lcontacts = list()
    return lcontacts

def contact():
    ncontact = namedtuple('contact', ['contact_name', 'contact_phone', 'contact_email'], defaults=[0])
    return ncontact

def cname():
    print("Please enter a new name for this contact:")
    contact_name = input()
    print('name added')
    return contact_name


def add_contact():
    new_contact = contact()
    new_cname = cname()
    new_cemail = cemail()
    new_phone = phone()
    new_contacts = contacts()
    new_cname()
    return contact_name
    # check to see if the contact exists, if so call detect_dup, if not add
    if contact_name in phone_book:
        print('''This contact already exists in your phone book. Would
            you like to overwrite the existing contact?''')
    else:
        new_cemail()
        return contact_email
        new_phone()
        return contact_phone
        new_contact()
        return ncontact(contact_name, contact_phone, contact_email)
        new_contacts()
        return lcontacts(ncontact)
        phone_book.append(lcontacts)

def phone():
    print("Enter a new phone number for this contact:")
    contact_phone = input()
    print("number added")
    return contact_phone

def cemail():
    print("Enter a new email address for this contact:")
    contact_email = input()
    print("email added")
    return contact_email

def name_search(contact_name):
    contact_name = input("Please enter the First Name and Last Name of the person you would like to search for: ")
    if contact_name in phone_book:
        for contacts in phone_book:
            for contact in contacts:
                print([contact_name][contact_email][contact_phone])
    else:
        return print("This contact does not exist")

def search_number(contact_number):
    for contact in phone_book:
        if 'contact_number' in phone_book:
            print(contact_name)
        else:
            return print("No contact was found under this phone number")
add_contact()
