"""Functions for use in creating the fixed width file"""
import string
import random
from random import randint

def create_padding(padding_length, padding_char =" "):
    """generates padding to append to  short entries"""

    return padding_char * padding_length


def create_fixed_width_header(column_names, offsets):
    """Creates a string represnting the header row"""

    header = ""
    for x in range(0, len(column_names)):
        padding = create_padding(offsets[x] - len(column_names[x]))
        header += column_names[x]
        header += padding
    header += "\n"
    return header

def create_dummy_entry(offset):
    """Creates random string right padded with spaces and length equalt to offset"""

    padding_length = randint(0,offset)
    content = ''.join(random.choice(string.punctuation + string.ascii_uppercase) for _ in range(offset - padding_length))
    entry = content + create_padding(padding_length)
    return entry

def create_dummy_row(offsets):
    """Creates a string representation of a row, with entry's whose lengths match the offsets"""

    row = ""
    for offset in offsets:
        row += create_dummy_entry(offset)
    row += "\n"
    return row


def create_dummy_fixed_width_file(column_names, offsets, num_rows, filename):
    """Create a fixed width file with random data.

    Args:
        column_names: The names of the columns as a list of strings.
        offests: The offests as a list of integers.
        num_rows: The number of rows (excluding the header) as an integer.
        filname: The name of the file to be writen.

    """

    content = create_fixed_width_header(column_names, offsets)
    for x in range(0, num_rows):
        content += create_dummy_row(offsets)
    content.encode('windows-1252')
    output_file = open(filename, "w")
    output_file.write(content)
    output_file.close()

offsets = [5,12,3,2,13,7,10,13,20,13]
column_names = ["f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8", "f9", "f10"]
filename = "DummyFixedWidthFile"
num_rows = 10

create_dummy_fixed_width_file(column_names, offsets, num_rows, filename)
