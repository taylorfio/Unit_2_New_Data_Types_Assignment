"""
the file with all the information read and added to a dictionary. Then the users input is used to search for
the information that match's it. Then your searched information creates a list of the info to print
"""
the_list = []  # stating variables
student_dictionary = {}
repeat = True

try:
    file = open('studentinfoText.txt', 'r')  # opens the text file with all the information
    file_list = file.readlines()  # reads the file per line
    for line in file_list:  # creates a 2d list for all the information from the text file
        for item in line.split():
            the_list.append(item.split(","))
    for x in range(len(the_list)):  # creates multiple keys using the values for the same information
        for y in the_list[x]:
            if y not in student_dictionary:  # checks if the information is in the dictionary and adds it if it isn't
                student_dictionary[y] = the_list[x]
            elif y in student_dictionary:
                student_dictionary[y] = student_dictionary[y], the_list[x]
except IOError:
    print("error 404 / files not found")  # defencive coding

while repeat == True:  # loop that repeats until you tell to to stop
    def delete_fun(input):  # function that checks if the input is a pass or information and if so adds it to a list
        if input != "":
            temp_list.append(input)
    temp_list = []
    print("if you dont want to enter a value press enter")
    fname_input = input("enter fname value")  # input to search the dictionary with
    delete_fun(fname_input)
    lname_input = input("enter lname value")
    delete_fun(lname_input)
    grade_input = input("enter grade value")
    delete_fun(grade_input)
    house_input = input("enter house value")
    delete_fun(house_input)
    adviser_input = input("enter adviser value")
    delete_fun(adviser_input)
    print("searching for", temp_list)  # prints what you inputted
    search_list = []

    try:
        for x in temp_list:
            if student_dictionary[x]:  # checks if there are duplicates of the information
                if x not in search_list:  # doesn't add the same thing more then once
                    search_list.append(student_dictionary[x])
        print("your results are ")

        if len(search_list) == 1:  # if only one item is being searched then it just prints out the corresponding keys
            print(search_list)  # make normal and separate lines

        if len(search_list) > 1:  # if more then one item is being searched
            result_list = []
            for x in range(len(search_list)):  # for loop the length of the about of items being searched
                for y in search_list[x]:
                    counter = 0  # resets counter
                    for item in temp_list:  # for loop for the amount of items in the list
                        if item in y:  # checks if the item is in the list
                            counter = counter + 1  # increases counter
                    if counter == len(temp_list):  # if the length of the counter is the same as the list
                        if y not in result_list:  # only prints if it hasn't been added to the list yet
                            result_list.append(y)
                            print(', '.join(y))  # prints results
    except KeyError:
        print("input error")  # defencive coding

    repeat_input = input("do you want to search? [y/n]")  # input for if you want to restart or not
    if repeat_input != 'n' and repeat_input != 'y':  # defencive coding
        while repeat_input != 'n' and repeat_input != 'y':
            print("error")
            repeat_input = input("do you want to search? [y/n]")
    if repeat_input == 'n':  # stops loop
        repeat = False
