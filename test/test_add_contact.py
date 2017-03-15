# -*- coding: utf-8 -*-
import pytest

from model.contact import PersonalData, PhoneNumbers, Emails, Www, AdditionalData, Notes, ContactBaseData, \
    ContactAllData
import random
import string


def random_string(maxlen):
    symbols = string.ascii_letters + ' '*10 + '-'*3+ '_'*3
    #                      + "'"*3
    return ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_string_with_new_line(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + ' '*10 + '\n' + '-'*3+ '_'*3
    #  + string.punctuation
    return prefix + ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])

# def random_email(maxlen):
#     symbols = string.ascii_letters + ' ' * 10 + '-' * 3 + "'" * 3 + '_' * 3
#     return ''.join([random.choice(symbols) for i in range(random.randrange(maxlen+5))]) + '@' +\
#            ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))]) + '.' +\
#            ''.join([random.choice(string.ascii_letters) for i in range(random.randrange(2-4))])
#
# def random_phone_number (maxlen):
#     symbols = str(string.digits) * 4  + '('+ ')' + '+' + '-' + ' '
#     return ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testData = [ContactAllData(contactBaseData=ContactBaseData, personalData=PersonalData, phoneNumbers=PhoneNumbers,
                           emails=Emails, www=Www, additionalData=AdditionalData, notes=Notes)
            for ContactBaseData.firstname in ('', random_string(10))
            for ContactBaseData.lastname in ('', random_string(18))
            for PersonalData.middlename in ('', random_string(10))
            for PersonalData.nickname in ('', random_string(10))
            for PersonalData.title in  ('', random_string(10))
            for PersonalData.company in ('', random_string(20))
            for PersonalData.address in ('', random_string_with_new_line('Adres pdstawowy: ', 30))
            ]

# testBaseData = [ContactBaseData(firstname=firstname, lastname=lastname)
#                 for firstname in ('', random_string(10))
#                 for lastname in ('', random_string(18))]
# testPersonalData = [PersonalData(middlename=middlename, nickname=nickname,title=title, company=company,
#                                                 address=address)
#                     for middlename in ('', random_string(10))
#                     for nickname in ('', random_string(10))
#                     for title in  ('', random_string(10))
#                     for company in ('', random_string(20))
#                     for address in ('', random_string_with_new_line('Adres pdstawowy: ', 30))]
# testPhoneNumbers = [PhoneNumbers(home=home, mobile=mobile, work=work,
#                                                 fax=fax)
#                     for home in ('', random_phone_number(16))
#                     for mobile in ('', random_phone_number(16))
#                     for work in ('', random_phone_number(16))
#                     for fax in ('', random_phone_number(16))]
# testEmails = [Emails(email1=email1, email2=email2, email3=email3)
#               for email1 in ('', random_phone_number(8))
#               for email2 in ('', random_phone_number(8))
#               for email3 in ('', random_phone_number(8))]
# testWwww = []
# testDay = []
# testMonth =[]
# testYear = []
# testNotes = []


@pytest.mark.parametrize('contact', testData, ids=[repr(x) for x in testData])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.init_new_contact()
    # contact= testData
    app.contact.fill_contact_base_data(contact.ContactBaseData)
    app.contact.fill_personal_data(contact.PersonalData)
                                   # PersonalData(middlename="Drugie", nickname="Nick",title="tytuł", company="Firma",
                                   #              address="Adres"))
    app.contact.fill_phone_number(PhoneNumbers(home="111111111", mobile="222222222", work="333333333",
                                                fax="444444444"))
    app.contact.fill_emails(Emails(email1="test1@test.pl", email2="test2@test.pl", email3="test3@test.pl"))
    app.contact.fill_www_address(Www(www="www.test.pl"))
    # For dates parameters are day, month written in number, year str - number with""
    app.contact.fill_birth_date(day=28, month=2, year="2010")
    app.contact.fill_anniversary_date(day=31, month=12, year="2010")
    app.contact.fill_additional_data(AdditionalData(address="ul. Ulica 1/1 \nMiasto 00-111", phone="888888888"))
    app.contact.fill_notes(Notes(notes="To są uwagi."))
    app.contact.submit_contact()
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact.ContactBaseData)
    assert sorted(new_contacts, key=contact.ContactBaseData.id_or_max) == sorted(old_contacts, key=contact.ContactBaseData.id_or_max)


def test_add_empty_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.init_new_contact()
    contact = ContactBaseData(firstname="", lastname="")
    app.contact.fill_contact_base_data(contact)
    app.contact.fill_personal_data(PersonalData(middlename="", nickname="", title="", company="", address=""))
    app.contact.fill_phone_number(PhoneNumbers(home="", mobile="", work="", fax=""))
    app.contact.fill_emails(Emails(email1="", email2="", email3=""))
    app.contact.fill_www_address(Www(www=""))
    # For dates parameters are day, month written in number, year str - number with""
    app.contact.fill_birth_date(day=-1, month=0, year="")
    app.contact.fill_anniversary_date(day=-1, month=0, year="")
    app.contact.fill_additional_data(AdditionalData(address="", phone=""))
    app.contact.fill_notes(Notes(notes=""))
    app.contact.submit_contact()
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
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
    app.contact.fill_www_address(Www(www=""))
    # For dates parameters are day, month written in number, year str - number with""
    app.contact.fill_birth_date(day=1, month=1, year="1990")
    app.contact.fill_anniversary_date(day=31, month=12, year="2012")
    app.contact.fill_additional_data(AdditionalData(address="", phone=""))
    app.contact.fill_notes(Notes(notes="To są uwagi. Nowe uwagi."))
    app.contact.submit_contact()
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(new_contacts, key=ContactBaseData.id_or_max) == sorted(old_contacts, key=ContactBaseData.id_or_max)
