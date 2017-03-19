# -*- coding: utf-8 -*-
import random
import string
from model.group import Group

# Stałe dane testowe

constant = [
    Group(name='name1', header='header1', footer='footer1'),
    Group(name='name2', header='header2', footer='footer2')
]

# Losowe dane testowe

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + ' '*10
    return prefix + ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testData = [
    Group(name=name, header=header, footer=footer)
    for name in ['', random_string("Nazwa", 10)]
    for header in ['', random_string("Nagłówek", 20)]
    for footer in ['', random_string("Stopka", 20)]
]

