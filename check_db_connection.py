import pymysql.cursors
# import mysql.connector

connection = pymysql.connect(host='localhost', database='addressbook', user='root', password='')
# connection = mysql.connector.connect(host='127.0.0.1', database='addressbook', user='root', password='')


try:
    cursor = connection.cursor()
    # cursor.execute('select * from group_list')
    cursor.execute('select group_id, group_name, group_header, group_footer from group_list')
    for row in cursor.fetchall():
        print(row)
finally:
    connection.close()