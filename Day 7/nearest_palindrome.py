#lex_auth_01269443664174284882
def nearest_palindrome(number):
    temporary = number
    rev = 0
    while (number > 0):
        digits = number % 10
        rev = (rev * 10) + digits
        number = number // 10
    
    if (rev == temporary):
        return True
    else:
        return False
    #start writitng your code here

number=12321
print(nearest_palindrome(number))