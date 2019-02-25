the_list = []
try:
    file = open('studentinfoText.txt', 'r')
    file_list = file.readlines()
    for line in file_list:
        for item in line.split():
            the_list.append(item.split(","))
    print(the_list)
    for x in range(len(the_list)):
        listname = the_list[x][0: 2]
        for y in the_list[x]:
            listname.append(y)

        print(listname)


#    the_list[x][y]



except IOError:
    print("error 404 / files not found")  # defencive coding



student_dictionary = {
    'lname': lname_list,
    'fname': fname_list,
    'grade': grade_list,
    'house': house_list,
    'adviser': adviser_list
}

# lname, fname, grade, house, adviser




with open('studentInfoText.txt') as f:
    for i in f:
        line = tuple(map(str, i.split(",")))
        directory.append(line)

    for i in directory:
        if FirstName in i[0] and LastName in i[1] and Grade in i[2] and House in i[3] and Adviser in i[4]:
            tempDirectory.append(i)

    for i in tempDirectory:
        print (i)

the_list = []
student_dictionary = {}
try:
    file = open('studentinfoText.txt', 'r')
    file_list = file.readlines()
    for line in file_list:
        for item in line.split():
            the_list.append(item.split(","))
    # print(the_list)
    for x in range(len(the_list)):
        for y in the_list[x]:
            listname = y
            # listname.append(the_list[x])
            student_dictionary[listname] = the_list[x]
    print(student_dictionary)

            # print(listname)
except IOError:
    print("error 404 / files not found")  # defencive coding






"""
student_dictionary = {
    'fname': fname_list,
    'lname': lname_list,
    'grade': grade_list,
    'house': house_list,
    'adviser': adviser_list
}

# lname, fname, grade, house, adviser




with open('studentInfoText.txt') as f:
    for i in f:
        line = tuple(map(str, i.split(",")))
        directory.append(line)

    for i in directory:
        if FirstName in i[0] and LastName in i[1] and Grade in i[2] and House in i[3] and Adviser in i[4]:
            tempDirectory.append(i)

    for i in tempDirectory:
        print (i)
"""