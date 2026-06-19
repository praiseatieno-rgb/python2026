# Create a python program to check;
#  when the age is less than 10 the program should print "you are in Primary Classes",
#  More than 12 and less than 15 the program should print "You are in Junior Secondary",
#  more than 15 and less than 19 the program should print "You are in Senior Secondary",
#  more than 19 the program should print "you are in College"


age = 17

if age < 10:
    print("You are in Primary Classes")
elif age > 12 and age < 15:
    print("You are in Junior Secondary")
elif age > 15 and age < 19:
    print("You are in Senior Secondary")
else:
    print("You are in College")