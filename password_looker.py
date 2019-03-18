#! python3
# An insecure password locker program.

import pyperclip

action = input('Do you wish to copy a password onto the clipboard or save a new password? Enter C for the former and P for the latter: ')

passwords = {}

while True:
    if action.upper() == 'C':
        account = input('Enter name of the account whose password you need: ')
        while True:
            if account in passwords:
                pyperclip.copy(passwords[account])
                print('Password for' + account + 'copied to clipboard.')
                break
            else:
                next_step = input('There is no account named ' + account + '. Enter exit if you wish to exit the program, and continue if you want to lookup another account: ')
                if next_step.lower() == 'exit':
                    break
        break
    elif action.upper() == 'P':
        new_account = input('Enter the account name you want to save a new password for: ')
        password = input('Enter the password: ')
        passwords[new_account] = password
        print('Your password was saved.')
        break
    else:
        print('You have not entered a valid answer. Please answer with C or P.')
        action = input('Do you wish to copy a password onto clipboard or save a new password? Enter C for the former and P for the latter.')

print('Thanks for using this program. See you soon!')
