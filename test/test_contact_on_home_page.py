from random import randrange
from re import sub
from model.contact import ContactBaseData, Emails, PersonalData, PhoneNumbers, AdditionalData


def test_contact_on_the_home_page_from_edit_page(app):
    if app.contact.count() == 0:
        app.contact.init_new_contact()
        app.contact.fill_contact_base_data(ContactBaseData(firstname="Testowe Imie", lastname='Testowe-Nazwisko'))
        app.contact.fill_emails(Emails(email1='ada1_ro@wp.pl', email3='bata01.alias.34@strona.info'))
        app.contact.fill_personal_data(PersonalData(address='ul. Wejhera 3/11/nGdansk 80-390'))
        app.contact.fill_phone_number(
            PhoneNumbers(home='(+48)888-558-147', work='dgdfh'))
        app.contact.fill_additional_data(AdditionalData(phone='*$@'))
        app.contact.submit_contact()
    contact_list = app.contact.get_contact_list()
    index = randrange(len(contact_list))
    contactFromHomePage = app.contact.get_contact_list()[index]
    contactFromEditPage = app.contact.get_contact_info_from_edit_page(index)
    assert contactFromHomePage.lastname == contactFromEditPage.lastname
    assert contactFromHomePage.firstname == contactFromEditPage.firstname
    assert contactFromHomePage.address == contactFromEditPage.address
    assert contactFromHomePage.allEmailsFromHomePage == merge_emails_like_on_home_page(contactFromEditPage)
    assert contactFromHomePage.allPhonesFromHomePage == merge_phones_like_on_home_page(contactFromEditPage)


def merge_emails_like_on_home_page(contact):
    return '\n'.join(filter(lambda x: x != '',
        (filter(lambda x: x is not None,([contact.email1, contact.email2, contact.email3])))))

def clear(s):
    return sub("[\s|\-|\(|\)]", '', s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != '',
                    map(lambda x: clear(x),
                        filter(lambda x: x is not None, [contact.homephone, contact.mobilephone, contact.workphone, contact.additionalphone]))))