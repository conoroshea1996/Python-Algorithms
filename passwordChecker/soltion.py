import re


def soltion():
    password = input('Enter your password \n >')

    if re.search('[^a-zA-Z0-9]', password):
        if len(password) < 6:
            print('password too short')
        elif len(password) > 12:
            print('Password to long')
        else:
            print('password saved')
    else:
        print('wrong format')


soltion()
