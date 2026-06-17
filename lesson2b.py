# Python Tuple -is a type of a list that does not change, unmutable.
# to introduce  a tuple we use the brackets/parenthesis ()

counties = ("Nairobi", "Mchakos", "Kisumu", "Kisii", "Narok", "Mombasa", "Lamu", "Kilifi")
print(counties)
print(type(counties))

# It stores its items indexes. We also start from index zero
print(counties[4])

# slicing of tuple
print(counties[3:])

# print from machakos to mombasa
print(counties[1:6])

# Note below code will show an error. why? because a tuple is immutable
counties.append("Nakuru")
print(counties)