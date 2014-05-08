__author__ = 'natalia'
"""
P1. Merge 2 objects with any depth (including contained dictionaries, lists, sets, strings, integers, floats). Type mismatches should yield a tuple with the two elements.
"""

def readInputFile(filename):
    f = open(filename, 'r')
    my_list = []

    for line in f:
        if line != '\n':
            index_of_whitespace = line.index(' ')
            key = line[:index_of_whitespace]
            value = line[index_of_whitespace:].strip()
            my_dict = {key : int(value)}
            my_list.append(my_dict)

    return my_list

def mainFunction(filename):
    my_list = readInputFile(filename)
    print my_list

if __name__ == "__main__":
    mainFunction('P3Input.txt')