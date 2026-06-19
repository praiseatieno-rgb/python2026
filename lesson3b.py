# based on the if and elif...else condition statement, we can createthe grading system as show below
marks = 57

if marks > 0 and marks < 30:
    print("the grade attached is: E")
elif marks >= 30 and marks <50:
    print("the grade attached is: D")
elif marks >= 50 and marks <60:
    print("the grade attached is: C")
elif marks >= 60 and marks <70:
    print("the grade attached is: B")
elif marks >= 70 and marks <80:
    print("the grade attached is: A")
else:
    print("Invalid entry. Please try again...")

print("=========================================")
#John went to donate blood but there are  conditions he needs to meet. A person can donate blood is that who has attained 50kgs or above and his or her age is not less than 18.Create a python program that is able to check whether john who is 57kgs and 26 years old is able to donate blood

weight = 47
age = 26

if age == 18 and weight == 50:
    print("Eligible to donate")
elif age >=18 and weight >= 50:
    print("Eligible to donate")
else:
    print("Not eligible")
    