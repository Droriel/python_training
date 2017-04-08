# -*- coding: utf-8 -*-
from model.contact import PersonalData


def test_delete_all_contacts(app, db, check_ui):
    if app.contact.count() == 0:
        app.contact.init_new_contact()
        app.contact.fill_personal_data(PersonalData(firstname="test"))
        app.contact.submit_contact()
        app.contact.init_new_contact()
        app.contact.fill_personal_data(PersonalData(firstname="test2"))
        app.contact.submit_contact()
    app.contact.delete_all_contacts()
    app.contact.open_main_page()
    # new_contacts = app.contact.get_contact_list()  usuwam bo nie ma potrzeby wczytywać listy
    assert len(db.get_contact_list()) == 0
    if check_ui:
        assert app.contact.count() == 0
