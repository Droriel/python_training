# -*- coding: utf-8 -*-

from model.contact import ContactBaseData


def test_add_contact(app, json_contacts):
    old_contacts = app.contact.get_contact_list()
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
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(json_contacts.contactBaseData)
    assert sorted(new_contacts, key=ContactBaseData.id_or_max) == sorted(old_contacts, key=ContactBaseData.id_or_max)

