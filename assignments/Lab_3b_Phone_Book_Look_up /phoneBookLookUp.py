"""
    Project Name: IT121_Python
    Sub-project: Labs
    File Name: phoneBookLookUp.py
    Author: Dustin McClure
    Lab: Lab 3b Phone Book Look-up
    Modified Date: 10/21/2020

    Python Program that asks for name/phone number/email,
    adds them to a dict, and then provides a lookup function for the user to
    look this info up.
"""
# create an empty dictionary called phone_book where we will store our contacts
phone_book = {}

# function definition for adding contact
def add_contact():

    # request input for the three contacts and output the information
    # entered.
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

    # store this information in a new nested dictionary called phone_book1
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

    # update our main phone book (dictionary phone_book) with the new phone
    # book
    phone_book.update(phone_book1)

# function def to search by phone number/name/email and then print values
def find_name_number_email():

    # request input from user
    search = input("Please enter the name, email, or phone number you would like to look up: ")

    # iterate through values in phone book dict and store result in var
    # values if input is found in values
    values = [value for value in phone_book.values() if search in value]

    # print the values for the contact if they are found
    print(values)

# call function add_contact
add_contact()

# print phone book updated with newly entered contacts
print(phone_book)

# ask user to search for contact by name/email/number using the
# find_name_number_email function setting our data var to phone_book
find_name_number_email()
