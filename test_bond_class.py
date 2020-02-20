import unittest
from bond import *

class TestBondClass(unittest.TestCase):
    
    def test_correct(self):
        corp = Bond("Corp1", "corporate", 1.5, 2.5)
        self.assertEqual(corp.name, "Corp1")
        self.assertEqual(corp.type, "corporate")
        self.assertEqual(corp.term, 1.5)
        self.assertEqual(corp.yld, 2.5)

    def test_type_error(self):
        with self.assertRaises(BondTypeError):
            gov = Bond("Gov1", "invalid", 1.5, 2.5)

    def test_term_error(self):
        with self.assertRaises(BondTermError):
            gov = Bond("Gov1", "government", -1.5, 2.5)

    def test_yield_error(self):
        with self.assertRaises(BondYieldError):
            gov = Bond("Gov1", "government", 1.5, -2.5)

    def test_diff_term(self):
        corp = Bond("Corp1", "corporate", 1.5, 1.3)
        gov = Bond("Gov1", "government", 2, 1.8)
        self.assertEqual(corp.diff_term(gov), 0.5)


if __name__ == '__main__':
    unittest.main()