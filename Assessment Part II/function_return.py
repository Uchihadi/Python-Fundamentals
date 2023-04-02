def func1():
    try:
        1/0
        return 1
    except ZeroDivisionError:
        "ABC" + 1
        return 2
    finally:
        int("A")
        return 3

try:
    result = func1() #ValueError; If the entire function returns an error even at finally, it will go to exception block
    print(result)
except:
    print(4)