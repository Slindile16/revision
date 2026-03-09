import unittest
from revision import (
    check_number,
    check_mark,
    sum_to_n,
    find_max,
    count_even,
    reverse_list,
    find_duplicates
)

class TestRevision(unittest.TestCase):

    # ===============================
    # TEST CONDITIONALS
    # ===============================

    def test_check_number_positive(self):
        self.assertEqual(check_number(5), "Positive")

    def test_check_number_negative(self):
        self.assertEqual(check_number(-3), "Negative")

    def test_check_number_zero(self):
        self.assertEqual(check_number(0), "Zero")


    def test_check_mark_pass(self):
        self.assertEqual(check_mark(70), "Pass")

    def test_check_mark_fail(self):
        self.assertEqual(check_mark(40), "Fail")


    # ===============================
    # TEST LOOPS
    # ===============================

    def test_sum_to_n(self):
        self.assertEqual(sum_to_n(5), 15)


    def test_find_max(self):
        self.assertEqual(find_max([3,7,2,9]), 9)


    def test_count_even(self):
        self.assertEqual(count_even([1,2,3,4,6]), 3)

    
    # ===============================
    # TEST SIMPLE ALGORITHMS
    # ===============================

    def test_reverse_list(self):
        self.assertEqual(reverse_list([1,2,3]), [3,2,1])

    def test_reverse_list_strings(self):
        self.assertEqual(reverse_list(["a","b","c"]), ["c","b","a"])

    def test_find_duplicates(self):
        self.assertEqual(find_duplicates([1,2,3,2,4,1]), [2,1])

    def test_find_duplicates_none(self):
        self.assertEqual(find_duplicates([1,2,3]), [])



if __name__ == "__main__":
    unittest.main()