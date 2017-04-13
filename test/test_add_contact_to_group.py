import random

from model.contact import ContactBaseData
from model.group import Group


def test_add_contact_to_group(app, orm):
    if len(orm.get_contact_list()) == 0:
        app.contact.init_new_contact()
        app.contact.fill_contact_base_data(ContactBaseData(firstname="test"))
        app.contact.submit_contact()
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    # choose random contact and group for test
    contact_to_test = random.choice(orm.get_contact_list())
    group_to_test = random.choice(orm.get_group_list())

    old_contacts_in_group = orm.get_contacts_in_group(group_to_test)
    app.contact.add_contact_to_group(contact_to_test.id, group_to_test.id)
    # veryfication if the contact was already in the group
    was = False
    for contact in old_contacts_in_group:
        if contact == contact_to_test:
            was = True
            break
        else:
            was = False
    if was == False:
        old_contacts_in_group.append(contact_to_test)

    new_contacts_in_group = orm.get_contacts_in_group(group_to_test)
    assert sorted(old_contacts_in_group, key=ContactBaseData.id_or_max) == sorted(new_contacts_in_group, key=ContactBaseData.id_or_max)


