"""
This checks to see if a one-hop between two cities exists by taking exactly two flights through a connection city.

The city input parameters go into the one hop function and check to see if the two citys have a destination city
in common they can hop between. If one hop is possible then it returns True and checks the returned value
in hop_check to confirm and print the answer
"""
flights = {'Montreal': ['Toronto', 'Tampa Bay'],  # this is the flight dictionary
           'Toronto': ['Montreal', 'Tampa Bay'],
           'Tampa Bay': ['Atlanta', 'Toronto'],
           'Atlanta': ['Tampa Bay']}


def one_hop(flights, city1, city2):  # function that checks to see if a one hop is possible
    try:  # defencive coding
        for x in flights[city1]:  # runs a for loop through the key for city1 value
            if city2 in flights[x]:  # checks if the two citys have a destination in common
                return True
    except KeyError:  # defencive coding
        print("city does not exist")  # error message


def hop_check(x):  # function that checks to see if the returned value is true or not and prints the result
    if x == True:
        print('yes one hop possible')
    if x != True:
        print('no one hop not possible')


x = one_hop(flights, 'Tampa Bay', 'Montreal')  # different values to test
hop_check(x)  # checks to see if the returned value is true or not
x = one_hop(flights, 'Tampa Bay', 'Toronto')
hop_check(x)
x = one_hop(flights, 'Atlanta', 'Toronto')
hop_check(x)
x = one_hop(flights, 'Atlanta', 'Tampa Bay')
hop_check(x)
x = one_hop(flights, 'Montreal', 'Toronto')
hop_check(x)
x = one_hop(flights, 'Atlanta', 'Montreal')
hop_check(x)
x = one_hop(flights, 'Toronto', 'Tampa Bay')
hop_check(x)
