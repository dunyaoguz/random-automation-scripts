# a program that adds bulletpoints to the start of each line to a copied text

import pyperclip

text = pyperclip.paste()

lines = text.split('\n')

fixed = []

for i in range(len(lines)):
    fixed.append('* ' + lines[i])

final = '\n'.join(fixed)

pyperclip.copy(final)
