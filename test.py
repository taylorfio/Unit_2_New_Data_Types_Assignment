"""
Tuples hold data much like a list
Tuples are immutable objects
- Immutable means they cannot be changed or updated
- Once you create it, that’s the way it stays
- Created using () OR no brackets
"""
Tuple1 = (“hello”, “world”)
Tuple2 = “hello”, “world”
# Tuple1 and Tuple2 are equal to the same object

"""
Tuples are ordered - they have index values
Tuples are accessed like all other lists, with square brackets
"""
ex/ print(tuple1[3])

empty_tuple = ()
# This creates an empty tuple

One_tuple = (3,)
# This creates a tuple with one item
# There must be a comma after the value

ex_tuple = ("t", "h", "a")
for i in ex_tuple:
   print(i)
# This is the same as the other lists

# If a value within the tuple is mutable (ex/ a list or dictionary) then that value can be modified
# ex/
ex_tuple = ("t", "h", [3,4])
ex_tuple[2].append(5)


_____________________________________________________________________________________________________


example_dictionary = {"year": 2019, "maker": "Honda", "4door": True}
print(example_dictionary["year"])  #prints 2019
example_dictionary["type"] = "civic type r" #creates the key "type" and adds the value “civic type r” to it
del example_dictionary["year"] #removes {“year”:2019} from the dictionary

# A data structure that holds items based on a key-value pair
# Created like:
dict1 = {
    “key1”: <value>,
    “key2”: <value>
}
# Accessed like:    dict1[“key1”]
# Key values are changes like : dict1[“key2”] = 37
# Key-value pairs are deleted like: del dict1[“key1”]

dict1["key3"] = {“A”: [3,4,5]}
dict1["key4"] = {"Toronto":"Raptors", "Golden State":"Warriors"}

dict1[True] = "yes"
print(dict1[True]) #prints "yes"
dict1[37] = 100

if 37 in dict1:
    ""
"""
.clear() - deletes all contents of a dictionary
.items() - returns all key, value pairs
.get(key) - returns the value for the passed key
.keys() - returns a list of all keys, use list()
    ex/ list(dict1.keys())
.values() - returns a list of all values, use list()
    ex/ list(dict1.values())
"""

# len() also works with Dictionaries**

# We can loop through a dictionary much like a list.
for x in dict1:
   print(x)
# This would print every key in the list (not key-value pair)
_____________________________________________________________________________________________________

