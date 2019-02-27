flights = {'Montreal': ['Toronto', 'Tampa Bay'],
           'Toronto': ['Montreal', 'Tampa Bay'],
           'Tampa Bay': ['Atlanta', 'Toronto'],
           'Atlanta': ['Tampa Bay']}


def one_hop(flights, city1, city2):
    try:
        for x in flights[city1]:
            if city2 in flights[x]:
                return True
    except KeyError:
        print("city does not exist")


def hop_check(x):
    if x == True:
        print('yes one hop possible')
    if x != True:
        print('no one hop not possible')


x = one_hop(flights, 'Tampa Bay', 'Montreal')
hop_check(x)
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
