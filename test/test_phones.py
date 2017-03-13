from re import sub
from model.contact import ContactBaseData, PhoneNumbers, AdditionalData


def test_phones_on_home_page(app):
    if app.contact.count() == 0:
        app.contact.init_new_contact()
        app.contact.fill_contact_base_data(ContactBaseData(firstname="test"))
        app.contact.fill_phone_number(
            PhoneNumbers(home='(+48)888-558-147', work='dgdfh'))
        app.contact.fill_additional_data(AdditionalData(phone='*$@'))
        app.contact.submit_contact()
    contactFromHomePage = app.contact.get_contact_list()[0]
    contactFromEditPage = app.contact.get_contact_info_from_edit_page(0)
    assert contactFromHomePage.allPhonesFromHomePage == merge_phones_like_on_home_page(contactFromEditPage)


def test_phones_on_view_page(app):
    if app.contact.count() == 0:
        app.contact.init_new_contact()
        app.contact.fill_contact_base_data(ContactBaseData(firstname="test"))
        app.contact.fill_phone_number(
            PhoneNumbers(home='(+48)888-558-147', work='dgdfh'))
        app.contact.fill_additional_data(AdditionalData(phone='*$@'))
        app.contact.submit_contact()
    contactFromHomePage = app.contact.get_contact_list()[0]
    contactFromViewPage = app.contact.get_contact_info_from_view_page(0)
    assert contactFromHomePage.allPhonesFromHomePage == merge_phones_like_on_home_page(contactFromViewPage)


def clear(s):
    return sub("[\s|\-|\(|\)]", '', s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != '',
                    map(lambda x: clear(x),
                        filter(lambda x: x is not None, [contact.homephone, contact.mobilephone, contact.workphone, contact.additionalphone]))))
