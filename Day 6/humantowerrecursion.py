#lex_auth_01269437527007232044

def human_pyramid(no_of_people):
    #remove pass and place the recursive code the you had written earlier for this function
    if (no_of_people == 1):
        return 1*50 #Once the count reaches here (1), it will jump to the next function
    else:
        return no_of_people*50 + human_pyramid(no_of_people - 2) #The count reduces by 2 due to recursive function that loops back to this function

def find_maximum_people(max_weight):
    #Write your logic here. You may invoke recursive function human_pyramid() wherever applicable
    no_of_people = 1 #Initialise the no. of people
    
    while True: #Function is always True
        weight = human_pyramid (no_of_people) #The no_of_people loops around the While statement
        
        if weight <= max_weight:
            no_of_people +=2 #Increments no of ppl by 2, as only odd numbers can be considered
        else:
            break
 
    return no_of_people - 2

#Provide different values for max_weight and test your program
max_people=find_maximum_people(1000)
print(max_people)