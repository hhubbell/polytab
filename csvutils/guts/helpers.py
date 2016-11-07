#
# This file contains the following functionality for csvutils
#   Constants
#   File IO utilities
#   Iterable manipulation
#

from __future__ import division
import csv
import decimal


KEY_VALUE_STR_FORMAT = '{:<{}}{:>{}}'
TAB_WIDTH = 4


def align(values):
    """
    Determine alignment based on column datatype.
    :param values:      Column values
    :return string:     str.format microlanguage alignment character
    """
    try:
        [float(x) for x in values]
        alg = '>'
    except ValueError:
        alg = '<'

    return alg

def avg(values):
    """
    Return the average of a list of numbers
    :param values:      Iter of values
    :return float:      Average of values
    """
    values = list(values)
    return sum(values) / len(values)

def ikeep(vals, indexes):
    """
    Inverse of imask
    :param vals:        List to mask
    :param indexes:     List of indexes to apply
    :return list:       Masked list
    """
    return [x for i, x in enumerate(vals) if i in indexes]

def imask(vals, indexes):
    """
    Mask a list based on a list of indexes
    :param vals:        List to mask
    :param indexes:     List of indexes to apply
    :return list:       Masked list
    """
    return [x for i, x in enumerate(vals) if i not in indexes]

def indexes(haystack, needles):
    """
    Return the indexes of the needles in the haystack
    :param haystack:    List to search
    :param needles:     Items to find
    :return list:       List of indexes matching needles in haystack
    """
    if needles:
        indexes = [haystack.index(x) for x in needles]
    else:
        indexes = range(len(haystack))

    return indexes

def quote(value):
    """
    Return a quoted string if the value is str
    """
    if isinstance(value, str):
        res = "'" + value + "'"
    else:
        res = value

    return res

def tofloat(value):
    """
    Convert a value to a float.  Return 0 for any failures.
    :param value:       Value to convert
    :return float:      Converted value
    """
    try:
        number = decimal.Decimal(value)
    except decimal.InvalidOperation:
        number = decimal.Decimal(0)

    return number

def trunc(string, width, replace='...'):
    """
    Truncate a string if it exceeds the specified width, replacing
    the truncated data with an ellipsis or other.
    :param string:      String to truncate
    :param width:       Max string length
    :option replace:    Replace truncated data with
    :return string:     New truncated string
    """
    return string[:width - len(replace)] + replace if len(string) > width else string