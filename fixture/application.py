# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper


class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()

    # additional methods -adding contact
    def submit_contact(self):
        wd = self.wd
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def fill_notes(self, notes):
        wd = self.wd
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(notes.notes)

    def fill_additonal_data(self, additionalData):
        wd = self.wd
        # Fill second address and phone
        # Fill in second address
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(additionalData.address)
        # Fill in "Prywatny" phone
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(additionalData.phone)

    def fill_anniversary_date(self, day, month, year):
        wd = self.wd
        # Choose in day
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[%s]" % str(day + 2)).is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[%s]" % str(day + 2)).click()
        # Choose in month
        if not wd.find_element_by_xpath(
                        "//div[@id='content']/form/select[4]//option[%s]" % str(month + 1)).is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[%s]" % str(month + 1)).click()
        # Fill in year
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(year)

    def fill_birth_date(self, day, month, year):
        wd = self.wd
        # Choose in day
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[%s]" % str(day + 2)).is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[%s]" % str(day + 2)).click()
        # Choose in month
        if not wd.find_element_by_xpath(
                        "//div[@id='content']/form/select[2]//option[%s]" % str(month + 1)).is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[%s]" % str(month + 1)).click()
        # Fill in year
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(year)

    def fill_www_address(self, www):
        wd = self.wd
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(www.www)

    def fill_emails(self, emails):
        wd = self.wd
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

    def fill_phone_number(self, phoneNumbers):
        wd = self.wd
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

    def fill_personal_data(self, personalData):
        wd = self.wd
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

    def init_new_contact(self):
        wd = self.wd
        wd.find_element_by_link_text("nowy wpis").click()