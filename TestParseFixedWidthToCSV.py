import unittest

import ParseFixedWidthToCSV
from ParseFixedWidthToCSV import _calculate_cumulative_offsets, _encode_list_items, _create_padding, _split_fixed_width_row

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

    def test_split_fixed_width_row(self):
        row = "aaBBBBC\n"
        cumulative_offsets =[2,6,7]
        expected_split_row =["aa","BBBB","C"]
        split_row = _split_fixed_width_row(row, cumulative_offsets)
        self.assertEqual(split_row, expected_split_row)

if __name__ == '__main__':
    unittest.main()
