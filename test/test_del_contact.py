# -*- coding: utf-8 -*-
from random import randrange
from model.contact import PersonalData


def test_del_contact_from_the_list(app):
    if app.contact.count() == 0:
        app.contact.init_new_contact()
        app.contact.fill_personal_data(PersonalData(firstname="test"))
        app.contact.submit_contact()
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index:index+1] = []
    assert new_contacts == old_contacts


def test_del_edited_contact(app):
    if app.contact.count() == 0:
        app.contact.init_new_contact()
        app.contact.fill_personal_data(PersonalData(firstname="test"))
        app.contact.submit_contact()
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.init_by_index_contact_edition(index)
    app.contact.delete_edited_contact()
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index:index+1] = []
    assert new_contacts == old_contacts