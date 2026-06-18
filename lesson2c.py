# Dictionary Data type
# Is a data type that storesits data in form of key -value pairs
#it is introduced by the use of the curly braces {}
#the value stored in side of a dictionary can be different data type i.e int, tuple, string
#list, dictionart
# Note unlike in tuple and list, on the dictionary we nomarmaly use the keys to access the value.
#the keys and the values are separeted from each other bythe use of full colon(:). At the end of each pair there should be a comma.

#example one
phonebook = {
    "Benson" : 254706428006,
    "Mary" : 254709857434,
    "Joseph" : 24567980345
}

print("My dictionary is:", phonebook)
print(type(phonebook))

# Below we use the following to access the items of the dictionary
print(phonebook["Benson"])
print(phonebook["Mary"])

print("======================================================================")

player = {
    "Name" : "Messi",
    "age" : 40,
    "teams" : ["Miami", "PSG", "Barcelona", "Argentina"],
    "more" : {
        "children" : 3,
        "residence" : "US",
        "phone" : (254768759463, 254790786534,223792563844)
    }
}

print("The name of the player is:", player["Name"])
print("The player's team is:",player["teams"][2])
print("The players number:",player["more"]["phone"][1])