# w module sys zamieszczone są stałe
from sys import maxsize
from test_addons import adjustments


class Group:

    def __init__(self, name=None, header=None, footer=None, id=None):
        self.name = name
        self.header = header
        self.footer = footer
        self.id = id

    def __repr__(self):
        return '%s: %s %s %s ' % (self.id, self.name, self.header, self.footer)

    # def __eq__(self, other):
    #         return (self.id == other.id or self.id is None or other.id is None) and self.name == adjustments.clear_multiple_spaces(other.name).strip()

    def __eq__(self, other):
            return (self.id == other.id or self.id is None or other.id is None) and self.name == adjustments.clear_multiple_spaces(other.name)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            # maksymalna liczba dla indeksu (ponieważ w pythonie nie ma maksymalnej liczby całkowitej maxsize uznaje
            # się za taką do celów praktycznych)
            return maxsize

