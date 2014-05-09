__author__ = 'natalia'
"""
P1. Merge 2 objects with any depth (including contained dictionaries, lists, sets, strings, integers, floats). Type mismatches should yield a tuple with the two elements.
"""


def read_input_file(filename):
    f = open(filename, 'r')
    my_list = []

    for line in f:
        if line != '\n':
            index_of_whitespace = line.index(' ')
            key = line[:index_of_whitespace]
            value = line[index_of_whitespace:].strip()
            my_dict = {key : int(value)}
            my_list.append(my_dict)

    f.close()
    return my_list


def write_output_file(filename, index_list):
    import os
    os.remove(filename)
    f = open(filename, 'a')
    for item in index_list:
        f.write(str(item))
        f.write('\t')
    f.close()

def sort_dict_after_keys(dict_list):
    received_dict_index = range(1, len(dict_list) + 1)
    while True:
        done = True
        for i in range(len(dict_list) - 1):
            key_1 = dict_list[i].keys()[0]
            key_2 = dict_list[i+1].keys()[0]
            if (key_1 > key_2) or (key_1 == key_2 and dict_list[i][key_1] > dict_list[i + 1][key_2]):
                done = False

                aux = dict_list[i]
                dict_list[i] = dict_list[i + 1]
                dict_list[i + 1] = aux

                aux_index = received_dict_index[i]
                received_dict_index[i] = received_dict_index[i + 1]
                received_dict_index[i + 1] = aux_index
        if done:
            break
    return (dict_list, received_dict_index)


def main_function(input_file, output_file):
    initial_dict_list = read_input_file(input_file)
    print 'Initial dict: {}'.format(initial_dict_list)
    sorted_dict_list, sorted_index_list = sort_dict_after_keys(initial_dict_list)
    print 'Sorted dict: {} '.format(sorted_dict_list)
    write_output_file(output_file, sorted_index_list)

if __name__ == "__main__":
    main_function('P3Input.txt', 'P3Output.txt')

"""
    Example:

    input:      [{'a': 10}, {'f': 9}, {'b': 12}, {'c': 8}, {'a': 7}, {'d': 20}, {'c': 5}]
                     1          2         3          4         5         6          7

    output:     [5, 1, 3, 7, 4, 6, 2]
"""