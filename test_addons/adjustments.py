# -*- coding: utf-8 -*-
from re import sub


def clear_multiple_spaces(s):
    return sub('  ',' ',s)