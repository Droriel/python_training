# -*- coding: utf-8 -*-
from random import randrange
from model.group import Group
import random
from test_addons import adjustments


def test_edit_first_group_top_edit(app, db, json_groups, check_ui):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    # randrange - generuje losową wartość od 0 do podanego parametru
    group_to_edit = random.choice(old_groups)
    group = json_groups
    group.id = group_to_edit.id
    app.group.edit_group_by_id(group.id, group, edit_button='top')
    new_groups = db.get_group_list()
    for i in range(len(old_groups)):
        if old_groups[i] == group_to_edit:
            old_groups[i] = group
    assert sorted(new_groups, key=Group.id_or_max) == sorted(old_groups, key=Group.id_or_max)

    def clean(group):
        return Group(id=group.id, name=adjustments.clear_multiple_spaces(group.name).strip())
    clear_new_groups = map(clean, new_groups)
    if check_ui:
        assert sorted(clear_new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


def test_edit_first_group_bottom_edit(app, db, json_groups, check_ui):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    group_to_edit = random.choice(old_groups)
    group = json_groups
    group.id = group_to_edit.id
    app.group.edit_group_by_id(group.id, group, edit_button='bottom')
    new_groups = db.get_group_list()
    for i in range(len(old_groups)):
        if old_groups[i] == group_to_edit:
            old_groups[i] = group
    assert sorted(new_groups, key=Group.id_or_max) == sorted(old_groups, key=Group.id_or_max)

    def clean(group):
        return Group(id=group.id, name=adjustments.clear_multiple_spaces(group.name).strip())
    clear_new_groups = map(clean, new_groups)
    if check_ui:
        assert sorted(clear_new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

