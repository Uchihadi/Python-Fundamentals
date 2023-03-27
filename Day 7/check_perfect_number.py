#lex_auth_01269446533799116898
import math

def check_perfect_number(number):
    sum = 0
    for i in range(1, number): #For Loop to generate numbers
        if (number % i == 0): #For each iteration, number is divisible with no remainder
            sum += i
    
    if sum == number and number != 0:
        return True
    else:
        return False
    #start writing your code here

def check_perfectno_from_list(no_list):
    perfect_list = []
    for i in no_list:
        if check_perfect_number(i):
            perfect_list.append(i)
    
    return perfect_list            
    #start writing your code here

perfectno_list=check_perfectno_from_list([87, 76, 567, 99, 0])
print(perfectno_list)