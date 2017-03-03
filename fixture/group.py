# -*- coding: utf-8 -*-
class  GroupHelper:

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
        self.open_groups_page()
        self.select_first_group()
        # submit deletion
        if delete_button == 'top':
            wd.find_element_by_xpath("(//input[@name='delete'])[1]").click()
        elif delete_button == 'bottom':
            wd.find_element_by_xpath("(//input[@name='delete'])[2]").click()
        else:
            print("Improper parameter for delete button value")
        self.return_to_groups_page()

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def edit_first_group(self, new_group_data, edit_button):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
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

    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements_by_name("selected[]"))



