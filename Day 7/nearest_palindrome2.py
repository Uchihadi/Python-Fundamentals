#lex_auth_01269443664174284882
def nearest_palindrome(number):
    string_num = str(number) #Stringify the number
    if string_num == string_num[::-1]: #Formula for palindrome
        return number
    else:
        number += 1
        return nearest_palindrome(number) #Goes back to the function if the formula palindrome is not met

    #start writitng your code here
number = 12300
print(nearest_palindrome(number))