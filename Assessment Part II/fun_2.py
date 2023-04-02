def fun(var1):
    if var1 < 1:
        return 0
    elif var1 % 2 == 0:
        fun(var1 - 1)
        print (var1)
    else:
        var1 + fun(var1 - 2)
        print (var1)
    return var1

fun(11)
fun(12)
fun(9)
fun(10)