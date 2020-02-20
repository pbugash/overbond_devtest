import unittest
from main import *

class TestGetCurve(unittest.TestCase):

    global corp_list, gov_list, benchmarks
    corp_list, gov_list = make_bond_list("sample_input_2.csv")
    benchmarks = get_benchmarks(corp_list, gov_list)

    def test_get_curve(self):
        c1 = corp_list[0]
        curve = get_curve(c1, gov_list)
        self.assertEqual(curve, 1.17)

        c2 = corp_list[1]
        curve = get_curve(c2, gov_list)
        self.assertEqual(curve, 2.33)
        
        # check that gov bonds are still the closest to corp
        # even if gov bonds are out of order, and that 
        c3 = corp_list[2]
        curve = get_curve(c3, gov_list)
        self.assertEqual(curve, 2.88)

if __name__ == '__main__':
    unittest.main()