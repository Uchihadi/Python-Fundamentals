#lex_auth_0127382164803993601239

#This verification is based on string match.

def sum_of_numbers(list_of_num,filter_func=None):
    sum_func = 0
    
    if filter_func == even:
        lst1 = even(list_of_num)
        for i in lst1:
            sum_func += i
    elif filter_func == odd:
        lst2 = odd(list_of_num)
        for i in lst2:
            sum_func += i
    else:        
        lst3 = list_of_num
        for i in lst3:
            sum_func += i
    return sum_func

def even(data):
    even_list = []
    for num in data:
        if num % 2 == 0:
            even_list.append(num)
    return even_list
     #Remove pass and write the logic here

def odd(data):
    odd_list = []
    for num in data:
        if num % 2 != 0:
            odd_list.append(num)
    return odd_list
    #Remove pass and write the logic here

sample_data = range(1,11)

print(sum_of_numbers(sample_data,None))