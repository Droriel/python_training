# -*- coding: utf-8 -*-
import pytest
from model.group import Group
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + ' '*10
    return prefix + ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testData =  [
    Group(name=name, header=header, footer=footer)
    for name in ['', random_string("Nazwa", 10)]
    for header in ['', random_string("Nagłówek", 20)]
    for footer in ['', random_string("Stopka", 20)]
]


# ids = prezentacja danych testowych w sprawozdaniu
@pytest.mark.parametrize('group', testData, ids=[repr(x) for x in testData])
def test_add_group(app, group):
    old_groups = app.group.get_group_list()
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(new_groups, key=Group.id_or_max) == sorted(old_groups, key=Group.id_or_max)

