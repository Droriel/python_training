# -*- coding: utf-8 -*-
from random import randrange
from model.group import Group


def test_edit_first_group_top_edit(app, json_groups):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    # randrange - generuje losową wartość od 0 do podanego parametru
    index = randrange(len(old_groups))
    group = json_groups
    group.id = old_groups[index].id
    app.group.edit_group_by_index(index, group, edit_button='top')
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(new_groups, key=Group.id_or_max) == sorted(old_groups, key=Group.id_or_max)


def test_edit_first_group_bottom_edit(app, json_groups):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = json_groups
    group.id = old_groups[index].id
    app.group.edit_group_by_index(index, group, edit_button='bottom')
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(new_groups, key=Group.id_or_max) == sorted(old_groups, key=Group.id_or_max)

