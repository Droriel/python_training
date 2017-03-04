# -*- coding: utf-8 -*-
from model.group import Group


def test_edit_first_group_top_edit(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    group = Group(name="Nazwa1", header="Nagłówek1", footer="Stopka1")
    group.id = old_groups[0].id
    app.group.edit_first_group(group, edit_button='top')
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(new_groups, key=Group.id_or_max) == sorted(old_groups, key=Group.id_or_max)


def test_edit_first_group_bottom_edit(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    group = Group(name="Nazwa2", header="Nagłówek2", footer="Stopka2")
    group.id = old_groups[0].id
    app.group.edit_first_group(group, edit_button='bottom')
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(new_groups, key=Group.id_or_max) == sorted(old_groups, key=Group.id_or_max)


def test_edit_first_group_top_edit_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    group = Group(name="Nazwa3")
    group.id = old_groups[0].id
    app.group.edit_first_group(group, edit_button='top')
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(new_groups, key=Group.id_or_max) == sorted(old_groups, key=Group.id_or_max)


def test_edit_first_group_top_edit_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test", header="test"))
    old_groups = app.group.get_group_list()
    group = Group(header="Nagłówek3")
    group.id = old_groups[0].id
    group.name = old_groups[0].name
    app.group.edit_first_group(group, edit_button='top')
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(new_groups, key=Group.id_or_max) == sorted(old_groups, key=Group.id_or_max)
