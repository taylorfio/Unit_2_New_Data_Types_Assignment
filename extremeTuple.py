"""
the tuple goes into the extremeTuple function as a parameter and the max and min of the tuple are stated. It also
finds if the tuple is empty, if all the numbers are the same or if it only contains one value
"""


def extremeTuple(args):  # function that sorts tuple
    try:
        if len(args) == 0:  # states if there are no numbers in the tuple
            return "length = 0"
        if min(args) == max(args):  # states the max and min are the same
            return "all values are " + max(str(args))
        else:
            return 'tuple max is', max(args), 'tuple min is', min(args)  # states the max and min of the tuple
    except:  # if the tuple doesn't work in the try statement it means the tuple only has one number value
        return args, "is the max and min becasue there is only one number"


tup = (24, 7, 0, 5)  # example tuple
print(extremeTuple(tup))  # prints the returned max and min values for the tuple from the function

