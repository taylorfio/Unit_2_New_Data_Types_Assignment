the_list = []
student_dictionary = {}
repeat = True

try:
    file = open('studentinfoText.txt', 'r')
    file_list = file.readlines()
    for line in file_list:
        for item in line.split():
            the_list.append(item.split(","))
    print(the_list)
    for x in range(len(the_list)):
        for y in the_list[x]:
            if y not in student_dictionary:
                student_dictionary[y] = the_list[x]  # overwrites values that already exist need to check and if exist then append
            elif y in student_dictionary:
                student_dictionary[y] = student_dictionary[y], the_list[x]
    print(student_dictionary)
except IOError:
    print("error 404 / files not found")  # defencive coding

while repeat == True:
    def delete_fun(input):
        if input != "0":
            temp_list.append(input)
    temp_list = []
    print("if you dont want to enter a value press 0")
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
    print(temp_list)
    holder_list = []
    for x in temp_list:
        if student_dictionary[x]:
            holder_list.append(student_dictionary[x])

    print(holder_list)

    repeat_input = input("do you want to search? [y/n]")
    if repeat_input == 'n':
        repeat = False




"""


    temp_list[1]
    temp_list[2]
    temp_list[3]
    temp_list[4]
    temp_list[5]


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
