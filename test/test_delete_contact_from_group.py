import random

from model.contact import ContactBaseData
from model.group import Group


def test_delete_contact_from_group(app, orm):
    # condition for lack of contacts or groups
    if len(orm.get_contact_list()) == 0:
        app.contact.init_new_contact()
        app.contact.fill_contact_base_data(ContactBaseData(firstname="test"))
        app.contact.submit_contact()
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    # veri=yfication and condition for lack of groups having any contacts
    groups = orm.get_group_list()
    groups_with_contacts = []
    for group in groups:
        if len(orm.get_contacts_in_group(group))>0 :
            groups_with_contacts.append(group)
    if len(groups_with_contacts)==0:
        contact_to_add=random.choice(orm.get_contact_list())
        group_to_add=random.choice(groups)
        app.contact.add_contact_to_group(contact_to_add.id, group_to_add.id)
        groups_with_contacts.append(group_to_add)
    # choosing group and contacts to delete
    group_to_test = random.choice(groups_with_contacts)
    contact_to_test = random.choice(orm.get_contacts_in_group(group_to_test))
    old_contacts_in_group = orm.get_contacts_in_group(group_to_test)
    # deleting
    app.contact.delete_contact_from_group(contact_to_test.id, group_to_test.id)
    old_contacts_in_group.remove(contact_to_test)
    new_contacts_in_group = orm.get_contacts_in_group(group_to_test)

    assert sorted(old_contacts_in_group, key=ContactBaseData.id_or_max) == sorted(new_contacts_in_group,
                                                                                  key=ContactBaseData.id_or_max)