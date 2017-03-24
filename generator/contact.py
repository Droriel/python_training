# -*- coding: utf-8 -*-
import random
import string
from model.contact import PersonalData, PhoneNumbers, Emails, Www, AdditionalData, Notes, ContactBaseData, \
    ContactAllData, BirthDate, AnniversaryDate
import jsonpickle
import os.path
import sys
import getopt

try:
    opts, args=getopt.getopt(sys.argv[1:], 'n:f:', ['number of contacts', 'file'])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = 'data/contacts.json'

for o, a in opts:
    if o == '-n':
        n = int(a)
    elif o == '-f':
        f = a


def random_string(maxlen):
    symbols = string.ascii_letters + ' '*13 + '-'*3 + '_'*3
    #                      + "'"*3
    return ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_string_with_new_line(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + ' '*15 + '\n'*5 + '-'*3 + '_'*3
    #  + string.punctuation
    return prefix + ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_email(maxlen):
    symbols = string.ascii_letters + ' ' * 10 + '-' * 3 + '_' * 3
    return ''.join([random.choice(symbols) for i in range(random.randrange(maxlen+5))]) + '@' +\
           ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))]) + '.' +\
           ''.join([random.choice(string.ascii_letters) for i in range(random.randrange(2,4))])


def random_phone_number(maxlen):
    symbols = str(string.digits) * 4  + '('+ ')' + '+' + '-' + ' '
    return ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_www(maxlen):
    symbols = string.ascii_letters + '-'
    return  'www.' + ''.join([random.choice(symbols)  for i in range(random.randrange(maxlen))]) + '.'+\
           ''.join([random.choice(string.ascii_letters) for i in range(random.randrange(2,4))])


def random_day():
    return random.randrange(1, 31)


def random_month():
    return random.randrange(1, 12)


def random_year():
    symbols = string.digits
    return ''.join([random.choice(symbols) for i in range(4)])


testData = [ContactAllData(contactBaseData=ContactBaseData(firstname=random_string(10), lastname=random_string(18)),
                           personalData=PersonalData(middlename=random_string(10), nickname=random_string(10),
                                                     title=random_string(10), company=random_string(20),
                                                     address=random_string_with_new_line('Adres podstawowy: ', 30)),
                           phoneNumbers=PhoneNumbers(home=random_phone_number(12), mobile=random_phone_number(16),
                                                     work=random_phone_number(12), fax=random_phone_number(10)),
                           emails=Emails(email1=random_email(8), email2=random_email(5), email3=random_email(6)),
                           www=Www(www=random_www(30)),
                           birthDate=BirthDate(day=random_day(), month=random_month(), year=random_year()),
                           anniversaryDate=AnniversaryDate(day=random_day(), month=random_month(), year=random_year()),
                           additionalData=AdditionalData(address=random_string_with_new_line('Adres dodatkowy: ', 30) ,
                                                         phone=random_phone_number(12)),
                           notes=Notes(notes=random_string_with_new_line('n', 100)))
            for i in range(n)]\
           + \
           [ContactAllData(contactBaseData=ContactBaseData(firstname='', lastname=''),
                           personalData=PersonalData(middlename='', nickname='',
                                                     title='', company='',
                                                     address=''),
                           phoneNumbers=PhoneNumbers(home='', mobile='',
                                                     work='', fax=''),
                           emails=Emails(email1='', email2='', email3=''),
                           www=Www(www=''),
                           birthDate=BirthDate(day=-1, month=0, year=''),
                           anniversaryDate=AnniversaryDate(day=-1, month=0, year=''),
                           additionalData=AdditionalData(address='' ,
                                                         phone=''),
                           notes=Notes(notes=''))]\
           +\
           [ContactAllData(contactBaseData=ContactBaseData(firstname=random_string(10), lastname=random_string(18)),
                           personalData=PersonalData(middlename=random_string(10), nickname=random_string(10),
                                                     title=random_string(10), company=random_string(20),
                                                     address=''),
                           phoneNumbers=PhoneNumbers(home='', mobile='',
                                                     work='', fax=''),
                           emails=Emails(email1='', email2='', email3=''),
                           www=Www(www=''),
                           birthDate=BirthDate(day=31, month=12, year='1999'),
                           anniversaryDate=AnniversaryDate(day=1, month=1, year='2010'),
                           additionalData=AdditionalData(address='',
                                                         phone=''),
                           notes=Notes(notes=random_string_with_new_line('n', 100)))]\
        + \
            [ContactAllData(contactBaseData=ContactBaseData(firstname=' a ', lastname=' b '),
                            personalData=PersonalData(middlename='', nickname='',
                                                      title='', company='',
                                                      address=''),
                            phoneNumbers=PhoneNumbers(home='', mobile='',
                                                      work='', fax=''),
                            emails=Emails(email1='', email2='', email3=''),
                            www=Www(www=''),
                            birthDate=BirthDate(day=-1, month=0, year=''),
                            anniversaryDate=AnniversaryDate(day=-1, month=0, year=''),
                            additionalData=AdditionalData(address='',
                                                          phone=''),
                            notes=Notes(notes=''))] \
        + \
        [ContactAllData(contactBaseData=ContactBaseData(firstname='a  b', lastname='c  d'),
                        personalData=PersonalData(middlename='', nickname='',
                                                  title='', company='',
                                                  address=''),
                        phoneNumbers=PhoneNumbers(home='', mobile='',
                                                  work='', fax=''),
                        emails=Emails(email1='', email2='', email3=''),
                        www=Www(www=''),
                        birthDate=BirthDate(day=-1, month=0, year=''),
                        anniversaryDate=AnniversaryDate(day=-1, month=0, year=''),
                        additionalData=AdditionalData(address='',
                                                      phone=''),
                        notes=Notes(notes=''))]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..' , f)

with open(file, 'w', encoding='utf8') as out:
    jsonpickle.set_encoder_options('json', indent=2)
    out.write(jsonpickle.encode(testData))