#lex_auth_01269441810970214471

def check_double(number):
    double = number * 2
    if len(str(double)) == len(str(number)):
        if sorted(str(double)) == sorted(str(number)):
            return True
        else:
            return False
    else:
        return False
    #Remove pass and write your logic here

#Provide different values for number and test your program
print(check_double(9))