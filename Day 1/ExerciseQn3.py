# Q3: Write a program that calculates the factorial of a number.
num = int(input("Enter a number: "))

# Initialise Factorial
factorial = 1

if num < 0:
    print ("Sorry the number is invalid")
elif num == 0:
    print ("Factorial of 0 is 1")
else:
    for i in range (1, num+1):
        factorial*=i
        i+=1
        # Factorial initialises at 1, i increments by 1 for every for loop hence each factorials will keep increase after every for loop

print (factorial)