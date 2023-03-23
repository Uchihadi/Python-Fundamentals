#lex_auth_01269442114344550475

def is_palindrome(word):
    #Remove pass and write your logic here
    word = word.lower()
    if len (word) < 1:
        return True
    else:
        if word [0] == word [-1]: #If first letter is the same as last letter
            return is_palindrome(word[1:-1]) 
        #Recursively call function with argument as sliced list with 1st and last char removed
        else:
            return False

#Provide different values for word and test your program
result=is_palindrome("Malayalam")
if(result):
    print("The given word is a Palindrome")
else:
    print("The given word is not a Palindrome")