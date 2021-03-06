# -*- coding: utf-8 -*-
from model.group import Group


class GroupHelper:

    def __init__(self, app):
        self.app = app

    # additional methods - adding group
    def open_groups_page(self):
        wd = self.app.wd
        if not(wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name('new')) > 0):
            wd.find_element_by_link_text("grupy").click()

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # Init group creation
        wd.find_element_by_name("new").click()
        self.fill_group_form(group)
        # Submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()
        self.group_cache = None

    def fill_group_form(self, group):
        wd = self.app.wd
        self.app.change_field_value("group_name", group.name)
        self.app.change_field_value("group_header", group.header)
        self.app.change_field_value("group_footer", group.footer)

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    # deleting first group on the list with bottom or top button
    def delete_first_group(self, delete_button):
        wd = self.app.wd
        self.delete_group_by_index(0, delete_button)

    def delete_group_by_index(self, index, delete_button):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_index(index)
        # submit deletion
        if delete_button == 'top':
            wd.find_element_by_xpath("(//input[@name='delete'])[1]").click()
        elif delete_button == 'bottom':
            wd.find_element_by_xpath("(//input[@name='delete'])[2]").click()
        else:
            print("Improper parameter for delete button value")
        self.return_to_groups_page()
        self.group_cache = None

    def delete_group_by_id(self, id, delete_button):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_id(id)
        # submit deletion
        if delete_button == 'top':
            wd.find_element_by_xpath("(//input[@name='delete'])[1]").click()
        elif delete_button == 'bottom':
            wd.find_element_by_xpath("(//input[@name='delete'])[2]").click()
        else:
            print("Improper parameter for delete button value")
        self.return_to_groups_page()
        self.group_cache = None

    def select_first_group(self):
        wd = self.app.wd
        self.select_group_by_index(0)

    def select_group_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_group_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']"%id).click()

    def edit_first_group(self, new_group_data, edit_button):
        wd = self.app.wd
        self.edit_group_by_index(0, new_group_data, edit_button)

    def edit_group_by_index(self, index, new_group_data, edit_button):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_index(index)
        # Init first group_edition
        if edit_button == 'top':
            wd.find_element_by_xpath("(//input[@name='edit'])[1]").click()
        elif edit_button == 'bottom':
            wd.find_element_by_xpath("(//input[@name='edit'])[2]").click()
        else:
            print("Improper parameter for edit button value")
        # Change group form
        self.fill_group_form(new_group_data)
        # Submit group edition
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()
        self.group_cache = None

    def edit_group_by_id(self, id, new_group_data, edit_button):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_id(id)
        # Init first group_edition
        if edit_button == 'top':
            wd.find_element_by_xpath("(//input[@name='edit'])[1]").click()
        elif edit_button == 'bottom':
            wd.find_element_by_xpath("(//input[@name='edit'])[2]").click()
        else:
            print("Improper parameter for edit button value")
        # Change group form
        self.fill_group_form(new_group_data)
        # Submit group edition
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()
        self.group_cache = None

    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements_by_name("selected[]"))

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_groups_page()
            self.group_cache = []
            for element in wd.find_elements_by_css_selector('span.group'):
                text = element.text
                id = element.find_element_by_name('selected[]').get_attribute('value')
                self.group_cache.append(Group(name=text, id=id))
        # tworzymy kopię listę tak aby dalej nie operować na cachu i go nie uszkodzić
        return list(self.group_cache)
        #cache trzeba zrzucić za każdym razem jak zmieninmy listę - utworzenie, modyfikwanie, usunięcie elementu


