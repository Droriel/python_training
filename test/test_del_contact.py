# -*- coding: utf-8 -*-
from model.contact import PersonalData


def test_del_contact_from_the_list(app):
    if app.contact.count() == 0:
        app.contact.init_new_contact()
        app.contact.fill_personal_data(PersonalData(firstname="test"))
        app.contact.submit_contact()
    app.contact.delete_first_contact()


def test_del_edited_contact(app):
    if app.contact.count() == 0:
        app.contact.init_new_contact()
        app.contact.fill_personal_data(PersonalData(firstname="test"))
        app.contact.submit_contact()
    app.contact.init_first_contact_edition()
    app.contact.delete_edited_contact()
