def func1 ():
    try:
        dict1 = {"IN": "India", "US": "United States"}
        del dict1["IN"]
        value = 100 // (len(dict1 - 1))
        print(value)
    except ZeroDivisionError:
        print("ZD", end =" ")
        value = int(dict1[0])
    except KeyError:
        print("KE", end = " ")
    finally:
        print("FI", end = " ")

try:
    func1()
    print("TR")
except:
    print("CA")