# Q4: Write a program that prints all the prime numbers between 1 and a given number.

num = int(input("Enter a number: "))

def prime_num(num):
    prime_list = []
    for i in range(1,num):
        for j in range(2, int(i/2)+1):
                if i % j == 0:
                    break
        else:
                prime_list.append(i)
    return prime_list

print(prime_num(num))
    
        
        