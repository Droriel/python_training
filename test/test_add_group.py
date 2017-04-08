# -*- coding: utf-8 -*-
from model.group import Group
from test_addons import adjustments


def test_add_group(app, db, json_groups, check_ui):
    group = json_groups
    old_groups = db.get_group_list()
    app.group.create(group)
    new_groups = db.get_group_list()
    old_groups.append(group)
    assert sorted(new_groups, key=Group.id_or_max) == sorted(old_groups, key=Group.id_or_max)
    if check_ui:

        def clean(group):
            return Group(id=group.id, name=adjustments.clear_multiple_spaces(group.name).strip())
        clear_new_groups = map(clean, new_groups)
        assert sorted(clear_new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

