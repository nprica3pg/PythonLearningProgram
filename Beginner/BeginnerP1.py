__author__ = 'natalia'
"""
P1. Implement a function that will flatten two lists up to a maximum given depth.
"""
import itertools


def flatten(list_a, list_b, max_depth):
    """

    :param list_a: first list to flatten
    :param list_b: second list to flatten
    :param max_depth: depth until the flattening goes
    :return: the two flattened lists concatenated
    """
    return list(itertools.chain(flatten_aux(list_a, max_depth),flatten_aux(list_b, max_depth)))


def flatten_aux(list1, max_depth):
    max_depth -= 1
    if not list1:
        return []
    result = []
    for el in list1:
        if isinstance(el, list):
            if max_depth >= 0:
                result.extend(flatten_aux(el, max_depth))
            else:
                result.append(el)
        else:
            result.append(el)
    return result

if __name__ == "__main__":
    list_1 = [1, 2, [3, 4, [5, 6, 7, [8, 9]]]]
    list_2 = [10, [[11, 12], 19, [20, 21], [13, [14, 15, [16, 17, 18]]]]]
    print flatten(list_1, list_2, 1)
    print flatten(list_1, list_2, 2)
    print flatten(list_1, list_2, 3)
    print flatten(list_1, list_2, 4)