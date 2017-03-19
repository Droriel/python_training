# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from data.add_group import testData
# from data.add_group import constant as testData


# ids = prezentacja danych testowych w sprawozdaniu
@pytest.mark.parametrize('group', testData, ids=[repr(x) for x in testData])
def test_add_group(app, group):
    old_groups = app.group.get_group_list()
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(new_groups, key=Group.id_or_max) == sorted(old_groups, key=Group.id_or_max)

