list1 = [10, 20, 30, 40]

for num in list1:
    if num == 20:
        break #stops and exits your loop
    else:
        print(num)

for num in list1:
    print(f"Inside the for loop wtih val {num}")
    
    # The Continue will break from current iteration, goes straight to next iteration
    if num == 20:
        continue
    
    print(f"The value is {num} at the end")
    