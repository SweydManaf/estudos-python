import re
pattern = re.compile(r'(\d{2}[/]\d{2}[/]\d{4})')
with open('documents.txt', 'r+') as file:
    oldText = file.read()
    newText = pattern.sub('DATA', oldText)

with open('documents.txt', 'w') as fileNew:
    fileNew.write(newText)