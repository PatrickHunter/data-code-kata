from ParseFixedWidthFileToCSV import parse_fixed_width_file_to_csv
from CreateDummyFixedWidthFile import create_dummy_fixed_width_file

offsets = [5,12,3,2,13,7,10,13,20,13]
column_names = ["f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8", "f9", "f10"]
filename = "DummyFixedWidthFile"
num_rows = 10

create_dummy_fixed_width_file(column_names, offsets, num_rows, filename)
print "Randomly generated DummyFixedWidthFile"

parse_fixed_width_file_to_csv("DummyFixedWidthFile", "DummyCSVFile.csv")

print "Parsed to DummyCSVFile.csv"
