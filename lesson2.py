#Boolean data type
# Is a data type that evaluates to either true or false

israining = False
print(israining)
print(type(israining))

paidloan = "True"
print(paidloan)
print(type(True))

#Python list data type
#a list is a collection of items that are ordered in a certain way .
#a list in python is introduced by the use of the []
#the items of list are stored inside of indexes. Note: In programming indexes starts 
# from idex zero (0)
# A list can bemuted i.e the content of a list can be changed. e.g

cars = ["BMW", "Benz", "Prado", "Ranger", "Probox", "Rover"]
print(cars)
print(type(cars))

# Accessing items of a list
# We use the indexes to access the item
print("The car on index zero is:",cars[0])
print("The car on index five is:",cars[5])

# List Slicing - this is creating a list from an already existing list
print(cars[4:])

#example 2
print(cars[0:4])

#example 3
print(cars[3:6])

#List mutability 
# we use the append function to add an item at the end of the list
cars.append("Mercedes")
print(cars)

cars.append("Subaru")
print(cars)


# we use the pop function to remove items at the end of the list
cars.pop()
print(cars)

#we can replace an item on a certain index as shown below
cars[0] = "Pajero"
print(cars)

#below we use the del function to delete an item in a certain index
del cars[4]
print(cars)

#check out on remove, sort functions on a list
