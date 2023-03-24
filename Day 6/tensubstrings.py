#lex_auth_01269442545042227276

def find_sum(num):
    sum = 0
    for i in num:
        sum += int(i)
    return sum

def find_ten_substring(num_str):
    substring = []
    for num in range(2, len(num_str)): #Number of elements to take from num_str
        end_idx = len(num_str) - num + 1
        for j in range(0, end_idx):
            if find_sum(num_str[j:j+num]) == 10: #Take 2 numbers then return to find_sum
                substring.append(num_str[j:j+num])
    return substring
        
    #Remove pass and write your logic here

num_str="2825302" #Number sequences to be placed inside the list
print("The number is:",num_str)
result_list=find_ten_substring(num_str)
print(result_list)