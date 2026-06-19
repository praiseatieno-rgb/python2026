# Python loops
# sometimes we may need to do a piece of code a number of times, in such case a loop maybe of importance. a loop is a control structure that helps us execute a blocl of code repeatedly until a condition is met
# In python, we have the main types of loops i.e the for loop and the while loop

# The for loop. Belo is the syntax
"""
for a variable range(n):
    block of code to be executed
"""

for greeting in range(50):
    print("Hello there", greeting)

print("====================================================")
for number in range(10, 20):
    print(number)

print("=====================================================")
# below we use some steps
for x in range(50, 71, 2):
    print(x)

print("======================================================")
# Create a program that is able to print all the numbers btwn 0 and 51
for Numbers in range(0, 51):
    print(Numbers)
