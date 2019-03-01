"""

"""
tup_dict = {
    '1': (1, 1, 1),
    '2': (1, 2, 1),
    '3': (2, 1, 1),
    '4': (1, 1, 2),
    '5': (2, 2, 2),
    '6': (2, 1, 2),
    '7': (1, 2, 2),
    '8': (2, 2, 1)}

history_list = []
bot_choice = 0
user_points = 0
bot_points = 0

while user_points < 30 and bot_points < 30:
    if len(history_list) < 3:
        bot_choice = 2
    else:
        for x in tup_dict:
            if tuple(history_list) == tup_dict[x]:
                list1 = []
                list2 = []
                for num in tup_dict[x]:
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
    #print(history_list) #use to check history

if bot_points > user_points:
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

if user_points > bot_points:
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
