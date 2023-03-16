#3 numbers can be sides of triangle if none are greater / equal to sum of 2 other numbers
#lex_auth_012693802383794176153

def form_triangle(num1,num2,num3):
    #Do not change the messages provided below
    success="Triangle can be formed"
    failure="Triangle can't be formed"
    
    if num1 >= num2 + num3:
        return failure
    elif num2 >= num1 + num3:
        return failure
    elif num3 >= num1 + num2:
        return failure
    else:
        return success

    #Write your logic here

    #Use the following messages to return the result wherever necessary
    return success
    return failure

#Provide different values for the variables, num1, num2, num3 and test your program
num1=3
num2=3
num3=5
form_triangle(num1, num2, num3)