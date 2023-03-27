#For generating the nearest palindrome of a number also we will be using the slicing operator
#The nearest palindrome of a given number is obtained by adding 1 to the number until it is a palindrome.
#This is done by using a while loop recursively
#When the condition is met, the number is given as output

def nearest_palindrome(number):
    while (1): #Looping to keep on adding 1 till palindrome
        if number == int(str(number)[::-1]) and number >= 100: #Palindrome Formula
            return number
        number += 1

    #start writitng your code here

#We typecast the integer to string because we cannot use the slice operator on an integer
#We typecast the string to an integer because we have to iterate the loop further by adding 1 if it is not a palindrome

number = 0
print(nearest_palindrome(number))