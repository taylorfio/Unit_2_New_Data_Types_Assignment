"""
"""
tup_list = []
tup1 = (1, 1, 1)
tup2 = (1, 2, 1)
tup3 = (2, 1, 1)
tup4 = (1, 1, 2)
tup5 = (2, 2, 2)
tup6 = (2, 1, 2)
tup7 = (1, 2, 2)
tup8 = (2, 2, 1)
tup_list.append(tup1)
tup_list.append(tup2)
tup_list.append(tup3)
tup_list.append(tup4)
tup_list.append(tup5)
tup_list.append(tup6)
tup_list.append(tup7)
tup_list.append(tup8)

temp_tup = []
history_list = []
bot_choice = 0
user_points = 0
bot_points = 0

while user_points < 30 and bot_points < 30:
    if len(history_list) < 3:
        bot_choice = 2
    else:
        for x in tup_list:
            if history_list == tup_list[x]:  # how to get this to work
                tup_list[x] = temp_tup

                print(temp_tup)  # del later

                list1 = []
                list2 = []
                for num in temp_tup:
                    if num == 1:
                        list1.append(0)
                    if num == 2:
                        list2.append(0)
                if len(list1) > len(list2):
                    bot_choice = 1
                if len(list2) > len(list1):
                    bot_choice = 2

    your_input = input("1 or 2: ")
    while your_input != "1" and your_input != "2":
        print("error")
        your_input = input("1 or 2: ")

    your_input = int(your_input)
    history_list.insert(0, your_input)
    if len(history_list) == 4:
        history_list.pop(3)
    if your_input == bot_choice:
        print("incorrect")
        bot_points = bot_points + 1
    if your_input != bot_choice:
        print("correct")
        user_points = user_points + 1

if bot_points > user_points:
    print('Computer Wins')
elif user_points > bot_points:
    print('You Win')
