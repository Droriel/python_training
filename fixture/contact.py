# -*- coding: utf-8 -*-
class  ContactHelper:

    def __init__(self, app):
        self.app = app

# additional methods -adding contact
    def submit_contact(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def fill_notes(self, notes):
        wd = self.app.wd
        self.app.change_field_value("notes", notes.notes)

    def fill_additional_data(self, additionalData):
        wd = self.app.wd
        # Fill second address and phone
        # Fill in second address
        self.app.change_field_value("address2", additionalData.address)
        # Fill in "Prywatny" phone
        self.app.change_field_value("phone2", additionalData.phone)

    def fill_anniversary_date(self, day, month, year):
        wd = self.app.wd
        # Choose in day
        if not wd.find_element_by_xpath(
                            "//div[@id='content']/form/select[3]//option[%s]" % str(day + 2)).is_selected():
                wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[%s]" % str(day + 2)).click()
        # Choose in month
        if not wd.find_element_by_xpath(
                            "//div[@id='content']/form/select[4]//option[%s]" % str(month + 1)).is_selected():
                wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[%s]" % str(month + 1)).click()
        # Fill in year
        self.app.change_field_value("ayear", year)

    def fill_birth_date(self, day, month, year):
        wd = self.app.wd
        # Choose in day
        if not wd.find_element_by_xpath(
                            "//div[@id='content']/form/select[1]//option[%s]" % str(day + 2)).is_selected():
                wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[%s]" % str(day + 2)).click()
        # Choose in month
        if not wd.find_element_by_xpath(
                            "//div[@id='content']/form/select[2]//option[%s]" % str(month + 1)).is_selected():
                wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[%s]" % str(month + 1)).click()
        # Fill in year
        self.app.change_field_value("byear", year)

    def fill_www_address(self, www):
        wd = self.app.wd
        self.app.change_field_value("homepage", www.www)

    def fill_emails(self, emails):
        wd = self.app.wd
        self.app.change_field_value("email", emails.email1)
        self.app.change_field_value("email2", emails.email2)
        self.app.change_field_value("email3", emails.email3)

    def fill_phone_number(self, phoneNumbers):
        wd = self.app.wd
        # Fill in home number
        self.app.change_field_value("home", phoneNumbers.home)
        self.app.change_field_value("mobile", phoneNumbers.mobile)
        self.app.change_field_value("work", phoneNumbers.work)
        self.app.change_field_value("fax", phoneNumbers.fax)

    def fill_personal_data(self, personalData):
        wd = self.app.wd
        self.app.change_field_value("firstname", personalData.firstname)
        self.app.change_field_value("middlename", personalData.middlename)
        self.app.change_field_value("lastname", personalData.lastname)
        self.app.change_field_value("nickname", personalData.nickname)
        # Add photo
        # wd.find_element_by_name("photo").click()
        self.app.change_field_value("title", personalData.title)
        self.app.change_field_value("company", personalData.company)
        self.app.change_field_value("address", personalData.address)

    def init_new_contact(self):
        wd = self.app.wd
        wd.find_element_by_link_text("nowy wpis").click()

    def delete_first_contact(self):
        wd = self.app.wd
        # Choose first contact
        wd.find_element_by_name("selected[]").click()
        # Submit contact deletation
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        # closing alert window
        wd.switch_to_alert().accept()

    def delete_all_contacts(self):
        wd = self.app.wd
        # Choose all contacts
        # //form[@name='MainForm']/input[2]
        wd.find_element_by_xpath("//input[@id='MassCB']").click()
        # Submit contact deletation
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        # closing alert window
        wd.switch_to_alert().accept()

    def init_first_contact_edition(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//img[@title='Edytuj']").click()

    def update_contact_top(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@value='Aktualizuj'][1]").click()

    def update_contact_bottom(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@value='Aktualizuj'][2]").click()

    def delete_edited_contact(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@value='Usuń']").click()