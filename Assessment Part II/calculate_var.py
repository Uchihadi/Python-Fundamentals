# Another Recursive Function for calculate
def calculate (var1, var2):
    while (var1 != var2):
        if (var1 > var2):
            return calculate (var1 - var2, var2)
        else:
            return calculate (var2, var2 - var1)
    
    return print(var1)

calculate(10, 55) # Correct Answer: Using Recursive function, the while loop runs around 12 times before var1 = var2 then break!
calculate(60, 30) # Correct Answer: While loop runs once before var1 = var2 then break
calculate(27, 47)
calculate(45, 20)