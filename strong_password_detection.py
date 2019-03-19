# a program that checks whether a password is strong
# a strong password is one that is at least 8 characters long
# , contains both uppercase and lowercase characters
# , and has at least one digit.

import pyperclip, re, sys

text = str(pyperclip.paste())

if len(text) < 8:
    print('This password is not strong because it is too short')
    sys.exit()

digits = []
uppercase_chars = []
lowercase_chars = []

digit_regex = re.compile(r'\d+')
lowercase_regex = re.compile(r'[a-z]+')
uppercase_regex = re.compile(r'[A-Z]+')

for t in text:
    try:
        uppercase_chars.append(uppercase_regex.search(t).group())
    except:
        pass
    try:
        lowercase_chars.append(lowercase_regex.search(t).group())
    except:
        pass
    try:
        digits.append(digit_regex.search(t).group())
    except:
        pass

if (len(digits) < 1) | (len(uppercase_chars) < 1) | (len(lowercase_chars) < 1):
    print('This password is not strong. A strong password needs to contain at least one uppercase letter, one lowercase letter and one digit.')
else:
    print('Congrats! This password is strong.')
