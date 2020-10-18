"""
Python Program that asks for name/phone number pairs, adds them to a map, and then provides a lookup function for the user to look this info up.
"""
phone_book = [];

def get_contact_name(contactName):
    contactName = input("Enter a new contact name: ")
    phone_book.append(contactName)

def get_contact_phone(contactPhone):
    contactPhone = input("Enter a new phone number for this contact: ")
    phone_book.append(contactPhone)

    def add_email(name, email):
    add_contact(name)
    if 'emails' in phone_book[name]:
        if email in phone_book[name]['emails']:
            pass
        else:
            phone_book[name].append(email)
    else:
        phone_book[name]['emails'] = [email]
    print("email added")

    def search_name(name):
    if name in phone_book:
        print(phone_book[name])
    else:
        print("name didn't exist")

def search_number(number):
    for name in phone_book:
        if 'numbers' in phone_book[name]:
            if number in phone_book[name]['numbers']:
                print(name)
                return
    print('number did not exist')

contactPhone1 = input("Enter a new contact phone number: ");
get_contact_phone(contactPhone1)
