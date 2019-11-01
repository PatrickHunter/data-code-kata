"""Functions for parsing a fixed width file to CSV."""
import csv
import os

_spec_column_names = ["f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8", "f9", "f10"]
_spec_column_offsets = [5, 12, 3, 2, 13, 7, 10, 13 ,20 ,13]

def _calculate_cumulative_offsets(offsets):
    """Uses a list of offsets to calculate the end position of each column.

    I almost just hardcoded the correct list.
    But I wanted something more flexible and to demonstrate that I can write this function.
    """

    assert(len(offsets) >0), "offsets can't be empty"
    cumulative_offset = 0
    cumulative_offsets = []
    for column in range(0, len(offsets)):
        offset = offsets[column]
        assert(isinstance(offset, int)), "offsets must be integers"
        assert(offset >0), "offsets must be postive"
        cumulative_offset += offset
        cumulative_offsets.append(cumulative_offset)
    return cumulative_offsets

def _encode_list_items(items, format = "utf-8"):
    """Changes the encoding of each list item to the given format, default utf-8"""

    encoded =[]
    try:
        encoded =[x.encode(format) for x in items]
    except UnicodeDecodeError as e:
        print "All characters in the input must be avalible in the output encoding"
        raise e
    return encoded

def _create_padding(padding_length, padding_char =" "):
    """Creates padding, used if the header must be inferred"""

    return padding_char * padding_length

def _create_fixed_width_header(column_names, offsets):
    """Creates a fixed width header based on the names and offests

    Not actually needed if the input follows the spec, but I include and option to
    infer a header in the parsing function.
    """

    header = ""
    for x in range(0, len(column_names)):
        padding = _create_padding(offsets[x] - len(column_names[x]))
        header += column_names[x]
        header += padding
    header += "\n"
    return header

def _split_fixed_width_row(row, cumulative_offsets):
    """Splits a string into a list of strings using the cumulative_offests"""

    split_row = []
    start_index = 0
    for cumulative_offset in cumulative_offsets:
        entry = row[start_index:cumulative_offset]
        split_row.append(entry)
        start_index = cumulative_offset
    return split_row

def parse_fixed_width_file_to_csv(input_file,
                                  output_file,
                                  input_encoding = "windows-1252",
                                  output_encoding = "utf-8",
                                  column_names = _spec_column_names,
                                  offsets = _spec_column_offsets):
    """Parses a fixed width file to a CSV file. 
    
    Args:
        input_file: The name of the input file.
        output_file; The name of the output file.
        input_encoding
        output_encoding: Endcoding of the output file, defaults to utf-8
        column_names: List of column names, defaults to the spec.
        offsets: List of offsets, defaults to the spec.
    Returns:
        No return value, only side effects.
    Raises:
        ValueError: Header is missing or invalid
        UnicodeDecodeError: The input contains character(s) not in output_encoding
        AssertionError: Other invalid inputs, details in message.
    """
    input =  open(input_file, 'r') 
    output = open(output_file, 'wb')
    writer = csv.writer(output)

    expected_header = _create_fixed_width_header(column_names, offsets)
    header = input.readline()
    if expected_header != header:
        raise ValueError("expected header %str got header %str" % (expected_header, header))
    writer.writerow(_encode_list_items(column_names, output_encoding))
    try:
        cumulative_offsets = _calculate_cumulative_offsets(offsets)
        row_len = sum(offsets) + 1
        for row in input:
            assert(len(row) == row_len), "row not the expected length"
            split_row = _split_fixed_width_row(row, cumulative_offsets)
            encoded_row =_encode_list_items(split_row, output_encoding)
            writer.writerow(encoded_row)
    except Exception as e:
        os.remove(output_file)
        input.close()
        raise e
    output.close    
    input.close()
