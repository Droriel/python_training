# -*- coding: utf-8 -*-
from model.group import Group


def test_edit_first_group_top_edit(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="Nazwa1", header="Nagłówek1", footer="Stopka1"), edit_button='top')
    app.session.logout()


def test_edit_first_group_bottom_edit(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="Nazwa2", header="Nagłówek2", footer="Stopka2"), edit_button='bottom')
    app.session.logout()


def test_edit_first_group_top_edit_name(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="Nazwa3"), edit_button='top')
    app.session.logout()


def test_edit_first_group_top_edit_header(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(header="Nagłówek3"), edit_button='top')
    app.session.logout()
