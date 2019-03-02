"""
while both the scores is less then 30 the game goes on. When it starts and there is insufficient history the computer
automatically picks 2. When you input your choice the dictionary of tuples is read and it finds the higher number from
the tuple to guess. When the bot has a history of three choices it will pick its choice based off the majority choice.
"""
tup_dict = {
    '1': (1, 1, 1),  # creates a dictionary with all the potential options for the history
    '2': (1, 2, 1),
    '3': (2, 1, 1),
    '4': (1, 1, 2),
    '5': (2, 2, 2),
    '6': (2, 1, 2),
    '7': (1, 2, 2),
    '8': (2, 2, 1)}

history_list = []  # states variables
bot_choice = 0
user_points = 0
bot_points = 0

while user_points < 30 and bot_points < 30:  # a while loop for the amount of points in a game
    if len(history_list) < 3:  # chooses 2 if the choice history is less then 3
        bot_choice = 2
    else:
        for x in tup_dict:  # loops through the dictionary
            if tuple(history_list) == tup_dict[x]:  # finds the tuple that matches the history
                list1 = []  # states the variables
                list2 = []
                for num in tup_dict[x]:  # loops through the tuple
                    if num == 1:  # if the variable is equal to a number it adds something to its list
                        list1.append(0)
                    if num == 2:
                        list2.append(0)
                if len(list1) > len(list2):  # counts the lists for each number and determines the bots choice
                    bot_choice = 1
                if len(list2) > len(list1):
                    bot_choice = 2

    your_input = input("1 or 2: ")  # takes your input
    while your_input != "1" and your_input != "2":  # defencive coding
        print("error")
        your_input = input("1 or 2: ")

    your_input = int(your_input)  # makes input a number
    history_list.insert(0, your_input)  # adds the number to the front of the list
    if len(history_list) == 4:  # deletes the number in the last position if the length is more then 3
        history_list.pop(3)
    if your_input == bot_choice:  # if you choose the same thing as the bot it gets a point
        print("incorrect")
        bot_points = bot_points + 1
    if your_input != bot_choice:  # if you don't choose the same thing as the bot you get a point
        print("correct")
        user_points = user_points + 1
    #print(history_list) #use to check history during testing

if bot_points > user_points:  # if the bot gets 30 points this prints
    print('Computer Wins')
    print("")
    print("  , ; ,   .-'---'-.   , ; ,")
    print("  \\|/  .'         '.  \|//")
    print("   \-;-/   ()   ()   \-;-/")
    print("   // ;               ; \ \ ")
    print("  //__; :.         .; ;__\ \ ")
    print(" `-----\'.'-.....-'.'/-----' ")
    print("        '.'.-.-,_.'.' ")
    print("          '(  (..-' ")
    print("            '-' ")

if user_points > bot_points:  # if you get 30 points this prints
    print('You Win')
    print("")
    print("         ___________")
    print("       '._==_==_=_.'")
    print("       .-\:      /-.")
    print("      | (|:.     |) |")
    print("       '-|:.     |-'")
    print("         \::.    /")
    print("          '::. .'")
    print("            ) (")
    print("          _.' '._")
    print("         `--------` ")
