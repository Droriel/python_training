# -*- coding: utf-8 -*-
from model.contact import PersonalData, PhoneNumbers, Emails, Wwww, AdditionalData, Notes, ContactBaseData


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.init_new_contact()
    contact = ContactBaseData(firstname="Imię",lastname="Nazwisko2")
    app.contact.fill_contact_base_data(contact)
    app.contact.fill_personal_data(PersonalData(middlename="Drugie", nickname="Nick",title="tytuł", company="Firma",
                                                address="Adres"))
    app.contact.fill_phone_number(PhoneNumbers(home="111111111", mobile="222222222", work="333333333",
                                                fax="444444444"))
    app.contact.fill_emails(Emails(email1="test1@test.pl", email2="test2@test.pl", email3="test3@test.pl"))
    app.contact.fill_www_address(Wwww(www="www.test.pl"))
    # For dates parameters are day, month written in number, year str - number with""
    app.contact.fill_birth_date(day=28, month=2, year="2010")
    app.contact.fill_anniversary_date(day=31, month=12, year="2010")
    app.contact.fill_additional_data(AdditionalData(address="ul. Ulica 1/1 \nMiasto 00-111", phone="888888888"))
    app.contact.fill_notes(Notes(notes="To są uwagi."))
    app.contact.submit_contact()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(new_contacts, key=ContactBaseData.id_or_max) == sorted(old_contacts, key=ContactBaseData.id_or_max)


def test_add_empty_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.init_new_contact()
    contact = ContactBaseData(firstname="", lastname="")
    app.contact.fill_contact_base_data(contact)
    app.contact.fill_personal_data(PersonalData(middlename="", nickname="", title="", company="", address=""))
    app.contact.fill_phone_number(PhoneNumbers(home="", mobile="", work="", fax=""))
    app.contact.fill_emails(Emails(email1="", email2="", email3=""))
    app.contact.fill_www_address(Wwww(www=""))
    # For dates parameters are day, month written in number, year str - number with""
    app.contact.fill_birth_date(day=-1, month=0, year="")
    app.contact.fill_anniversary_date(day=-1, month=0, year="")
    app.contact.fill_additional_data(AdditionalData(address="", phone=""))
    app.contact.fill_notes(Notes(notes=""))
    app.contact.submit_contact()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(new_contacts, key=ContactBaseData.id_or_max) == sorted(old_contacts, key=ContactBaseData.id_or_max)


def test_add_contact_with_empty_addresses_phones(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.init_new_contact()
    contact = ContactBaseData(firstname="Anna", lastname="Kowalska")
    app.contact.fill_contact_base_data(contact)
    app.contact.fill_personal_data(PersonalData(middlename="Janina", nickname="Anka", title="Dr",
                                                company="NZOZ Sierakowice", address=""))
    app.contact.fill_phone_number(PhoneNumbers(home="", mobile="", work="", fax=""))
    app.contact.fill_emails(Emails(email1="", email2="", email3=""))
    app.contact.fill_www_address(Wwww(www=""))
    # For dates parameters are day, month written in number, year str - number with""
    app.contact.fill_birth_date(day=1, month=1, year="1990")
    app.contact.fill_anniversary_date(day=31, month=12, year="2012")
    app.contact.fill_additional_data(AdditionalData(address="", phone=""))
    app.contact.fill_notes(Notes(notes="To są uwagi. Nowe uwagi."))
    app.contact.submit_contact()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(new_contacts, key=ContactBaseData.id_or_max) == sorted(old_contacts, key=ContactBaseData.id_or_max)
