import unittest

from beginner_p2 import merge


class P2TestCase(unittest.TestCase):

    def setUp(self):
        super(P2TestCase, self).setUp()
        self.obj_1 = {'x': [1, 2, 3], 'y': 1, 'z': set([1, 2, 3]), 'w': 'qweqwe', 't': {'a': [1, 2]}, 'm': [1]}
        self.obj_2 = {'x': [4, 5, 6], 'y': 4, 'z': set([4, 2, 3]), 'w': 'asdf', 't': {'a': [3, 2]}, 'm': "wer"}
        self.obj_3 = {'x': ('bla', ['b', 'l', 'u']), 'y': 5.4, 'a': 'mam', 't': {'a': [10, 11], 'b': 3.5}, 'm': 'mumu'}

    def test_merge_same_keys_in_dict(self):
        result = merge(self.obj_1, self.obj_2)
        expected = {'m': ([1], 'wer'), 't': {'a': [1, 2, 3, 2]}, 'w': 'qweqweasdf', 'y': 5, 'x': [1, 2, 3, 4, 5, 6], 'z': set([1, 2, 3, 4])}
        self.assertDictEqual(result, expected)

    def test_merge_different_keys(self):
        result = merge(self.obj_2, self.obj_3)
        expected = {'a': 'mam', 'm': 'wermumu', 't': {'a': [3, 2, 10, 11], 'b': 3.5}, 'w': 'asdf', 'y': (4, 5.4), 'x': ([4, 5, 6], ('bla', ['b', 'l', 'u'])), 'z': set([2, 3, 4])}
        self.assertDictEqual(result, expected, 'mumu: {}'.format(result))

    def tearDown(self):
        self.obj_1 = None
        self.obj_2 = None
        self.obj_3 = None

if __name__ == "__main__":
    unittest.main()

