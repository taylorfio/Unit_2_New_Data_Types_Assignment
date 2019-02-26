flights = {'Montreal': ['Toronto', 'Tampa Bay'],
           'Toronto': ['Montreal', 'Tampa Bay'],
           'Tampa Bay': ['Atlanta', 'Toronto'],
           'Atlanta': ['Tampa Bay']}

def one_hop (flights_input, city1, city2):
    """flights is a flight dictionary. city1 and city2 are keys in flights.
    Return True if and only if there is at least one one-hop from city1 to
    city2."""

    if flights_input[city1 or city2]:
        if city1 or city2 in flights:
            print(flights[city1] or flights[city2])
    else:
        print("none found")

flights_input = input("what flight do you want to check?    ")
if flights_input in flights:
    city1 = flights.get(flights_input[0])
    city2 = flights.get(flights_input[1])
    print(city1)
    print(city2)

    one_hop(flights_input, city1, city2)

if flights_input not in flights:
    print("not found")
