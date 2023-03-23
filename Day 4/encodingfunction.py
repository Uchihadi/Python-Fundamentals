#lex_auth_01269444961482342489

def sms_encoding(data):
    encoded = ""
    words = data.split() #Splitting sentence into words
    
    for element in words:
        if len(element) == 1: #If the word has only one letter
            encoded += element
        else:
            for letter in element: #
                if letter != 'a':
                    if letter != 'e':
                        if letter != 'i':
                            if letter != 'o':
                                if letter != 'u':
                                    if letter != 'A':
                                        if letter != 'E':
                                            if letter != 'I':
                                                if letter != 'O':
                                                    if letter != 'U':
                                                        encoded += str(letter)
        encoded += " "
        
    # words = data.split()
    # print(words)
    # vowel = "aeiouAEIOU"
    
    # for element in words:
    #     if len(element) == 1:
    #         encoded += element
    #     else:
    #         for letter in element:
    #             if letter not in vowel:
    #                 encoded += letter
    #     encoded += " "   
    
    return encoded[0:-1]
    
    #start writing your code here

data="I love Python"
print(sms_encoding(data))