"""
‘*args is a tuple of parameters of any length. Return the max value, min value as a tuple. You may assume all
args are numbers, but you may not assume that the length of args is non-zero.’

The program will use extremeTuple to state the maximum value, minimum value, or if there is neither a maximum or
minimum value. Your program will also handle attempts to use extremeTuple when the length of args is zero.
"""


def extremeTuple (args):
    tup1 = args[0]
    tup2 = args[1]
    tup3 = args[2]
    final_list = []

    final_list.insert(0, tup1)
    if tup2 >= final_list[0]:
        final_list.insert(0, tup2)
    else:
        final_list.insert(1, tup2)
    if tup3 >= final_list[0]:
        final_list.insert(0, tup3)
    else:
        if tup3 >= final_list[1]:
            final_list.insert(1, tup3)
        else:
            final_list.insert(2, tup3)
    return final_list


tup = (5, 22, 15)
print(extremeTuple(tup))
