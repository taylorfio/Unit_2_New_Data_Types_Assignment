"""
It will guess 2 if there is not enough information or if there is a tie
next questions are "mind read"
have history of guesses in list
.insert(0) each new entery at front of list

use tuples to store options for history
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
print(tup_list)

temp_tup = []
history_list = []
user_points = 0
bot_points = 0
while user_points < 30 and bot_points < 30:
    if len(history_list) < 3:
        bot_choice = 2
    else:
        for x in tup_list:
            if history_list == tup_list[x]:
                tup_list[x] = temp_tup
                print(temp_tup)
                for x in temp_tup:
                    print(x)


    your_input = input("1 or 2")
    if your_input != "1" or your_input != "2":
        while your_input != "1" or your_input != "2":
            print("error")
            your_input = int(input('1 or 2: '))
        if your_input == "1":
            ""
        if your_input == "2":
            ""
        


















































"""
c_score = 0
u_score = 0
guessed = []
while (c_score != (30 or 31)) or (u_score != (30 or 31)):
    c_choose = 2
    u_number = int(input('1 or 2: '))
    guessed.append(u_number)
    if len(guessed) > 3:
        last = [guessed[len(guessed) - 1], guessed[len(guessed) - 2], guessed[len(guessed) - 3]]
        if sum(last) == (3 or 4):
            c_choose = 2
        else:
            c_choose = 1
    if c_choose == u_number:
        c_score += 1
        print('correct')
    if c_choose != u_number:
        u_score += 1
        print('In-correct')
if c_score > u_score:
    print('Computer Wins')
elif u_score > c_score:
    print('You Win')
"""