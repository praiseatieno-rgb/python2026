#comparion/Relation operators
#These are operators that are used to compare/relate different condition and they usually evaluate to a boolean value(true/false)
#they are six in total i.e (> < >= <= == !=)

print(5>2)
print(5<2)
print(5>=2)
print(5<=2)
print(5==2)
print(5!=2)

# Logical operations
# Logical AND - This is to evaluate to true only if both or all of the conditions are true
print((5<2) and (5>3))

# Logical OR operations
#this evaluates to true if one of the statement/condition is true
print((5<2)or(5>3))

# Logical NOT
#used to nagete a statement /condition (if the anser is true it turns out to be false and vise versa)
print(not(5>2))

print("=================================================================================================================")
#if...else conditional statement
#this is a conditional statement that is used to avaluate a condition and if it is met, the if block execute otherwise the else block gets executed.

number = -10

if number > 0:
    print("the number is positive")
else:
    print("the number is negative")


    print("================================================================")
    #create a python program that is able to evaluate whether a number is even or an odd number.

    number2 = 7
if number2 % 2 == 0:
    print("number is an odd number")
else:
    print("number is an odd number")

    print("===============================================================")
    #if... elif...else conditional statement
    # we use the above to evaluate multiple connection
    mynumber = -8

if mynumber> 0:
    print("the number is positive")
elif mynumber == 0:
    print("the number is zero")
else:
    print("the number is negative")

print("=====================================")
# create a phython program that is able to check based on the age whether a person is eligible to vote or not. If he is eligible to vote print("you can vote"), else print("you can not be allowed to vote"). A person is able to vote if he is above of age 18.
 
Age = 19

if Age >= 18:
  print("you can vote")
else:
 print("you can not be allowed to vote")