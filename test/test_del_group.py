# -*- coding: utf-8 -*-
from random import randrange
from model.group import Group


def test_delete_some_group_top_button(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    # randrange - generuje losową wartość od 0 do podanego parametru
    index = randrange(len(old_groups))
    app.group.delete_group_by_index(index, delete_button="top")
    assert len(old_groups) - 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index:index+1] = []
    assert new_groups == old_groups


def test_delete_first_group_bottom_button(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    app.group.delete_group_by_index(index, delete_button="bottom")
    assert len(old_groups) - 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index:index+1] = []
    assert new_groups == old_groups
