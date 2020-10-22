"""
    Project Name: IT121_Python
    Sub-project: Labs
    File Name: fuckstrings.py
    Author: Dustin McClure
    Lab: Lab 3a - Using Strings
    Modified 1: Date0/10/2020

    Python Program that asks for name/phone number pairs,
    adds them to a map, and then provides a lookup function for the user to
    look this info up.
"""

phone_book = {}

def add_contact():
    name = input("Please enter a contact name for this new contact: ")
    email = input("Please enter an email address for this new contact: ")
    phone = input("Please enter a phone number for this new contact: ")
    print('''This is the information for the new contact you added
        Full Name: %s
        Email: %s
        Phone Number: %s
        ''' % (name, email, phone))
    name2 = input("Please enter a contact name for this new contact: ")
    email2 = input("Please enter an email address for this new contact: ")
    phone2 = input("Please enter a phone number for this new contact: ")
    print('''This is the information for the new contact you added
        Full Name: %s
        Email: %s
        Phone Number: %s
        ''' % (name2, email2, phone2))
    name3 = input("Please enter a contact name for this new contact: ")
    email3 = input("Please enter an email address for this new contact: ")
    phone3 = input("Please enter a phone number for this new contact: ")
    print('''This is the information for the new contact you added
        Full Name: %s
        Email: %s
        Phone Number: %s
        ''' % (name3, email3, phone3))

    phone_book1 = {
    0: [
    name,
    email,
    phone
    ],
    1: [
    name2,
    email2,
    phone2
    ],
    2: [
    name3,
    email3,
    phone3
    ]
    }

    phone_book.update(phone_book1)

def find_name_number_email(data):
    search = input("Please enter the name, email, or phone number you would like to look up: ")
    values = [value for value in phone_book.values() if search in value]
    print(values)


add_contact()
print(phone_book)
find_name_number_email(data=phone_book)
