# -*- coding: utf-8 -*-
from random import randrange
from model.group import Group


def test_edit_first_group_top_edit(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    # randrange - generuje losową wartość od 0 do podanego parametru
    index = randrange(len(old_groups))
    group = Group(name="Nazwa1", header="Nagłówek1", footer="Stopka1")
    group.id = old_groups[index].id
    app.group.edit_group_by_index(index, group, edit_button='top')
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(new_groups, key=Group.id_or_max) == sorted(old_groups, key=Group.id_or_max)


def test_edit_first_group_bottom_edit(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="Nazwa2", header="Nagłówek2", footer="Stopka2")
    group.id = old_groups[index].id
    app.group.edit_group_by_index(index, group, edit_button='bottom')
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(new_groups, key=Group.id_or_max) == sorted(old_groups, key=Group.id_or_max)


def test_edit_first_group_top_edit_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="Nazwa3")
    group.id = old_groups[index].id
    app.group.edit_group_by_index(index, group, edit_button='top')
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(new_groups, key=Group.id_or_max) == sorted(old_groups, key=Group.id_or_max)


def test_edit_first_group_top_edit_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test", header="test"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(header="Nagłówek3")
    group.id = old_groups[index].id
    group.name = old_groups[index].name
    app.group.edit_group_by_index(index, group, edit_button='top')
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(new_groups, key=Group.id_or_max) == sorted(old_groups, key=Group.id_or_max)
