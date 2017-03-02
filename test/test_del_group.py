# -*- coding: utf-8 -*-
from model.group import Group


def test_delete_first_group_top_button(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.delete_first_group(delete_button="top")


def test_delete_first_group_bottom_button(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.delete_first_group(delete_button="bottom")
