#lex_auth_01269442760027340879

def find_divisors(num):
    divisors = [] #Initialising an empty list for divisors
    for i in range (1, num + 1): #It is a start (1) and end value @ num
        if num % i == 0:
            divisors.append(i)
    return len(divisors) #Returns the length of the list

def find_smallest_number(num):
    #start writing your code here
    for i in range (2, 1000): #Running a for-loop from start to end
        if find_divisors(i) == num: #Runs another function to find list of divisors
            return i

num = 16
print ("The number of divisors :", num)
result = find_smallest_number (num)
print ("The smallest number having", num," divisors:", result)