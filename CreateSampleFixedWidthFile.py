def create_padding(padding_length, padding_char =" "):
    return padding_char * padding_length


def create_fixed_width_header(columns, offsets):
    header = ""
    for x in range(0, len(columns)):
        padding = create_padding(len(columns[x]) - offsets[x])
        header += columns[x]
        header += padding
    return header
