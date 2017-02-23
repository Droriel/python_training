# -*- coding: utf-8 -*-


def test_del_contact_from_the_list(app):
    app.session.login(username="admin", password="secret")
    app.contact.delete_first_contact()
    app.session.logout()


def test_del_edited_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.init_first_contact_edition()
    app.contact.delete_edited_contact()
    app.session.logout()