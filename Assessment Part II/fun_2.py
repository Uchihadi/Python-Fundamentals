# Using Recursive functions
def fun(var1):
    if var1 < 1:
        return 0
    elif var1 % 2 == 0: #If var1 is 10, it will return var1(9)
        return fun(var1 - 1)
    else:
        return var1 + fun(var1 - 2) #If var1(9) then it will add an increment of -2 hence
    # 9 + 7 + 5 + 3 + 1

# fun(11)
# fun(12)
fun(9)
fun(10)