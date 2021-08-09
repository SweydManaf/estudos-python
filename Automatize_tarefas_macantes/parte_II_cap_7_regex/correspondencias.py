import re

# ---------- Correspondencia com pipe --------------
heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Frey')
print(mo1.group())

mo2 = heroRegex.search('Tina Fey and Batman.')
mo2.group()
print(mo2.group())

# -------------- Especificar o prefixo ----------------
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group(1))
print('-='*30)


# ----------- Correspondencia opcional ----------------
batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman.')
print(mo1.group())


phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo1 = phoneRegex.search('My number is 415-555-4242')
print(mo1.group())

mo2 = phoneRegex.search('My number is 555-4242')
print(mo2.group())
print('-='*30)


# -- Correspondencias a zero ou mais ocorrencias ------
""" * - zero ou mais. """

batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())

mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())

mo3 = batRegex.search('The Adventures of Batwowowoman')
print(mo3.group())
print('-='*30)

# Correspondencias a uma ou mais ocorrencias ----------
"""+ - um ou mais. """

batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batwoman')
print(mo1.group())

mo2 = batRegex.search('The Adeventures of Batwowowoman')
print(mo2.group())

mo3 = batRegex.search('The adventures of Batman')
if mo3 == None: print(True)
print('-='*30)
# ------- Comparando repeticoes especificas -------

haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('HaHaHa')
print(mo1.group())

mo2 = haRegex.search('Ha')
if mo2 == None: print(True)
print('-='*30)

# ----- greedy (gulosas) e nongreedy (nao gulosas) ---------
greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
print(mo1.group())

nongreedyHaRegex = re.compile('(Ha){3,5}?')
mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
print(mo2.group())






