class Contact:

    def __init__(self, lastname=None, firstname=None, id=None):
        self.lastname = lastname
        self.firstname = firstname
        self.id = id


class PersonalData:

    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, title=None, company=None, address=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
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


class Wwww:

    def __init__(self, www=None):
        self.www = www


class AdditionalData:

    def __init__(self, address=None, phone=None):
        self.address = address
        self.phone = phone


class Notes:

    def __init__(self, notes=None):
        self.notes = notes



