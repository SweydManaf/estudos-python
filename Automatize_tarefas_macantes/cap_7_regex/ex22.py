import re

specialRegex = re.compile(r'((alice|bob|carol) '
                          r'(eats|pets|throws|) '
                          r'(apples|cats|baseballs.))',
                          re.IGNORECASE)

analisExp = specialRegex.findall('''
Alice eats apples.
Bob pets cats. 
Carol throws baseballs. 
Alice throws Apples. 
BOB EATS CATS. 
RoboCop eats apples. 
ALICE THROWS FOOTBALLS. 
Carol eats 7 cats. ''')

for groups in analisExp:
    print(groups[0])