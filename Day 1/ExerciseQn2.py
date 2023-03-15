# Q2: Write a program that checks if a number is even or odd. Print "even" if the number is even and "odd" if the number is odd.
num = int(input("Enter a number: "))

if num <= 0:
    print ("Sorry number is invalid")
elif num % 2 != 0:
    print ("odd")
else:
    print ("even")

