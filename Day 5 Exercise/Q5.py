#lex_auth_01269438947391897654

#Global variable
list_of_marks=(25, 25, 25, 25, 25, 25, 25, 25, 25, 25)

def find_more_than_average():
    count = 0
    avg_marks = sum(list_of_marks) / len(list_of_marks)
    for num in list_of_marks:
        if num > avg_marks:
            count += 1
    percentage = (count / len(list_of_marks)) * 100
    return percentage
    #Remove pass and write your logic here

def sort_marks():
    sorted_ = sorted(list_of_marks)
    return sorted_

    #Remove pass and write your logic here

def generate_frequency():
    gener = [0] * 26
    for m in list_of_marks:
        gener[m] += 1
    return gener
            

print(find_more_than_average())
print(generate_frequency())
print(sort_marks())