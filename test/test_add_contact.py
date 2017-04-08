# -*- coding: utf-8 -*-

from model.contact import ContactBaseData, ContactAllData
from test_addons import adjustments


def test_add_contact(app, db, json_contacts, check_ui):
    old_contacts = db.get_contact_list()
    app.contact.init_new_contact()
    contact= json_contacts
    app.contact.fill_contact_base_data(contact.contactBaseData)
    app.contact.fill_personal_data(contact.personalData)
    app.contact.fill_phone_number(contact.phoneNumbers)
    app.contact.fill_emails(contact.emails)
    app.contact.fill_www_address(contact.www)
    app.contact.fill_birth_date(contact.birthDate)
    app.contact.fill_anniversary_date(contact.anniversaryDate)
    app.contact.fill_additional_data(contact.additionalData)
    app.contact.fill_notes(contact.notes)
    app.contact.submit_contact()
    new_contacts = db.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    # app.contact.get_contact_list()
    # old_contacts.append(json_contacts.contactBaseData)
    old_contacts.append(contact)
    assert new_contacts == old_contacts
    # assert sorted(new_contacts, key=ContactBaseData.id_or_max) == sorted(old_contacts, key=ContactBaseData.id_or_max)
    if check_ui:

        def clean(contact):
            return ContactBaseData(id=contact.contactBaseData.id,
                                   firstname=adjustments.clear_multiple_spaces(contact.contactBaseData.firstname).strip(),
                                   lastname=adjustments.clear_multiple_spaces(contact.contactBaseData.lastname).strip())
        clear_new_contacts = map(clean, new_contacts)
        assert sorted(clear_new_contacts, key=ContactBaseData.id_or_max) == sorted(app.contact.get_contact_list(), key=ContactBaseData.id_or_max)

