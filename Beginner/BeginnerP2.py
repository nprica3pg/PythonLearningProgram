__author__ = 'natalia'
"""
P1. Merge 2 objects with any depth (including contained dictionaries, lists, sets, strings, integers, floats). Type mismatches should yield a tuple with the two elements.
"""


def merge(obj_a, obj_b):
    """

    :param obj_a:
    :param obj_b:
    :return: the two objects merged
    """
    result = type(obj_a)()
    if type(obj_a) != type(obj_b):
        result = (obj_a, obj_b)

    elif hasattr(obj_a, '__iter__') and hasattr(obj_b, '__iter__'):  # the object is iterable

        if type(obj_a) == dict:
            obj_a_keys = obj_a.keys()
            if obj_a_keys != obj_b.keys():
                result = (obj_a, obj_b)
            else:
                for k in obj_a_keys:
                    result[k] = merge(obj_a[k], obj_b[k])

        elif type(obj_a) == list:
            obj_a.extend(obj_b)
            result = obj_a

        elif type(obj_a) == set:
            result = obj_a | obj_b

    else:
        result = obj_a + obj_b

    return result


if __name__ == "__main__":
    obj_1 = {'x': [1, 2, 3], 'y': 1, 'z': set([1, 2, 3]), 'w': 'qweqwe', 't': {'a': [1, 2]}, 'm': [1]}
    obj_2 = {'x': [4, 5, 6], 'y': 4, 'z': set([4, 2, 3]), 'w': 'asdf', 't': {'a': [3, 2]}, 'm': "wer"}
    print merge(obj_1, obj_2)