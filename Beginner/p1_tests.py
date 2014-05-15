import unittest

from beginner_p1 import flatten


class P1TestCase(unittest.TestCase):

    def setUp(self):
        super(P1TestCase, self).setUp()
        self.list_1 = [1, 2, [3, 4, [5, 6, 7, [8, 9]]]]
        self.list_2 = [10, [[11, 12], 19, [20, 21], [13, [14, 15, [16, 17, 18]]]]]

    def test_level0(self):
        result = flatten(self.list_1, self.list_2, 0)
        expected = [1, 2, [3, 4, [5, 6, 7, [8, 9]]], 10, [[11, 12], 19, [20, 21], [13, [14, 15, [16, 17, 18]]]]]
        self.assertEqual(result, expected)

    def test_level1(self):
        result = flatten(self.list_1, self.list_2, 1)
        expected = [1, 2, 3, 4, [5, 6, 7, [8, 9]], 10, [11, 12], 19, [20, 21], [13, [14, 15, [16, 17, 18]]]]
        self.assertEqual(result, expected)

    def test_level2(self):
        result = flatten(self.list_1, self.list_2, 2)
        expected = [1, 2, 3, 4, 5, 6, 7, [8, 9], 10, 11, 12, 19, 20, 21, 13, [14, 15, [16, 17, 18]]]
        self.assertEqual(result, expected)

    def test_level3(self):
        result = flatten(self.list_1, self.list_2, 3)
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 19, 20, 21, 13, 14, 15, [16, 17, 18]]
        self.assertEqual(result, expected)

    def test_level4(self):
        result = flatten(self.list_1, self.list_2, 4)
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 19, 20, 21, 13, 14, 15, 16, 17, 18]
        self.assertEqual(result, expected)

    def tearDown(self):
        self.list_1 = []
        self.list_2 = []

if __name__ == "__main__":
    unittest.main()

