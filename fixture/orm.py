# -*- coding: utf-8 -*-
from pony.orm import *
from datetime import datetime
from model.contact import ContactBaseData
from model.group import Group
from pymysql.converters import encoders, decoders, convert_mysql_timestamp

class ORMFixture:

    db = Database()

    class ORMGroup(db.Entity):
        _table_ = 'group_list'
        id = PrimaryKey(int, column='group_id')
        name = Optional(str, column='group_name')
        header = Optional(str, column='group_header')
        footer = Optional(str, column='group_footer')
        contacts = Set(lambda: ORMFixture.ORMContact, table='address_in_groups', column='id', reverse='groups', lazy=True)
    #     lambda bo nie możemy się odwołać bezpośrednio do czegoś co jest zdeciniowane później
    #      lazy=True nie pobieraj informacji przy budowaniu obiektu jeśli się do niej nie zwracamy

    class ORMContact(db.Entity):
        _table_ = 'addressbook'
        id = PrimaryKey(int, column='id')
        firstname = Optional(str, column='firstname')
        lastname = Optional(str, column='lastname')
        address = Optional(str, column='address')
        homephone = Optional(str, column='home')
        mobilephone = Optional(str, column='mobile')
        workphone = Optional(str, column='work')
        email1 = Optional(str, column='email')
        email2 = Optional(str, column='email2')
        email3 = Optional(str, column='email3')
        # www = Optional(str, column='homepage')
        # address2 = Optional(str, column='address2')
        # phone2 = Optional(str, column='phone2')
        # notes = Optional(str, column='notes')
        deprecated = Optional(datetime, column='deprecated')
        groups = Set(lambda: ORMFixture.ORMGroup, table='address_in_groups', column='group_id', reverse='contacts', lazy=True)

    def __init__(self, host, name, user, password):
        conv = encoders
        conv.update(decoders)
        conv[datetime] = convert_mysql_timestamp
        self.db.bind('mysql', host=host, database=name, user=user, password=password, conv=conv)
        # self.db.bind ('mysql',host=host, database=name, user=user, password=password, conv=decoders)
        self.db.generate_mapping()
        # sql_debug służy do pokazywania jakie zostały zbudowane zapytania
        # sql_debug(True)

    def convert_groups_to_model(self, groups):
        def convert(group):
            return Group(id=str(group.id), name=group.name, header=group.header, footer=group.footer)
        return list(map(convert, groups))

    @db_session
    def get_group_list(self):
        # with db_session:
        return self.convert_groups_to_model(select(g for g in ORMFixture.ORMGroup))

    def convert_contacts_to_model(self, contacts):
        def convert(contact):
            return ContactBaseData(id=str(contact.id), firstname=contact.firstname, lastname=contact.lastname,
                                   address=contact.address, homephone=contact.homephone, mobilephone=contact.mobilephone,
                                   workphone=contact.workphone, email1=contact.email1, email2=contact.email2,
                                   email3=contact.email3)
        return list(map(convert, contacts))


    @db_session
    def get_contact_list(self):
        # with db_session:
        # return self.convert_contacts_to_model(select(c for c in ORMFixture.ORMContact if c.deprecated != datetime(0,0,0)))
        return self.convert_contacts_to_model(select(c for c in ORMFixture.ORMContact if c.deprecated is None))

    def get_group_by_id(self, id):
        return list(select(g for g in ORMFixture.ORMGroup if g.id == id))[0]

    @db_session
    def get_contacts_in_group(self, group):
        orm_group = self.get_group_by_id(group.id)
        return self.convert_contacts_to_model(orm_group.contacts)

    @db_session
    def get_contacts_not_in_group(self, group):
        orm_group = self.get_group_by_id(group.id)
        return self.convert_contacts_to_model\
            (select(c for c in ORMFixture.ORMContact
                    if c.deprecated is None and orm_group not in c.groups))

