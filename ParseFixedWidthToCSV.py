import csv

_spec_column_names = ["f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8", "f9", "f10"]
_spec_column_offsets = [5, 12, 3, 2, 13, 7, 10, 13 ,20 ,13]

"""Uses a list of offsets to calculate the end position of each column.

   Depending on the circumstances I could have just hardcoded the correct list.
   But I wanted something more flexible and to demonstrate that I can write this function.
"""
def _calculate_cumulative_offsets(offsets):
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
    encoded =[x.encode(format) for x in items]
    return encoded


def parse_fixed_width_file_to_csv(input_file,
                                  output_file,
                                  input_encoding = "windows-1252",
                                  output_encoding ="utf-8",
                                  column_names = _spec_column_names,
                                  offsets = _spec_column_offsets):
    """Parses a fixed width file to a CSV file. 
    
    Args:
        input_file: The name of the input file.
        output_file; The name of the output file.
        input_encoding: Encoding of the input file, defaults to windows-1252
        output_endcoing: Endcoding of the output file, defaults to utf-8
        column_names: List of column names, defaults to the spec.
        offsets: List of offsets, defaults to the spec.
    Returns:
        No return value, only side effects.
    Raises:
        InvalidRowError: One or more rows are the wrong length.
        InvalidHeaderError: The first row is not a valid header and the input is not empty.
        InvalidSourceEncodingError: The input encoding does not match input_encoding.
        NonconvertableValueWarning: The input contains uses character(s) not in output_encoding
    """
