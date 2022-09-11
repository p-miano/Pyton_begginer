"""
Email registration:
Create a program that allows the registration of a person's name and email (through inputs) and that checks:
If name and e-mail have been filled in, otherwise notify user to fill in all the data correctly.
If the email contains '@' and if after the '@' there is a '.', otherwise it should display an invalid email message.

"""

name = input("Name: ")
email = input("Email: ")

#removing extra spaces at the beginning and end
name = name.strip()
email = email.strip()

if name != '' and email != '':
    spaceless_name = name.replace(' ', '')
    if spaceless_name.isalpha():    
        if '@' in email:
            email_list = email.split('@')
            server = email_list[1]
            if '.' in server:
                print('Name is {} and email is {}.'.format(name, email))
            else:
                print('Invalid email.')  
        else:
            print('Invalid email.')
    else:
        print('Fill in name correctly')
else:
    print('Fill in all data correctly.')