import re
from model.contact import ContactBaseData,Emails


def test_emails_on_home_page(app):
    if app.contact.count() == 0:
        app.contact.init_new_contact()
        app.contact.fill_contact_base_data(ContactBaseData(firstname="test"))
        app.contact.fill_emails(Emails(email1='ada1_ro@wp.pl', email3='bata01.alias.34@strona.info'))
        app.contact.submit_contact()
    contactFromHomePage = app.contact.get_contact_list()[0]
    contactFromEditPage = app.contact.get_contact_info_from_edit_page(0)
    assert contactFromHomePage.allEmailsFromHomePage == merge_emails_like_on_home_page(contactFromEditPage)


def test_emails_on_view_page(app):
    if app.contact.count() == 0:
        app.contact.init_new_contact()
        app.contact.fill_contact_base_data(ContactBaseData(firstname="test", email1='ada1_ro@wp.pl', email3='bata01.alias.34@strona.info'))
        app.contact.submit_contact()
    contactFromHomePage = app.contact.get_contact_list()[0]
    contactFromViewPage = app.contact.get_contact_info_from_view_page(0)
    assert contactFromHomePage.allEmailsFromHomePage == merge_emails_like_on_home_page_from_all_emails(contactFromViewPage)
    # assert contactFromHomePage.allEmailsFromHomePage == contactFromViewPage


def merge_emails_like_on_home_page(contact):
    return '\n'.join(filter(lambda x: x != '',
        (filter(lambda x: x is not None,([contact.email1, contact.email2, contact.email3])))))

def merge_emails_like_on_home_page_from_all_emails(contact):
    return '\n'.join(filter(lambda x: x != '',
        (filter(lambda x: x is not None,(contact.allEmailsFromHomePage)))))
