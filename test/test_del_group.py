# -*- coding: utf-8 -*-
import random
from model.group import Group
from test_addons import adjustments


def test_delete_some_group_top_button(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    # randrange - generuje losową wartość od 0 do podanego parametru
    # index = randrange(len(old_groups))
    app.group.delete_group_by_id(group.id, delete_button="top")
    new_groups = db.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups.remove(group)
    assert new_groups == old_groups

    def clean(group):
        return Group(id=group.id, name=adjustments.clear_multiple_spaces(group.name).strip())
    clear_new_groups = map(clean, new_groups)
    if check_ui:
        assert sorted(clear_new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


def test_delete_first_group_bottom_button(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.delete_group_by_id(group.id, delete_button="bottom")
    new_groups = db.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups.remove(group)
    assert new_groups == old_groups

    def clean(group):
        return Group(id=group.id, name=adjustments.clear_multiple_spaces(group.name).strip())
    clear_new_groups = map(clean, new_groups)
    if check_ui:
        assert sorted(clear_new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

