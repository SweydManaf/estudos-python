import re


formatNumberRegex = re.compile(r'(\d{1,3}(,\d{3})*$)')

mo1 = formatNumberRegex.findall(input(': '))

print(mo1)

