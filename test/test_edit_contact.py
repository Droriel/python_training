# -*- coding: utf-8 -*-
from random import randrange
import random
from model.contact import PersonalData, ContactBaseData
from test_addons import adjustments


# def test_edit_first_contact_top_upadate(app, json_contacts):
#     if app.contact.count() == 0:
#         app.contact.init_new_contact()
#         app.contact.fill_personal_data(PersonalData(firstname="test"))
#         app.contact.submit_contact()
#     old_contacts = app.contact.get_contact_list()
#     index = randrange(len(old_contacts))
#     app.contact.init_by_index_contact_edition(index)
#     contact = json_contacts
#     app.contact.fill_contact_base_data(contact.contactBaseData)
#     app.contact.fill_personal_data(contact.personalData)
#     app.contact.fill_phone_number(contact.phoneNumbers)
#     app.contact.fill_emails(contact.emails)
#     app.contact.fill_www_address(contact.www)
#     app.contact.update_birth_date(contact.birthDate)
#     app.contact.update_anniversary_date(contact.anniversaryDate)
#     app.contact.fill_additional_data(contact.additionalData)
#     app.contact.fill_notes(contact.notes)
#     app.contact.update_contact_top()
#     assert len(old_contacts) == app.contact.count()
#     new_contacts = app.contact.get_contact_list()
#     contact.contactBaseData.id = old_contacts[index].id
#     old_contacts[index] = contact.contactBaseData
#     assert sorted(old_contacts, key=ContactBaseData.id_or_max) == sorted(new_contacts, key=ContactBaseData.id_or_max)


def test_edit_first_contact_bottom_update(app, db,  check_ui, json_contacts):
    if app.contact.count() == 0:
        app.contact.init_new_contact()
        app.contact.fill_personal_data(PersonalData(firstname="test"))
        app.contact.submit_contact()
    old_contacts = db.get_contact_list()
    contact_to_edit = random.choice(old_contacts)
    contact = json_contacts
    contact.contactBaseData.id = contact_to_edit.contactBaseData.id
    app.contact.init_by_id_contact_edition(contact.contactBaseData.id)
    app.contact.fill_contact_base_data(contact.contactBaseData)
    app.contact.fill_personal_data(contact.personalData)
    app.contact.fill_phone_number(contact.phoneNumbers)
    app.contact.fill_emails(contact.emails)
    app.contact.fill_www_address(contact.www)
    app.contact.update_birth_date(contact.birthDate)
    app.contact.update_anniversary_date(contact.anniversaryDate)
    app.contact.fill_additional_data(contact.additionalData)
    app.contact.fill_notes(contact.notes)
    app.contact.update_contact_bottom()
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    # contact.contactBaseData.id = old_contacts[index].id
    # old_contacts[index] = contact.contactBaseData
    for i in range(len(old_contacts)):
        if old_contacts[i] == contact_to_edit:
            old_contacts[i] = contact
    assert new_contacts == old_contacts
    if check_ui:

        def clean(contact):
            return ContactBaseData(id=contact.contactBaseData.id,
                                   firstname=adjustments.clear_multiple_spaces(contact.contactBaseData.firstname).strip(),
                                   lastname=adjustments.clear_multiple_spaces(contact.contactBaseData.lastname).strip())
        clear_new_contacts = map(clean, new_contacts)
        assert sorted(clear_new_contacts, key=ContactBaseData.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                                   key=ContactBaseData.id_or_max)

