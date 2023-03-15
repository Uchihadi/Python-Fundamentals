name = "Hadi"
a = "Diyanah"

print ("Diyahnah", name, a)

name = input("Please enter your name: ")
print(name)

age = input("Please enter your age: ")
# Values return from input function will always be strings
# Create an integer from the values returned from the input

# You can use the same variables (as it will override) or declare new variable
age = int(age) + 10
print(age)

age1 = int(input("Check Eligibility: "))

# Python does not have parentheses {} but rather colon : for if else statement
if age1 > 18:
    print("Eligible to Vote")
elif age1 == 18: #Comparing the values
    print ("Congrats you are eligible to vote")
else:
    print("Not eligible to vote")