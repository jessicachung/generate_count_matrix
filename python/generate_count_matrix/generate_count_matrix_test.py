'''
Unit tests for generate_count_matrix.

Usage: python -m unittest -v generate_count_matrix_test
'''

import unittest
from generate_count_matrix import parse_counts

class TestParseCounts(unittest.TestCase):
    '''Unit tests for parse_counts'''
    def do_test(self, data, expected, **kwargs):
        "Wrapper function for testing parse_counts"
        result = parse_counts(data, **kwargs)
        self.assertEqual(expected, result)

    def test_basic_case(self):
        "Test basic three line input"
        expected = (("A","B","C"),[1,2,3])
        self.do_test(data=["A\t1","B\t2","C\t3"], expected=expected)

    def test_defined_columns(self):
        "Test defined gene and count columns"
        expected = (("A","B","C"),[1,2,3])
        self.do_test(data=["1\tA\t0\t0\t1","2\tB\t0\t0\t2","3\tC\t0\t0\t3"],
            expected=expected, gene_col=2, count_col=5)

    def test_delimiter(self):
        "Test defined delimiter"
        expected = (("A","B","C"),[1,2,3])
        self.do_test(data=["1:A:0:0:1","2:B:0:0:2","3:C:0:0:3"],
            expected=expected, gene_col=2, count_col=5, delimiter=":")

    def test_skip_comments(self):
        "Test skipping comment lines"
        expected = (("A","B","C","D","E"),[1,2,3,4,5])
        self.do_test(
            data=["# header","# header","","A\t1","B\t2","C\t3","D\t4","E\t5"],
            expected=expected, skip_comments=True)

    def test_skip_lines(self):
        "Test skipping header lines"
        expected = (("A","B","C","D","E"),[1,2,3,4,5])
        self.do_test(
            data=["# header","# header","A\t1","B\t2","C\t3","D\t4","E\t5"],
            expected=expected, skip_lines=2)

    def test_fail_nonidentical_fields(self):
        "Files with different number of fields should exit on error"
        with self.assertRaises(SystemExit):
            parse_counts(data=["# header","A\t1","B\t2"])

    def test_fail_nonexistent_column(self):
        "Using a non-existent column should exit on error"
        with self.assertRaises(SystemExit):
            parse_counts(data=["A\t1","B\t2","C\t3"], gene_col=3)

    def test_fail_nonnumerical_counts(self):
        "Using a non-numerical count column should exit on error"
        with self.assertRaises(SystemExit):
            parse_counts(data=["A\tA","B\t2","C\t3"])


if __name__ == '__main__':
    unittest.main()
