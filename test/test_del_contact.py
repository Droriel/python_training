# -*- coding: utf-8 -*-


def test_del_contact_from_the_list(app):
    app.contact.delete_first_contact()


def test_del_edited_contact(app):
    app.contact.init_first_contact_edition()
    app.contact.delete_edited_contact()
