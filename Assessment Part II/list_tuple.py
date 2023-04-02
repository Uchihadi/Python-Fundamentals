try:
    tupl1 = ([1,2], [3, 4])
    list1 = [(1, 2), (3, 4)]
    list2 = tupl1 [0] #Will Overwrite List 2 but not the Tuple
    list1 [1] = (6,7)
    print(tupl1, list1)
except TypeError:
    print("Err")