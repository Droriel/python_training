# -*- coding: utf-8 -*-
import pytest
from contact import PersonalData, PhoneNumbers, Emails, Wwww, AdditionalData, Notes
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.init_new_contact()
    app.fill_personal_data(PersonalData(firstname="Imię", middlename="Drugie", lastname="Nazwisko2",
                                                 nickname="Nick",title="tytuł", company="Firma", address="Adres"))
    app.fill_phone_number(PhoneNumbers(home="111111111", mobile="222222222", work="333333333",
                                                fax="444444444"))
    app.fill_emails(Emails(email1="test1@test.pl", email2="test2@test.pl", email3="test3@test.pl"))
    app.fill_www_address(Wwww(www="www.test.pl"))
    # For dates parameters are day, month written in number, year str - number with""
    app.fill_birth_date(day=28, month=2, year="2010")
    app.fill_anniversary_date(day=31, month=12, year="2010")
    app.fill_additonal_data(AdditionalData(address="ul. Ulica 1/1 \nMiasto 00-111", phone="888888888"))
    app.fill_notes(Notes(notes="To są uwagi."))
    app.submit_contact()
    app.logout()


def test_add_empty_contact(app):
    app.login(username="admin", password="secret")
    app.init_new_contact()
    app.fill_personal_data(PersonalData(firstname="", middlename="", lastname="", nickname="",
                           title="", company="", address=""))
    app.fill_phone_number(PhoneNumbers(home="", mobile="", work="", fax=""))
    app.fill_emails(Emails(email1="", email2="", email3=""))
    app.fill_www_address(Wwww(www=""))
    # For dates parameters are day, month written in number, year str - number with""
    app.fill_birth_date(day=-1, month=0, year="")
    app.fill_anniversary_date(day=-1, month=0, year="")
    app.fill_additonal_data(AdditionalData(address="", phone=""))
    app.fill_notes(Notes(notes=""))
    app.submit_contact()
    app.logout()


def test_add_contact_with_empty_addresses_phones(app):
    app.login(username="admin", password="secret")
    app.init_new_contact()
    app.fill_personal_data(PersonalData(firstname="Anna", middlename="Janina", lastname="Kowalska",
                                                 nickname="Anka",
                           title="Dr", company="NZOZ Sierakowice", address=""))
    app.fill_phone_number(PhoneNumbers(home="", mobile="", work="", fax=""))
    app.fill_emails(Emails(email1="", email2="", email3=""))
    app.fill_www_address(Wwww(www=""))
    # For dates parameters are day, month written in number, year str - number with""
    app.fill_birth_date(day=1, month=1, year="1990")
    app.fill_anniversary_date(day=31, month=12, year="2012")
    app.fill_additonal_data(AdditionalData(address="", phone=""))
    app.fill_notes(Notes(notes="To są uwagi. Nowe uwagi."))
    app.submit_contact()
    app.logout()

