#lex_auth_01269437527007232044

def human_pyramid(no_of_people):
    #remove pass and place the recursive code the you had written earlier for this function
    if (no_of_people == 1):
        return 1*50
    else:
        return no_of_people*50 + human_pyramid(no_of_people - 2)

def find_maximum_people(max_weight):
    #write your logic here. You may invoke recursive function human_pyramid() wherever applicable
    no_of_people = 1
    while True:
        weight = human_pyramid (no_of_people)
        
        if weight <= max_weight:
            no_of_people +=2
        else:
            break
 
    return no_of_people - 2

#Provide different values for max_weight and test your program
max_people=find_maximum_people(1000)
print(max_people)