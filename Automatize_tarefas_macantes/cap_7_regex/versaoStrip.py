import re

pattern = re.compile(r'^(\s)+|(\s)+$') # remove espaćos no ininio e no fim
print(pattern.sub('', '   Sweyd     Abdul    '))
