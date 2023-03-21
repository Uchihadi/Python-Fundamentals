#lex_auth_01269438947391897654

#Global variable
list_of_marks=(12,18,25,24,2,5,18,20,20,21)

def find_more_than_average():
    count = 0
    avg_marks = sum(list_of_marks) / len(list_of_marks)
    for num in list_of_marks:
        if num > avg_marks:
            count += 1
            percentage = count / len(list_of_marks) * 100
    return percentage
    #Remove pass and write your logic here

def sort_marks():
    sorted_ = tuple(sorted(list_of_marks))
    return sorted_

    #Remove pass and write your logic here

def generate_frequency():
    pass
    #Remove pass and write your logic here

print(find_more_than_average())
print(generate_frequency())
print(sort_marks())