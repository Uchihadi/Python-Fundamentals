#lex_auth_01269438594930278448

def find_pairs_of_numbers(num_list,n):
    
    # Remove pass and write your logic here
    # Accepts a list of positive integers with no repetitions
    # Returns count of pairs of numbers in the list that adds up to n
    
    count = 0
    # Using a set to store numbers in the list
    set_num = set(num_list)
    
    for num in num_list:
        if n - num in set_num and n - num != num:
            count += 1
    
    return count // 2
    
    # for num1 in num_list:
    #     for num2 in num_list:
    #         if num1 + num2 == n:
    #             count += 1
    
    # return count

num_list=[1, 2, 4, 5, 6]
n=6
print(find_pairs_of_numbers(num_list,n))