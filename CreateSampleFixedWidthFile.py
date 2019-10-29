import string
import random

def create_padding(padding_length, padding_char =" "):
    return padding_char * padding_length


def create_fixed_width_header(column_names, offsets):
    header = ""
    for x in range(0, len(column_names)):
        padding = create_padding(offsets[x] - len(column_names[x]))
        header += column_names[x]
        header += padding
    header += "\n"
    return header

def create_dummy_entry(offset):
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(offset))

def create_dummy_row(offsets):
    row = ""
    for offset in offsets:
        row += create_dummy_entry(offset)
    row += "\n"
    return row


def create_dummy_fixed_width_file(column_names, offsets, num_rows, filename):
    content = create_fixed_width_header(column_names, offsets)
    for x in range(0, num_rows):
        content += create_dummy_row(offsets)
    content.encode('windows-1252')
    output_file = open(filename, "w")
    output_file.write(content)
    output_file.close()

offsets = [5,12,3,2,13,7,10,13,20,13]
column_names = ["f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8", "f9", "f10"]
filename = "test_output_file"
num_rows = 10

create_dummy_fixed_width_file(column_names, offsets, num_rows, filename)