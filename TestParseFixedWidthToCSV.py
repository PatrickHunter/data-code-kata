import unittest

import ParseFixedWidthToCSV
from ParseFixedWidthToCSV import _calculate_cumulative_offsets

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
if __name__ == '__main__':
    unittest.main()
