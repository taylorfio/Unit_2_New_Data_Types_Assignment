"""
It will guess 2 if there is not enough information or if there is a tie
next questions are "mind read"
have history of guesses in list
.insert(0) each new entery at front of list

use tuples to store options for history
"""

your_points = 0
bot_points = 0


while your_points < 30 and bot_points < 30:

    your_input = input("1 or 2")
    if your_input != "1" or your_input != "2":
        while your_input != "1" or your_input != "2":
            print("error")
            your_input = input("1 or 2")



