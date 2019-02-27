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
                student_dictionary[y] = the_list[x]  # overwrites values that already exist need to check and if exist then append
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
    holder_list = []
    for x in temp_list:
        if student_dictionary[x]:
            if x not in holder_list:
                holder_list.append(student_dictionary[x])

    print("your results are ")
    for x in range(len(holder_list)):
        for y in holder_list[x]:
            counter = 0
            for item in temp_list:
                if item in y:
                    counter = counter + 1
            if counter == len(temp_list):
                print(y)


    repeat_input = input("do you want to search? [y/n]")
    if repeat_input == 'n':
        repeat = False
