from sys import maxsize
from test_addons import adjustments


class ContactAllData:

    def __init__(self, contactBaseData, personalData, phoneNumbers, emails, www, additionalData, notes, birthDate, anniversaryDate):
        self.contactBaseData = contactBaseData
        self.personalData = personalData
        self.phoneNumbers = phoneNumbers
        self.emails = emails
        self.www = www
        self.additionalData = additionalData
        self.notes = notes
        self.birthDate = birthDate
        self.anniversaryDate = anniversaryDate

    def __repr__(self):
        return '%s' % (repr(self.contactBaseData))

    # def __repr__(self):
    #     return '%s: %s %s' % (self.ContactBaseData.id, self.ContactBaseData.lastname, self.ContactBaseData.firstname)
    #
    # def __eq__(self, other):
    #     return (self.ContactBaseData == other.ContactBaseData)


class ContactBaseData:

    def __init__(self, lastname=None, firstname=None, id=None, address=None,
                 homephone=None, mobilephone=None, workphone=None, additionalphone=None, allPhonesFromHomePage=None, allEmailsFromHomePage=None, email1=None, email2=None, email3=None):
        self.lastname = lastname
        self.firstname = firstname
        self.id = id
        self.address = address
        #all emails
        #all phones
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.additionalphone = additionalphone
        self.allPhonesFromHomePage = allPhonesFromHomePage
        self.email1 = email1
        self.email2 = email2
        self.email3 = email3
        self.allEmailsFromHomePage = allEmailsFromHomePage

    def __repr__(self):
        return '%s: %s %s' % (self.id, self.lastname, self.firstname)

    def __eq__(self, other):
        return (self.id == other.id or self.id is None or other.id is None) \
               and self.lastname.strip() == adjustments.clear_multiple_spaces(other.lastname).strip() \
               and self.firstname.strip() == adjustments.clear_multiple_spaces(other.firstname).strip()

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            # maksymalna liczba dla indeksu (ponieważ w pythonie nie ma maksymalnej liczby całkowitej maxsize uznaje
            # się za taką do celów praktycznych)
            return maxsize


class PersonalData:

    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, title=None, company=None, address=None):
        self.middlename = middlename
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address


class PhoneNumbers:

    def __init__(self, home=None, mobile=None, work=None, fax=None):
        self.home = home
        self.mobile = mobile
        self.work = work
        self.fax = fax


class Emails:

    def __init__(self, email1=None, email2=None, email3=None):
        self.email1 = email1
        self.email2 = email2
        self.email3 = email3


class Www:

    def __init__(self, www=None):
        self.www = www


class AdditionalData:

    def __init__(self, address=None, phone=None):
        self.address = address
        self.phone = phone


class Notes:

    def __init__(self, notes=None):
        self.notes = notes


class BirthDate:

    def __init__(self, day=None, month=None, year=None):
        self.day = day
        self.month = month
        self.year = year


class AnniversaryDate:
    def __init__(self, day=None, month=None, year=None):
        self.day = day
        self.month = month
        self.year = year



