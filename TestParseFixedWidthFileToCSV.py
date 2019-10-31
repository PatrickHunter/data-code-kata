import unittest
import os
import csv
import ParseFixedWidthFileToCSV
from ParseFixedWidthFileToCSV import _calculate_cumulative_offsets, _encode_list_items, _create_padding, _split_fixed_width_row, parse_fixed_width_file_to_csv


class TestInternalFunctions(unittest.TestCase):

    def test_calculate_cumulative_offsets(self):
        with self.assertRaises(AssertionError):
            _calculate_cumulative_offsets([])
        with self.assertRaises(AssertionError):
            _calculate_cumulative_offsets([-1])
        with self.assertRaises(AssertionError):
            _calculate_cumulative_offsets([1.1])
        spec_column_offsets = [5, 12, 3, 2, 13, 7, 10, 13 ,20 ,13]
        spec_cumulative_offsets = [5, 17, 20, 22, 35, 42, 52, 65 ,85 ,98]
        self.assertEqual(_calculate_cumulative_offsets(spec_column_offsets),
                         spec_cumulative_offsets)


    def test_encode_list_items(self):
        item1 = "item1".encode("windows-1252")
        item2 = "item2".encode("windows-1252")
        input_list = [item1,item2]
        output_list = _encode_list_items(input_list)
        output_list[0].decode('utf-8')
        output_list[1].decode('utf-8')
        self.assertEquals(input_list, output_list)

    def test_create_padding(self):
        expected_padding = "   "
        created_padding = _create_padding(3)
        self.assertEqual(expected_padding, created_padding)
        expected_padding = "**"
        created_padding= _create_padding(2, "*")
        self.assertEqual(expected_padding, created_padding)

    """since this is internal and
    used after assertions I assume valid input.
    """
    def test_split_fixed_width_row(self):
        row = "aaBBBBC\n"
        cumulative_offsets =[2,6,7]
        expected_split_row =["aa","BBBB","C"]
        split_row = _split_fixed_width_row(row, cumulative_offsets)
        self.assertEqual(split_row, expected_split_row)

class TestExternalFunction(unittest.TestCase):
    
    def test_with_no_header(self):
        with self.assertRaises(ValueError):
            parse_fixed_width_file_to_csv("NoHeaderTestInput", "NoHeaderTestOutput")

    def test_with_windows_only_char(self):
        with self.assertRaises(UnicodeDecodeError):
            parse_fixed_width_file_to_csv("WindowsTestInput", "WindowsOnlyTestOutput")
    
    def test_with_wrong_header(self):
        with self.assertRaises(ValueError):
            parse_fixed_width_file_to_csv("WrongHeaderTestInput", "WrongHeaderTestOutput")

    def test_with_row_too_long(self):
        with self.assertRaises(AssertionError):
            parse_fixed_width_file_to_csv("LongRowHeaderTestInput", "TooLongTestOutput")

    def test_with_row_too_short(self):
        with self.assertRaises(AssertionError):
            parse_fixed_width_file_to_csv("ShortRowTestInput", "TooTestShortOutput")
    
    def test_commas_in_input(self):
        parse_fixed_width_file_to_csv("CommaTestInput", "CommaTestOutput",
                                      column_names = ["f1"], offsets = [1])
        with open("CommaTestOutput", 'r') as output:
            output.readline()
            expected = '","\r\n'
            read = output.readline()
            self.assertEqual(expected,read)
        os.remove("CommaTestOutput")

    def test_quotes_in_input(self):
        parse_fixed_width_file_to_csv("QuoteTestInput", "QuoteTestOutput",
                                      column_names = ["f1"], offsets = [2])
        with open("QuoteTestOutput", 'r') as output:
            output.readline()
            expected = '" """\r\n'
            read = output.readline()
            self.assertEqual(expected,read)
        os.remove("QuoteTestOutput")

if __name__ == '__main__':
    unittest.main()
