import unittest
import day_1 as d1

class TestSum(unittest.TestCase):
    def setUp(self):
        self.list_num = [1721,979,366,299,675,1456]
    
    # test that function(list) returns 2 elements
    def test_len_of_2(self):
        x = d1.sum_to_2020(self.list_num)
        self.assertEqual(len(x), 2)

    # test function(list) returns elements which sum to 2020
    def test_sum_is_2020(self):
        x = d1.sum_to_2020(self.list_num)
        sumofelem = x[0] + x[1]
        self.assertEqual(sumofelem, 2020)


if __name__ == '__main__':
    unittest.main()