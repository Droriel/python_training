# -*- coding: utf-8 -*-
import random
from model.contact import PersonalData, ContactBaseData
from test_addons import adjustments


def test_del_contact_from_the_list(app, db, check_ui):
    if app.contact.count() == 0:
        app.contact.init_new_contact()
        app.contact.fill_personal_data(PersonalData(firstname="test"))
        app.contact.submit_contact()
    old_contacts = db.get_contact_list()
    contact_to_delete = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact_to_delete.contactBaseData.id)
    app.contact.open_main_page()
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(contact_to_delete)
    assert new_contacts == old_contacts
    if check_ui:

        def clean(contact):
            return ContactBaseData(id=contact.contactBaseData.id,
                                   firstname=adjustments.clear_multiple_spaces(contact.contactBaseData.firstname).strip(),
                                   lastname=adjustments.clear_multiple_spaces(contact.contactBaseData.lastname).strip())
        clear_new_contacts = map(clean, new_contacts)
        assert sorted(clear_new_contacts, key=ContactBaseData.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                                   key=ContactBaseData.id_or_max)


def test_del_edited_contact(app, db, check_ui):
    if app.contact.count() == 0:
        app.contact.init_new_contact()
        app.contact.fill_personal_data(PersonalData(firstname="test"))
        app.contact.submit_contact()
    old_contacts = db.get_contact_list()
    contact_to_delete = random.choice(old_contacts)
    app.contact.init_by_id_contact_edition(contact_to_delete.contactBaseData.id)
    app.contact.delete_edited_contact()
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(contact_to_delete)
    assert new_contacts == old_contacts
    if check_ui:

        def clean(contact):
            return ContactBaseData(id=contact.contactBaseData.id,
                                   firstname=adjustments.clear_multiple_spaces(contact.contactBaseData.firstname).strip(),
                                   lastname=adjustments.clear_multiple_spaces(contact.contactBaseData.lastname).strip())
        clear_new_contacts = map(clean, new_contacts)
        assert sorted(clear_new_contacts, key=ContactBaseData.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                                   key=ContactBaseData.id_or_max)