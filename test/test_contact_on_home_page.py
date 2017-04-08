# -*- coding: utf-8 -*-
from random import randrange
from re import sub
from model.contact import ContactBaseData, Emails, PersonalData, PhoneNumbers, AdditionalData, ContactAllData
from test_addons import adjustments


def test_contact_on_the_home_page_from_edit_page(app):
    if app.contact.count() == 0:
        app.contact.init_new_contact()
        app.contact.fill_contact_base_data(ContactBaseData(firstname="Testowe Imie", lastname='Testowe-Nazwisko'))
        app.contact.fill_emails(Emails(email1='ada1_ro@wp.pl', email3='bata01.alias.34@strona.info'))
        app.contact.fill_personal_data(PersonalData(address='ul. Wejhera 3/11/nGdansk 80-390'))
        app.contact.fill_phone_number(
            PhoneNumbers(home='(+48)888-558-147', work='dgdfh'))
        app.contact.fill_additional_data(AdditionalData(phone='*$@'))
        app.contact.submit_contact()
    contact_list = app.contact.get_contact_list()
    index = randrange(len(contact_list))
    contactFromHomePage = app.contact.get_contact_list()[index]
    contactFromEditPage = app.contact.get_contact_info_from_edit_page(index)
    assert contactFromHomePage.lastname == adjustments.clear_multiple_spaces(contactFromEditPage.lastname).strip()
    assert contactFromHomePage.firstname == adjustments.clear_multiple_spaces(contactFromEditPage.firstname).strip()
    assert contactFromHomePage.address == adjustments.clear_multiple_spaces(contactFromEditPage.address).strip()
    assert contactFromHomePage.allEmailsFromHomePage == merge_emails_like_on_home_page(contactFromEditPage).strip()
    assert contactFromHomePage.allPhonesFromHomePage == merge_phones_like_on_home_page(contactFromEditPage).strip()


def test_contact_on_the_home_page_from_db(app, db):
    if app.contact.count() == 0:
        app.contact.init_new_contact()
        app.contact.fill_contact_base_data(ContactBaseData(firstname="Testowe Imie", lastname='Testowe-Nazwisko'))
        app.contact.fill_emails(Emails(email1='ada1_ro@wp.pl', email3='bata01.alias.34@strona.info'))
        app.contact.fill_personal_data(PersonalData(address='ul. Wejhera 3/11/nGdansk 80-390'))
        app.contact.fill_phone_number(
            PhoneNumbers(home='(+48)888-558-147', work='dgdfh'))
        app.contact.fill_additional_data(AdditionalData(phone='*$@'))
        app.contact.submit_contact()
    contact_list_fromHomePage = app.contact.get_contact_list()
    contact_list_fromDB = db.get_contact_list()
    clear_contact_list_fromDB = map(clean, contact_list_fromDB)
    sorted_contact_list_fromHomePage = sorted(contact_list_fromHomePage, key=ContactBaseData.id_or_max)
    sorted_contact_list_fromDB = sorted(clear_contact_list_fromDB, key=ContactBaseData.id_or_max)
    assert sorted_contact_list_fromHomePage == sorted_contact_list_fromDB
    for contact in range(len(sorted_contact_list_fromDB)):
        assert sorted_contact_list_fromDB[contact].address == \
               adjustments.clear_multiple_spaces(sorted_contact_list_fromHomePage[contact].address)
        assert merge_emails_like_on_home_page(sorted_contact_list_fromDB[contact]).strip() == \
               sorted_contact_list_fromHomePage[contact].allEmailsFromHomePage
        assert merge_phones_like_on_home_page(sorted_contact_list_fromDB[contact]).strip() == \
               sorted_contact_list_fromHomePage[contact].allPhonesFromHomePage


def merge_emails_like_on_home_page(contact):
    return '\n'.join(filter(lambda x: x != '',
        (filter(lambda x: x is not None,([adjustments.clear_multiple_spaces(contact.email1), adjustments.clear_multiple_spaces(contact.email2), adjustments.clear_multiple_spaces(contact.email3)])))))

def clear(s):
    return sub("[\s|\-|\(|\)]", '', s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != '',
                    map(lambda x: clear(x),
                        filter(lambda x: x is not None, [contact.homephone, contact.mobilephone, contact.workphone, contact.additionalphone]))))


def clean(contact):
    return ContactBaseData(id=contact.contactBaseData.id,
                           firstname=adjustments.clear_multiple_spaces(contact.contactBaseData.firstname).strip(),
                           lastname=adjustments.clear_multiple_spaces(contact.contactBaseData.lastname).strip(),
                           address=adjustments.clear_multiple_spaces(contact.contactBaseData.address).strip(),
                           homephone=contact.contactBaseData.homephone,
                           mobilephone=contact.contactBaseData.mobilephone,
                           workphone=contact.contactBaseData.workphone,
                           additionalphone=contact.contactBaseData.additionalphone,
                           email1=contact.contactBaseData.email1.strip(),
                           email2=contact.contactBaseData.email2.strip(),
                           email3=contact.contactBaseData.email3.strip())

