import os
import os.path

for a in os.listdir('.'):
    if os.path.isdir(a):
        print(f'{a}/')
    elif os.path.isfile(a):
        print(f'{a}')