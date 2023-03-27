#lex_auth_01269446319507046499

def remove_duplicates(value):
    no_duplicate = []
    no_duplicate_string = ""
    
    for i in range (0, len(value)):
        no_duplicate.append(value[i])
        no_duplicate_list = list(dict.fromkeys(no_duplicate))
    
    for i in no_duplicate_list:
        no_duplicate_string += i

    return no_duplicate_string
    #start writing your code here

print(remove_duplicates("222233435657uwqtqasda!"))