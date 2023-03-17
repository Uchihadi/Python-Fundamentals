#lex_auth_012693813706604544157

def find_max(num1, num2):
    max_num=-1
    
    # Write your logic here
    if (num1 < num2):
        for i in range(num1, num2+1, 1):
            if (i%5 == 0 and i < 100):
                sum_digit = 0
                j = i
                while (j != 0):
                    remainder = j % 10
                    sum_digit += remainder
                    j //= 10
                if (sum_digit % 3 == 0):
                    max_num = i
            
    return max_num

#Provide different values for num1 and num2 and test your program.
max_num=find_max(15,12)
print(max_num)