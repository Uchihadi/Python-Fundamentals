#lex_auth_012693816331657216161

def encode(message):
    
    #Remove pass and write your logic here
    output = "" #Initialise string opening
    count = 1
    output += message[0]
    
    for i in range (1, len(message)):
        if message[i] == message[i-1]:
            count += 1
        else:
            output += str(count)
            output += message[i]
            count = 1
    
    output = str(count)
    return output
            

#Provide different values for message and test your program
encoded_message=encode("ABBBBCCCCCCCCAB")
print(encoded_message)