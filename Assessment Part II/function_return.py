def func1():
    try:
        1/0 #ZeroDivisionError
        return 1
    except ZeroDivisionError:
        "ABC" + 1 #TypeError
        return 2
    finally:
        int("A") #Value Error
        return 3

try:
    result = func1() #ValueError; If the entire function returns an error even at finally, it will go to exception block
    print(result)
except:
    print(4)