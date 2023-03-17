# Write a python program to find and display the product of three positive integer values
#lex_auth_012693711503400960120

def find_product(num1,num2,num3):
    if num1 == 7:
        product = num2 * num3
    elif num2 == 7:
        product = num3
    elif num3 == 7:
        product = -1
    else:
        product = num1 * num2 * num3
    #write your logic here
    return product

#Provide different values for num1, num2, num3 and test your program
product=find_product(1, 5, 7)
print(product)