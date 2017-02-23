# -*- coding: utf-8 -*-


def test_delete_first_group_top_button(app):
    app.session.login(username="admin", password="secret")
    app.group.delete_first_group_top_button()
    app.session.logout()


def test_delete_first_group_bottom_button(app):
    app.session.login(username="admin", password="secret")
    app.group.delete_first_group_bottom_button()
    app.session.logout()