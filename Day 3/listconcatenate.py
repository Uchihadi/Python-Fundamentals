#lex_auth_01269441913243238467

def create_largest_number(number_list):
    
    #remove pass and write your logic here
    number_list.sort() #sorting in ascending order
    number_list.reverse()
    numbers = " " #Initialise the numbers
    
    for i in number_list:
        numbers += str(i) #str i concatenates to the left
    return numbers
    
number_list=[23,45,67]
largest_number=create_largest_number(number_list)
print(largest_number)