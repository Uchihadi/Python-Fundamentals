#lex_auth_012693750719488000124

def get_count(num_list):
    count=0

    # Write your logic here
    # num_list
    for num in range(len(num_list) - 1):
        if num_list[num] == num_list[num + 1]:
            count += 1
        return count

#provide different values in list and test your program
num_list=[1,1,5,100,-20,-20,6,0,0]
print(get_count(num_list))