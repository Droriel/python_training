# -*- coding: utf-8 -*-
from model.group import Group


def test_edit_first_group_top_edit(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.edit_first_group(Group(name="Nazwa1", header="Nagłówek1", footer="Stopka1"), edit_button='top')


def test_edit_first_group_bottom_edit(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.edit_first_group(Group(name="Nazwa2", header="Nagłówek2", footer="Stopka2"), edit_button='bottom')


def test_edit_first_group_top_edit_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.edit_first_group(Group(name="Nazwa3"), edit_button='top')


def test_edit_first_group_top_edit_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test", header="test"))
    app.group.edit_first_group(Group(header="Nagłówek3"), edit_button='top')
