import unittest
from bond import *
from benchmarks import *

class TestGetBenchmarks(unittest.TestCase):

    global corp_list, gov_list, benchmarks
    corp_list, gov_list = make_bond_list("sample_input.csv")
    benchmarks = get_benchmarks(corp_list, gov_list)

    def test_get_benchmarks(self):

        c1 = corp_list[0]
        self.assertEqual(benchmarks[c1][0].name, "G1")
        
        c2 = corp_list[1]
        self.assertEqual(benchmarks[c2][0].name, "G2")

        c7 = corp_list[6]
        self.assertEqual(benchmarks[c7][0].name, "G6")

        
if __name__ == '__main__':
    unittest.main()