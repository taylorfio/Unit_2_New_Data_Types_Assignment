flights = {'Montreal': ['Toronto', 'Tampa Bay'],
           'Toronto': ['Montreal', 'Tampa Bay'],
           'Tampa Bay': ['Atlanta', 'Toronto'],
           'Atlanta': ['Tampa Bay']}

def one_hop (flights_input, city1, city2):
    """flights is a flight dictionary. city1 and city2 are keys in flights.
    Return True if and only if there is at least one one-hop from city1 to
    city2."""

    if flights_input[city1 or city2]:  # string indices must be integers?
        for city1 in flights:
            print(flights[city1])
        for city2 in flights:
            print(flights[city2])
    else:
        print("none found")


repeat = True
while repeat == True:
    flights_input = input("what flight do you want to check?    ")
    if flights_input in flights:
        citys = flights.get(flights_input)
        city1 = citys[0]
        city2 = citys[1]
        print(city1)
        print(city2)
        one_hop(flights_input, city1, city2)

    elif flights_input not in flights:
        print("not found")
    else:
        print("brokeoz")

    repeat_input = input("do you want to search? [y/n]")
    if repeat_input == 'n':
        repeat = False
