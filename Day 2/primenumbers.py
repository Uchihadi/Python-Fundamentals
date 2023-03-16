print("Prime numbers")
number2=int(input("Please enter your number:"))
print("Prime numbers between 1 and",number2,"are:")
for number2 in range(1,number2+1):
    if number2 >=1:
        for a in range(2,number2):
            if( number2 % a)==0:
                break
        else:
            print(number2)