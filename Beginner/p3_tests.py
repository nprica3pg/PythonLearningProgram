import unittest


from beginner_p3 import read_input_file
from beginner_p3 import write_output_file
from beginner_p3 import sort_dict_after_keys


class P3TestCase(unittest.TestCase):

    def setUp(self):
        super(P3TestCase, self).setUp()
        self.list_from_file = [{'a': 10}, {'f': 9}, {'b': 12}, {'c': 8}, {'a': 7}, {'d': 20}, {'c': 5}]
        self.sorted_indexes = [5, 1, 3, 7, 4, 6, 2]
        self.sorted_dict = [{'a': 7}, {'a': 10}, {'b': 12}, {'c': 5}, {'c': 8}, {'d': 20}, {'f': 9}]
        self.input_filename = 'P3Input.txt'
        self.output_filename = 'P3Output.txt'

    def test_read_input_file(self):
        result = read_input_file(self.input_filename)
        self.assertListEqual(result, self.list_from_file)

    def test_sort_list_of_dicts(self):
        result_dicts, result_indexes = sort_dict_after_keys(self.list_from_file)
        self.assertListEqual(result_indexes, self.sorted_indexes)
        self.assertListEqual(result_dicts, self.sorted_dict)

    def test_write_output_file(self):
        write_output_file(self.output_filename, self.sorted_indexes)
        with open(self.output_filename, 'r') as f:
            list_ = []
            for line in f:
                splitted_line = line.split('\t')
                list_ = [int(el.strip()) for el in splitted_line if el.strip() != '']

            self.assertListEqual(list_, self.sorted_indexes)

if __name__ == "__main__":
    unittest.main()

