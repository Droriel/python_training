# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest
from contact import PersonalData, PhoneNumbers, Emails, Wwww, AdditionalData, Notes


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


class test_add_contact(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_add_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.init_new_contact(wd)
        self.fill_personal_data(wd, PersonalData(firstname="Imię", middlename="Drugie", lastname="Nazwisko2",
                                                 nickname="Nick",title="tytuł", company="Firma", address="Adres"))
        self.fill_phone_number(wd, PhoneNumbers(home="111111111", mobile="222222222", work="333333333",
                                                fax="444444444"))
        self.fill_emails(wd, Emails(email1="test1@test.pl", email2="test2@test.pl", email3="test3@test.pl"))
        self.fill_www_address(wd, Wwww(www="www.test.pl"))
        # For dates parameters are day, month written in number, year str - number with""
        self.fill_birth_date(wd, day=28, month=2, year="2010")
        self.fill_anniversary_date(wd, day=31, month=12, year="2010")
        self.fill_additonal_data(wd, AdditionalData(address="ul. Ulica 1/1 \nMiasto 00-111", phone="888888888"))
        self.fill_notes(wd, Notes(notes="To są uwagi."))
        self.submit_contact(wd)
        self.logout(wd)

    def test_add_empty_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.init_new_contact(wd)
        self.fill_personal_data(wd, PersonalData(firstname="", middlename="", lastname="", nickname="",
                           title="", company="", address=""))
        self.fill_phone_number(wd, PhoneNumbers(home="", mobile="", work="", fax=""))
        self.fill_emails(wd, Emails(email1="", email2="", email3=""))
        self.fill_www_address(wd, Wwww(www=""))
        # For dates parameters are day, month written in number, year str - number with""
        self.fill_birth_date(wd, day=-1, month=0, year="")
        self.fill_anniversary_date(wd, day=-1, month=0, year="")
        self.fill_additonal_data(wd, AdditionalData(address="", phone=""))
        self.fill_notes(wd, Notes(notes=""))
        self.submit_contact(wd)
        self.logout(wd)

    def test_add_contact_with_empty_addresses_phones(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.init_new_contact(wd)
        self.fill_personal_data(wd, PersonalData(firstname="Anna", middlename="Janina", lastname="Kowalska",
                                                 nickname="Anka",
                           title="Dr", company="NZOZ Sierakowice", address=""))
        self.fill_phone_number(wd, PhoneNumbers(home="", mobile="", work="", fax=""))
        self.fill_emails(wd, Emails(email1="", email2="", email3=""))
        self.fill_www_address(wd, Wwww(www=""))
        # For dates parameters are day, month written in number, year str - number with""
        self.fill_birth_date(wd, day=1, month=1, year="1990")
        self.fill_anniversary_date(wd, day=31, month=12, year="2012")
        self.fill_additonal_data(wd, AdditionalData(address="", phone=""))
        self.fill_notes(wd, Notes(notes="To są uwagi. Nowe uwagi."))
        self.submit_contact(wd)
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_link_text("Wyloguj się").click()

    def submit_contact(self, wd):
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def fill_notes(self, wd, notes):
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(notes.notes)

    def fill_additonal_data(self, wd, additionalData):
        # Fill second address and phone
        # Fill in second address
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(additionalData.address)
        # Fill in "Prywatny" phone
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(additionalData.phone)

    def fill_anniversary_date(self, wd, day, month, year):
        # Choose in day
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[%s]" % str(day+2)).is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[%s]" % str(day+2)).click()
        # Choose in month
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[%s]" % str(month+1)).is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[%s]" % str(month+1)).click()
        # Fill in year
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(year)

    def fill_birth_date(self, wd, day, month, year):
        # Choose in day
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[%s]" % str(day+2)).is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[%s]" % str(day+2)).click()
        # Choose in month
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[%s]" % str(month+1)).is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[%s]" % str(month+1)).click()
        # Fill in year
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(year)

    def fill_www_address(self, wd, www):
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(www.www)

    def fill_emails(self, wd, emails):
        # Fill in first e-mail addresses
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(emails.email1)
        # Fill in second e-mail addresses
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(emails.email2)
        # Fill in third e-mail addresses
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(emails.email3)

    def fill_phone_number(self, wd, phoneNumbers):
        # Fill in home number
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(phoneNumbers.home)
        # Fill in mobile number
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(phoneNumbers.mobile)
        # Fill in work number
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(phoneNumbers.work)
        # Fill in fax number
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(phoneNumbers.fax)

    def fill_personal_data(self, wd, personalData):
        # Fill in first name
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(personalData.firstname)
        # Fill in middle name
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(personalData.middlename)
        # Fill in last name
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(personalData.lastname)
        # Fill in nickname
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(personalData.nickname)
        # Add photo
        # wd.find_element_by_name("photo").click()
        # Add title
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(personalData.title)
        # Add company name
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(personalData.company)
        # Add address
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(personalData.address)

    def init_new_contact(self, wd):
        wd.find_element_by_link_text("nowy wpis").click()

    def login(self, wd, username, password):
        # Fill in username
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        # Fill in password
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/edit.php")

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
