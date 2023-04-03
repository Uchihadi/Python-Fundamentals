def fun(var1):
    if var1 < 1:
        return 0
    elif var1 % 2 == 0:
        return fun(var1 - 1)
    else:
        return var1 + fun(var1 - 2)

fun(11)
fun(12)
fun(9)
fun(10)