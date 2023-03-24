def find_duplicates(list_of_numbers):
    # Base Code: Once the list reaches the end or no more list avail, returns empty string
    if len (list_of_numbers) == 0 or len (list_of_numbers) == 1: #If the length of the list is left with 0/1
        return [] #Returns empty string as specified by Question
    else:
        first_element = list_of_numbers[0]
        rest_of_the_list = list_of_numbers[1:] #Slicing the rest of elements
        
        # print(f"The first element is {first_element} and rest of the list is {rest_of_the_list}")
        duplicates = find_duplicates(rest_of_the_list)
        
        if first_element in rest_of_the_list and first_element not in duplicates:
            # print(f"Appending {first_element}")
            duplicates.append(first_element)
            
    return duplicates

list_of_numbers = [1, 2, 3, 22, 33, 11, 34, 2, 34, 2, 1]
list_of_duplicates = find_duplicates(list_of_numbers)
list_of_duplicates.reverse()
print(list_of_duplicates)