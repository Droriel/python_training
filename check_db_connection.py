# import pymysql.cursors
# import mysql.connector
# from fixture.db import DbFixture
from fixture.orm import ORMFixture

# connection = pymysql.connect(host='localhost', database='addressbook', user='root', password='')
# connection = mysql.connector.connect(host='127.0.0.1', database='addressbook', user='root', password='')
# db = DbFixture(host='localhost', name='addressbook', user='root', password='')
from model.group import Group

db = ORMFixture(host='localhost', name='addressbook', user='root', password='')

# try:
#     cursor = connection.cursor()
#     # cursor.execute('select * from group_list')
#     cursor.execute('select group_id, group_name, group_header, group_footer from group_list')
#     for row in cursor.fetchall():
#         print(row)
# finally:
#     connection.close()

try:
    # groups = db.get_group_list()
    # for group in groups:
    #     print(group)
    # print(len(groups))

    # contacts = db.get_contact_list()
    # for contact in contacts:
    #     print(contact)
    # print(len(contacts))

    # contacts = db.get_contacts_in_group(Group(id='553'))
    # for contact in contacts:
    #     print(contact)
    # print(len(contacts))

    contacts = db.get_contacts_not_in_group(Group(id='553'))
    for contact in contacts:
        print(contact)
    print(len(contacts))
finally:
    pass
    # db.destroy()

