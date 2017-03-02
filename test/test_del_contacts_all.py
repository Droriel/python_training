# -*- coding: utf-8 -*-
from model.contact import PersonalData


def test_delete_all_contacts(app):
    if app.contact.count() == 0:
        app.contact.init_new_contact()
        app.contact.fill_personal_data(PersonalData(firstname="test"))
        app.contact.submit_contact()
        app.contact.init_new_contact()
        app.contact.fill_personal_data(PersonalData(firstname="test2"))
        app.contact.submit_contact()
    app.contact.delete_all_contacts()
