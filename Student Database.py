"""

"""
the_list = []
student_dictionary = {}
repeat = True

try:
    file = open('studentinfoText.txt', 'r')
    file_list = file.readlines()
    for line in file_list:
        for item in line.split():
            the_list.append(item.split(","))
    for x in range(len(the_list)):
        for y in the_list[x]:
            if y not in student_dictionary:
                student_dictionary[y] = the_list[x]
            elif y in student_dictionary:
                student_dictionary[y] = student_dictionary[y], the_list[x]
except IOError:
    print("error 404 / files not found")  # defencive coding

while repeat == True:
    def delete_fun(input):
        if input != "":
            temp_list.append(input)
    temp_list = []
    print("if you dont want to enter a value press enter")
    fname_input = input("enter fname value")
    delete_fun(fname_input)
    lname_input = input("enter lname value")
    delete_fun(lname_input)
    grade_input = input("enter grade value")
    delete_fun(grade_input)
    house_input = input("enter house value")
    delete_fun(house_input)
    adviser_input = input("enter adviser value")
    delete_fun(adviser_input)
    print("searching for", temp_list)
    search_list = []

    try:
        for x in temp_list:
            if student_dictionary[x]:
                if x not in search_list:
                    search_list.append(student_dictionary[x])
        print("your results are ")
        if len(search_list) == 1:
            print(search_list)  # make normal and separate lines

        if len(search_list) > 1:
            result_list = []
            for x in range(len(search_list)):
                for y in search_list[x]:
                    counter = 0
                    for item in temp_list:
                        if item in y:
                            counter = counter + 1
                    if counter == len(temp_list):
                        if y not in result_list:
                            result_list.append(y)
                            print(', '.join(y))
    except KeyError:
        print("input error")

    repeat_input = input("do you want to search? [y/n]")
    if repeat_input != 'n' and repeat_input != 'y':
        while repeat_input != 'n' and repeat_input != 'y':
            print("error")
            repeat_input = input("do you want to search? [y/n]")
    if repeat_input == 'n':
        repeat = False
