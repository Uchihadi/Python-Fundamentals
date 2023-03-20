

def make_amount(rupees_to_make,no_of_five,no_of_one):
    five_needed = 0
    one_needed = 0 
    
    # only use the max no_of_five that you have
    remaining = rupees_to_make
    for i in range(no_of_five):
        if remaining < 5:
            break
        
        remaining = remaining - 5
        five_needed = five_needed + 1
    
    # after considering all the fives, consider ones
    if remaining > 0:
        if (remaining <= no_of_one):
            print("No. of Five needed :", five_needed)
            print("No. of One needed  :", remaining)
        elif (remaining > no_of_one):
            print(-1)
        else:
            print(-1)
    # remaining = 0
    else:
        if (five_needed * 5 == rupees_to_make):
            print("No. of Five needed :", five_needed)
            print("No. of One needed  :", remaining)
        else:
            print(-1)

make_amount(100,21,5)