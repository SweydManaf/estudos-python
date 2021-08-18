from logging import basicConfig, getLogger, DEBUG
from collections import deque
from pdb import post_mortem
from sys import exc_info

basicConfig(filename='teste.log',
            filemode='w',
            level=DEBUG)

log = getLogger(__name__)

log.info('Teste')

try:
    0/0
except:
    for line in deque(open('teste.log'), 10):
        print(line)
    post_mortem(exc_info()[2])