def extremeTuple (args):
    try:
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
    except:
        print("incorrect amount of values in tuple")


tup = (0, 22, 15)
print(extremeTuple(tup))
