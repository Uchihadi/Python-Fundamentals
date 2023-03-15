# Q6: Write a program that prompts the user to enter a list of numbers and then prints the sum of all the even numbers in the list.

def list_number():
    total = 0
    
    users_list = input("Please input a list of numbers: ")
    list = users_list.split()
    for i in list:
        i = int(i)
        if i % 2 == 0:
            total += i
    print(total)

list_number()