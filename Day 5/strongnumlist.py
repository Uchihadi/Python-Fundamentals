#lex_auth_01269437118923571233

def factorial(number):
    if number == 1:
        return number
    elif number == 0:
        return 1
    else:
        factorial_num = (number * factorial (number - 1))
        return factorial_num
#remove pass and write your logic to find and return the factorial of given number


def find_strong_numbers(num_list):
    strong_num = []
    for num in num_list:
        temp = str(num)
        answer = 0
        for i in temp:
            answer += factorial(int(i))
        if num == answer:
            strong_num.append(num)
    return strong_num


num_list=[145,375,100,2,10]
strong_num_list=find_strong_numbers(num_list)
print(strong_num_list)