var1, var2 = 10, 40
def func1(var1):
    global var2
    var1, var2 = 20, 50
    print(var1, end=" ")
    print(var2, end=" ")
func1 (30)
print(var1, end= " ")
print(var2, end= " ")