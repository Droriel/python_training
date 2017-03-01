# -*- coding: utf-8 -*-
from model.contact import PersonalData, PhoneNumbers, Emails, Wwww, AdditionalData, Notes


def test_edit_first_contact_top_upadate(app):
    app.contact.init_first_contact_edition()
    app.contact.fill_personal_data(PersonalData(firstname="ImięInne", middlename="DrugieInne", lastname="NazwiskoInne",
                                                nickname="NickInny", title="tytułInny", company="FirmaInna", address="AdresInny"))
    app.contact.fill_phone_number(PhoneNumbers(home="999999999", mobile="888888888", work="777777777",
                                               fax="444444445"))
    app.contact.fill_emails(Emails(email1="test1inny@test.pl", email2="test2inny@test.pl", email3="test3inny@test.pl"))
    app.contact.fill_www_address(Wwww(www="www.testinny.pl"))
    # For dates parameters are day, month written in number +1 e.g. February: month=2+1, year str - number with""
    app.contact.fill_birth_date(day=13, month=8+1, year="2002")
    app.contact.fill_anniversary_date(day=5, month=3+1, year="2015")
    app.contact.fill_additional_data(AdditionalData(address="ul. Inna 1/1 \nMiasto Inne 09-911", phone="1111111111"))
    app.contact.fill_notes(Notes(notes="To są  Zmienione uwagi."))
    app.contact.update_contact_top()


def test_edit_first_contact_bottom_upadate(app):
    app.contact.init_first_contact_edition()
    app.contact.fill_personal_data(PersonalData(firstname="ImięInne2", middlename="DrugieInne2", lastname="NazwiskoInne2",
                                                nickname="NickInny2", title="tytułInny2", company="FirmaInna2", address="AdresInny2"))
    app.contact.fill_phone_number(PhoneNumbers(home="9999999992", mobile="8888888882", work="7777777772",
                                               fax="4444444452"))
    app.contact.fill_emails(Emails(email1="test1inny2@test.pl", email2="test2inny22@test.pl", email3="test3inny@test.pl"))
    app.contact.fill_www_address(Wwww(www="www.testinny2.pl"))
    # For dates parameters are day, month written in number +1 e.g. February: month=2+1, year str - number with""
    app.contact.fill_birth_date(day=11, month=9, year="2004")
    app.contact.fill_anniversary_date(day=9, month=2, year="2011")
    app.contact.fill_additional_data(AdditionalData(address="ul. Inna 21/1 \nMiasto Inne 29-911", phone="1111111112"))
    app.contact.fill_notes(Notes(notes="To są  Zmienione uwagi. 2"))
    app.contact.update_contact_bottom()


def test_edit_first_contact_partial(app):
    app.contact.init_first_contact_edition()
    app.contact.fill_personal_data(PersonalData(lastname="NazwiskoInne3",
                                                nickname="NickInny3"))
    app.contact.fill_phone_number(PhoneNumbers(home="", mobile="8888888883"))
    app.contact.fill_emails(Emails(email2="test2inny3@test.pl", email3=""))
    app.contact.fill_www_address(Wwww(www="www.testinny2.pl"))
    # For dates parameters are day, month written in number +1 e.g. February: month=2+1, year str - number with""
    app.contact.fill_birth_date(day=3, month=2+1, year="2003")
    app.contact.fill_anniversary_date(day=4, month=4+1, year="2004")
    app.contact.fill_additional_data(AdditionalData(phone="1111111113"))
    app.contact.fill_notes(Notes(notes="To są  Zmienione uwagi. 3"))
    app.contact.update_contact_bottom()
