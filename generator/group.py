# -*- coding: utf-8 -*-
import random
import string
from model.group import Group
import jsonpickle
import os.path
import sys
import getopt

try:
    opts, args=getopt.getopt(sys.argv[1:], 'n:f:', ['number of groups', 'file'])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = 'data/groups.json'

for o, a in opts:
    if o == '-n':
        n = int(a)
    elif o == '-f':
        f = a
# opcje wpisujemy w opcje skryptu "-n 10 -f data/test,json"

def random_string(prefix, maxlen):
    # symbols = string.ascii_letters + string.digits + string.punctuation + ' '*10
    symbols = string.ascii_letters + string.digits + ' ' * 15 + '\n' * 5 + '-' * 3 + '_' * 3
    return prefix + ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testData = [Group(name='', header='', footer='')] + \
[
        Group(name=random_string("Nazwa", 10), header=random_string("Naglowek", 20), footer=random_string("Stopka", 20))
    for i in range(n)

] + \
        [Group(name=random_string("Nazwa", 10), header='', footer='')] + \
        [Group(name='', header=random_string("Naglowek", 20), footer='')] + \
        [Group(name='', header='', footer=random_string("Stopka", 20))]
# random na kombinacjach pola pustego i niepustego
# testData = [
#     Group(name=name, header=header, footer=footer)
#     for name in ['', random_string("Nazwa", 10)]
#     for header in ['', random_string("Nagłówek", 20)]
#     for footer in ['', random_string("Stopka", 20)]
# ]


# file = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), './data/groups.json')
file = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..' , f)

with open(file, 'w', encoding='utf8') as out:
    jsonpickle.set_encoder_options('json', indent=2)
    out.write(jsonpickle.encode(testData))