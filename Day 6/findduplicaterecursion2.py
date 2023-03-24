def find_duplicates(list_of_numbers):
    duplicates_list = [] #Initialise duplicates list
    #Creating a set from the list. Sets allow it to be unordered and faster to check if elements exist in set
    list_set = set(list_of_numbers)
    
    for num in list_set: #The list_set only allows each number to occur only once
        count = list_of_numbers.count(num) #Count method returns how many times the number occurs in the list
        if count > 1:
            duplicates_list.append(num)
    return sorted (duplicates_list)

list_of_numbers = [1, 2, 3, 22, 33, 11, 34, 2, 34, 2, 1]
list_of_duplicates = find_duplicates(list_of_numbers)
list_of_duplicates.reverse()
print(list_of_duplicates)