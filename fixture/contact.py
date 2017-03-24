# -*- coding: utf-8 -*-
from model.contact import ContactBaseData
import re


class  ContactHelper:

    def __init__(self, app):
        self.app = app

# additional methods -adding contact
    def open_main_page(self):
        wd = self.app.wd
        if not(wd.current_url.endswith('/addressbook/') and len(wd.find_elements_by_xpath("//strong[contains(.,'Liczba trafień:')]")) > 0):
            wd.find_element_by_xpath("//a[contains(.,'strona główna')]").click()

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

    def fill_anniversary_date(self, anniversaryDate):
        wd = self.app.wd
        # Choose in day
        if not wd.find_element_by_xpath(
                            "//div[@id='content']/form/select[3]//option[%s]" % str(anniversaryDate.day + 2)).is_selected():
                wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[%s]" % str(anniversaryDate.day + 2)).click()
        # Choose in month
        if not wd.find_element_by_xpath(
                            "//div[@id='content']/form/select[4]//option[%s]" % str(anniversaryDate.month + 1)).is_selected():
                wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[%s]" % str(anniversaryDate.month + 1)).click()
        # Fill in year
        self.app.change_field_value("ayear", anniversaryDate.year)

    def update_anniversary_date(self, anniversaryDate):
        wd = self.app.wd
        # Choose in day
        if not wd.find_element_by_xpath(
                            "//div[@id='content']/form/select[3]//option[%s]" % str(anniversaryDate.day + 2)).is_selected():
                wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[%s]" % str(anniversaryDate.day + 2)).click()
        # Choose in month
        if not wd.find_element_by_xpath(
                            "//div[@id='content']/form/select[4]//option[%s]" % str(anniversaryDate.month + 2)).is_selected():
                wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[%s]" % str(anniversaryDate.month + 2)).click()
        # Fill in year
        self.app.change_field_value("ayear", anniversaryDate.year)

    def fill_birth_date(self, birthDate):
        wd = self.app.wd
        # Choose in day
        if not wd.find_element_by_xpath(
                            "//div[@id='content']/form/select[1]//option[%s]" % str(birthDate.day + 2)).is_selected():
                wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[%s]" % str(birthDate.day + 2)).click()
        # Choose in month
        if not wd.find_element_by_xpath(
                            "//div[@id='content']/form/select[2]//option[%s]" % str(birthDate.month + 1)).is_selected():
                wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[%s]" % str(birthDate.month + 1)).click()
        # Fill in year
        self.app.change_field_value("byear", birthDate.year)

    def update_birth_date(self, birthDate):
        wd = self.app.wd
        # Choose in day
        if not wd.find_element_by_xpath(
                            "//div[@id='content']/form/select[1]//option[%s]" % str(birthDate.day + 2)).is_selected():
                wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[%s]" % str(birthDate.day + 2)).click()
        # Choose in month
        if not wd.find_element_by_xpath(
                            "//div[@id='content']/form/select[2]//option[%s]" % str(birthDate.month + 2)).is_selected():
                wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[%s]" % str(birthDate.month + 2)).click()
        # Fill in year
        self.app.change_field_value("byear", birthDate.year)

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

    def fill_contact_base_data(self,baseData):
        wd = self.app.wd
        self.app.change_field_value("firstname", baseData.firstname)
        self.app.change_field_value("lastname", baseData.lastname)
        # self.app.change_field_value("home", phoneNumbers.home)
        # self.app.change_field_value("mobile", phoneNumbers.mobile)
        # self.app.change_field_value("work", phoneNumbers.work)
        # self.app.change_field_value("phone2", additionalData.phone)
        # self.app.change_field_value("email", emails.email1)
        # self.app.change_field_value("email2", emails.email2)
        # self.app.change_field_value("email3", emails.email3)

    def fill_personal_data(self, personalData):
        wd = self.app.wd
        self.app.change_field_value("middlename", personalData.middlename)
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
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_main_page()
        # Choose first contact
        wd.find_elements_by_name("selected[]")[index].click()
        # Submit contact deletation
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        # closing alert window
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def delete_all_contacts(self):
        wd = self.app.wd
        self.open_main_page()
        # Choose all contacts
        # //form[@name='MainForm']/input[2]
        wd.find_element_by_xpath("//input[@id='MassCB']").click()
        # Submit contact deletation
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        # closing alert window
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def init_first_contact_edition(self):
        wd = self.app.wd
        self.init_by_index_contact_edition(0)

    def init_by_index_contact_edition(self,index):
        wd = self.app.wd
        self.open_main_page()
        wd.find_elements_by_xpath("//img[@title='Edytuj']")[index].click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.open_main_page()
        wd.find_elements_by_xpath("//img[@alt='Szczegóły']")[index].click()

    def update_contact_top(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@value='Aktualizuj'][1]").click()
        self.contact_cache = None

    def update_contact_bottom(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@value='Aktualizuj'][2]").click()
        self.contact_cache = None

    def delete_edited_contact(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@value='Usuń']").click()
        self.contact_cache = None

    # counting elements on the list
    def count(self):
        wd = self.app.wd
        self.open_main_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        wd = self.app.wd
        self.open_main_page()
        self.contact_cache = []
        for row in wd.find_elements_by_name('entry'):
            cells = row.find_elements_by_tag_name('td')
            id = cells[0].find_element_by_tag_name('input').get_attribute('value')
            # . przed // oznacza relatywne użycie xpatha - jakby tworzyła nowy dom w ramach wiersza
            # text1 = element.find_element_by_xpath(".//td[2]").text
            # text2 = element.find_element_by_xpath(".//td[3]").text
            # lastName = row.find_element_by_css_selector('*>td:nth-of-type(2)').text
            # firstName = row.find_element_by_css_selector('*>td:nth-of-type(3)').text
            firstName = cells[2].text
            lastName = cells[1].text
            allPhones = cells[5].text
            allEmails = cells[4].text
            address = cells[3].text
            self.contact_cache.append(ContactBaseData(firstname=firstName, lastname=lastName, id=id, address=address,
                                                      allPhonesFromHomePage=allPhones, allEmailsFromHomePage=allEmails))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.init_by_index_contact_edition(index)
        id = wd.find_element_by_name('id').get_attribute('value')
        firstname = wd.find_element_by_name('firstname').get_attribute('value')
        lastname = wd.find_element_by_name('lastname').get_attribute('value')
        address = wd.find_element_by_name('address').get_attribute('value')
        homephone = wd.find_element_by_name('home').get_attribute('value')
        workphone = wd.find_element_by_name('work').get_attribute('value')
        mobilephone = wd.find_element_by_name('mobile').get_attribute('value')
        additionalphone = wd.find_element_by_name('phone2').get_attribute('value')
        email1 = wd.find_element_by_name('email').get_attribute('value')
        email2 = wd.find_element_by_name('email2').get_attribute('value')
        email3 = wd.find_element_by_name('email3').get_attribute('value')
        return ContactBaseData(firstname=firstname, lastname=lastname, id=id,
                               homephone=homephone, workphone=workphone, mobilephone=mobilephone,
                                                    additionalphone=additionalphone, email1=email1, email2=email2, email3=email3, address=address)

    def get_contact_info_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id('content').text
        if re.search('H:\s(.*)', text) is not None:
            homephone = re.search('H:\s(.*)', text).group(1)
        else:
            homephone = None
        if re.search('W:\s(.*)', text) is not None:
            workphone = re.search('W:\s(.*)', text).group(1)
        else:
            workphone = None
        if re.search('M:\s(.*)', text) is not None:
            mobilephone = re.search('M:\s(.*)', text).group(1)
        else:
            mobilephone = None
        if re.search('P:\s(.*)', text) is not None:
            additionalphone = re.search('P:\s(.*)', text).group(1)
        else:
            additionalphone = None
        # allEmails = wd.find_elements_by_xpath("//a[starts-with(@href, 'mailto:')]")
        allEmails = []
        for i in range(0, len(wd.find_elements_by_xpath("//a[starts-with(@href, 'mailto:')]"))):
            allEmails.append(wd.find_elements_by_xpath("//a[starts-with(@href, 'mailto:')]")[i].text)
        return ContactBaseData(homephone=homephone, workphone=workphone, mobilephone=mobilephone,
                                                    additionalphone=additionalphone, allEmailsFromHomePage=allEmails)
