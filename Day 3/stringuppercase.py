#lex_auth_012693816331657216161

def encode(message):
    
    #Remove pass and write your logic here
    output = "" #Initialise string opening for final output
    prev = message[0] #First character of input string
    i = 1 #Initialise the i value
    count = 1 # Initialise the count
    
    while len(message) > i:
        if message [i] == prev: #The previous letter equals the letter in the i position
            count += 1 # If message[i] == message [i - 1] then add count
        else:
            output += str(count) + prev #prev is a letter; count becomes a string and current count of output
            count = 1 # resets the count
            prev = message [i] #updates the prev
        
        if i == len(message) - 1: #One final run of repeated characters not added to output string
            output += str(count) + prev #Appends to the output string
        i += 1 #Adding count to the while loop
    if len(message) == 1: #One final run of repeated characters not added to output string
            output += str(count) + prev

    return output


#Provide different values for message and test your program
encoded_message=encode("ABBBBCCCCCCCCAB")
print(encoded_message)