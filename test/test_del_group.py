# -*- coding: utf-8 -*-
from model.group import Group


def test_delete_first_group_top_button(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    app.group.delete_first_group(delete_button="top")
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)


def test_delete_first_group_bottom_button(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    app.group.delete_first_group(delete_button="bottom")
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)