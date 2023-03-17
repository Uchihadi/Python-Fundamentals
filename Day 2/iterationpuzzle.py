#lex_auth_012693810762121216155

def solve(heads,legs):
    error_msg="No solution"
    chicken_count = 0
    rabbit_count = 0
    
    # Start writing your code here
    #Populate the variables: chicken_count and rabbit_count
    if heads > legs or legs % 2 != 0 or heads == 1:
        print (error_msg)
    else:
        rabbit_count = int((legs - 2*heads) / 2)
        chicken_count = int(heads - rabbit_count)
        
        return chicken_count, rabbit_count

    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work

    #print(chicken_count,rabbit_count)
    #print(error_msg)

#Provide different values for heads and legs and test your program
solve(38,131)