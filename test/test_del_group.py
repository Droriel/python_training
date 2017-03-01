# -*- coding: utf-8 -*-


def test_delete_first_group_top_button(app):
    app.group.delete_first_group(delete_button="top")


def test_delete_first_group_bottom_button(app):
    app.group.delete_first_group(delete_button="bottom")
