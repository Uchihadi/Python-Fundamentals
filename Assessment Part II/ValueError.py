def func (var1, var2):
    try:
        var3 = (int) (var1)
        var2 = var3 + "A" #Results in ValueError
        print (var2)
    except TypeError: #Since it is not a TypeError, it will be caught at finally statement
        print("T")
    finally:
        print("IF")

try:
    func("R", 13)
except ValueError:
    print("V")
finally:
    print("OF")