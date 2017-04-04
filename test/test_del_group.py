# -*- coding: utf-8 -*-
import random
from model.group import Group


def test_delete_some_group_top_button(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    # randrange - generuje losową wartość od 0 do podanego parametru
    # index = randrange(len(old_groups))
    app.group.delete_group_by_id(group.id, delete_button="top")
    assert len(old_groups) - 1 == app.group.count()
    new_groups = db.get_group_list()
    old_groups.remove(group)
    assert new_groups == old_groups


def test_delete_first_group_bottom_button(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    group = random.choice(old_groups)
    app.group.delete_group_by_id(group.id, delete_button="bottom")
    assert len(old_groups) - 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.remove(group)
    assert new_groups == old_groups
