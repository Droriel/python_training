# -*- coding: utf-8 -*-
import pymysql.cursors
# import mysql.connector

from model.group import Group
from model.contact import ContactAllData, ContactBaseData, PhoneNumbers


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)
        # self.connection = mysql.connector.connect(host=host, database=name, user=user, password=password)
        # self.connection.autocommit = True

    def get_group_list(self):
        list =[]
        cursor = self.connection.cursor()
        # sprawdzić czy można zamiast poniższego użyć kontrukcji with
        try:
            cursor.execute('select group_id, group_name, group_header, group_footer from group_list')
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list =[]
        cursor = self.connection.cursor()
        # sprawdzić czy można zamiast poniższego użyć kontrukcji with
        try:
            cursor.execute('select id, firstname, lastname, address, home, mobile, work, phone2, email, email2, email3 from addressbook where deprecated="0000-00-00 00:00:00"')
            for row in cursor:
                (id, firstname, lastname, address, homephone, mobilephone, workphone, additionalphone, email1, email2, email3) = row
                contactBaseData = ContactBaseData(id=str(id), firstname=firstname, lastname=lastname, address=address,
                                                  homephone=homephone, mobilephone=mobilephone, workphone=workphone, additionalphone=additionalphone,
                                                  email1=email1, email2=email2, email3=email3)
                list.append(ContactAllData(contactBaseData=contactBaseData, personalData='', phoneNumbers='',
                                           emails='',www='', additionalData='', notes='', birthDate='', anniversaryDate=''))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()