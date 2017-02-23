# -*- coding: utf-8 -*-
from model.group import Group


def test_edit_first_group_top_edit(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_top_edit(Group(name="Nazwa1", header="Nagłówek1", footer="Stopka1"))
    app.session.logout()


def test_edit_first_group_bottom_edit(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_bottom_edit(Group(name="Nazwa2", header="Nagłówek2", footer="Stopka2"))
    app.session.logout()
