# -*- coding: utf-8 -*-
import pytest

from model.contact import PersonalData, PhoneNumbers, Emails, Www, AdditionalData, Notes, ContactBaseData, \
    ContactAllData
import random
import string


def random_string(maxlen):
    symbols = string.ascii_letters + ' '*13 + '-'*3 + '_'*3
    #                      + "'"*3
    return ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_string_with_new_line(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + ' '*15 + '\n'*5 + '-'*3 + '_'*3
    #  + string.punctuation
    return prefix + ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_email(maxlen):
    symbols = string.ascii_letters + ' ' * 10 + '-' * 3 + '_' * 3
    return ''.join([random.choice(symbols) for i in range(random.randrange(maxlen+5))]) + '@' +\
           ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))]) + '.' +\
           ''.join([random.choice(string.ascii_letters) for i in range(random.randrange(2,4))])


def random_phone_number(maxlen):
    symbols = str(string.digits) * 4  + '('+ ')' + '+' + '-' + ' '
    return ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_www(maxlen):
    symbols = string.ascii_letters + '-'
    return  'www.' + ''.join([random.choice(symbols)  for i in range(random.randrange(maxlen))]) + '.'+\
           ''.join([random.choice(string.ascii_letters) for i in range(random.randrange(2,4))])

testData = [ContactAllData(contactBaseData=ContactBaseData(firstname=random_string(10), lastname=random_string(18)),
                           personalData=PersonalData(middlename=random_string(10), nickname=random_string(10),
                                                     title=random_string(10), company=random_string(20),
                                                     address=random_string_with_new_line('Adres podstawowy: ', 30)),
                           phoneNumbers=PhoneNumbers(home=random_phone_number(12), mobile=random_phone_number(16),
                                                     work=random_phone_number(12), fax=random_phone_number(10)),
                           emails=Emails(email1=random_email(8), email2=random_email(5), email3=random_email(6)),
                           www=Www(www=random_www(30)),
                           additionalData=AdditionalData(address=random_string_with_new_line('Adres dodatkowy: ', 30) ,
                                                         phone=random_phone_number(12)),
                           notes=Notes(notes=random_string_with_new_line('n', 100)))]\
           + \
           [ContactAllData(contactBaseData=ContactBaseData(firstname='', lastname=''),
                           personalData=PersonalData(middlename='', nickname='',
                                                     title='', company='',
                                                     address=''),
                           phoneNumbers=PhoneNumbers(home='', mobile='',
                                                     work='', fax=''),
                           emails=Emails(email1='', email2='', email3=''),
                           www=Www(www=''),
                           additionalData=AdditionalData(address='' ,
                                                         phone=''),
                           notes=Notes(notes=''))]\
           +\
           [ContactAllData(contactBaseData=ContactBaseData(firstname=random_string(10), lastname=random_string(18)),
                           personalData=PersonalData(middlename=random_string(10), nickname=random_string(10),
                                                     title=random_string(10), company=random_string(20),
                                                     address=''),
                           phoneNumbers=PhoneNumbers(home='', mobile='',
                                                     work='', fax=''),
                           emails=Emails(email1='', email2='', email3=''),
                           www=Www(www=''),
                           additionalData=AdditionalData(address='',
                                                         phone=''),
                           notes=Notes(notes=random_string_with_new_line('n', 100)))]\
        + \
            [ContactAllData(contactBaseData=ContactBaseData(firstname=' a ', lastname=' b '),
                            personalData=PersonalData(middlename='', nickname='',
                                                      title='', company='',
                                                      address=''),
                            phoneNumbers=PhoneNumbers(home='', mobile='',
                                                      work='', fax=''),
                            emails=Emails(email1='', email2='', email3=''),
                            www=Www(www=''),
                            additionalData=AdditionalData(address='',
                                                          phone=''),
                            notes=Notes(notes=''))] \
        + \
        [ContactAllData(contactBaseData=ContactBaseData(firstname='a  b', lastname='c  d'),
                        personalData=PersonalData(middlename='', nickname='',
                                                  title='', company='',
                                                  address=''),
                        phoneNumbers=PhoneNumbers(home='', mobile='',
                                                  work='', fax=''),
                        emails=Emails(email1='', email2='', email3=''),
                        www=Www(www=''),
                        additionalData=AdditionalData(address='',
                                                      phone=''),
                        notes=Notes(notes=''))] \

            # testDay = []
# testMonth =[]
# testYear = []

@pytest.mark.parametrize('contact', testData, ids=[repr(x) for x in testData])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.init_new_contact()
    # contact= testData
    app.contact.fill_contact_base_data(contact.contactBaseData)
    app.contact.fill_personal_data(contact.personalData)
    app.contact.fill_phone_number(contact.phoneNumbers)
    app.contact.fill_emails(contact.emails)
    app.contact.fill_www_address(contact.www)
    # For dates parameters are day, month written in number, year str - number with""
    app.contact.fill_birth_date(day=28, month=2, year="2010")
    app.contact.fill_anniversary_date(day=31, month=12, year="2010")
    app.contact.fill_additional_data(contact.additionalData)
    app.contact.fill_notes(contact.notes)
    app.contact.submit_contact()
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact.contactBaseData)
    assert sorted(new_contacts, key=ContactBaseData.id_or_max) == sorted(old_contacts, key=ContactBaseData.id_or_max)


# def test_add_contact_with_empty_addresses_phones(app):
#     old_contacts = app.contact.get_contact_list()
#     app.contact.init_new_contact()
#     contact = ContactBaseData(firstname="Anna", lastname="Kowalska")
#     app.contact.fill_contact_base_data(contact)
#     app.contact.fill_personal_data(PersonalData(middlename="Janina", nickname="Anka", title="Dr",
#                                                 company="NZOZ Sierakowice", address=""))
#     app.contact.fill_phone_number(PhoneNumbers(home="", mobile="", work="", fax=""))
#     app.contact.fill_emails(Emails(email1="", email2="", email3=""))
#     app.contact.fill_www_address(Www(www=""))
#     # For dates parameters are day, month written in number, year str - number with""
#     app.contact.fill_birth_date(day=1, month=1, year="1990")
#     app.contact.fill_anniversary_date(day=31, month=12, year="2012")
#     app.contact.fill_additional_data(AdditionalData(address="", phone=""))
#     app.contact.fill_notes(Notes(notes="To są uwagi. Nowe uwagi."))
#     app.contact.submit_contact()
#     assert len(old_contacts) + 1 == app.contact.count()
#     new_contacts = app.contact.get_contact_list()
#     old_contacts.append(contact)
#     assert sorted(new_contacts, key=ContactBaseData.id_or_max) == sorted(old_contacts, key=ContactBaseData.id_or_max)
