import csv

def _calculate_cumulative_offsets(input_row, offsets):
    cumulative_offset = 0
    cumulative_offsets = offsets
    for column in range(0, len(offsets)):
        offset = offsets[column]
        cumulative_offset += offset
        cumulative_offsets.append(cumulative_offset)
    return cumulative_offsets

def _encode_list_items(items, format = "utf-8"):
    encoded =[x.encode(format) for x in items]
    return encoded


def parse_fixed_width_file_to_csv(input_file, output_file,
                                  input_encoding = "windows-1252",
                                  output_encoding ="utf-8",
                                  column_name = spec_column_names,
                                  offsets = spec_column_offsets,
                                  souce_formating_srict = True)
        
