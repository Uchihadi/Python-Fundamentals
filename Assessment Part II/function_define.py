list1= [10, 20, 0, 40, 0]
def test():
    try:
        var1 = 3
        if (list1[var1]/list1[var1+1] > 1):
            value = var1 + 1
    except ZeroDivisionError:
        print("1")
    except IndexError:
        print("2")
    finally:
        print("4")
    print("5")
test()