def add(num1, num2):
    num3 = num1 + num2
    print(num3)
    return num3

output = add (2, 4)

print(output)

def sub(num4, num5):
    num6 = num4 - num5
    print(num6)
    return num6

# to define the num as values
output1 = sub (num5 = 2, num4 = 4)

print(output1)

def mul(num7, num8):
    num9 = num7*num8
    print(num9)
    return num9

output2 = mul(2, 4)

print(output2)

def adds(*nums):
    sums = 0
    for number in nums:
        sums = sums + number
        
    print(sums)
    
adds(10, 20, 30)