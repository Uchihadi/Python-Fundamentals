#lex_auth_01269446319507046499

def remove_duplicates(value):
    duplicate = [] # Initialise a list for duplicates
    no_duplicate = [] # Initialise a list for non-duplicates
    no_duplicate_string = "" # Initialise a string for non-duplicates
    
    for i in range (0, len(value)):
        duplicate.append(value[i]) # Creating a list for duplicates
    
    for i in duplicate:
        if i not in no_duplicate:
            no_duplicate.append(i) # Appending a list of no duplicates in duplicates
        
    for i in no_duplicate:
        no_duplicate_string += i #Adding each element to make it a string

    return no_duplicate_string
    #start writing your code here

print(remove_duplicates("222233435657uwqtqasda!"))