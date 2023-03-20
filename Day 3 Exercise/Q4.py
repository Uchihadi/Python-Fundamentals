#lex_auth_012693819159732224162

def check_palindrome(word):
    word = word.lower() # Making the word a lowercase
    reversed_word = word[::-1] # Syntax for slicing a string 'word' in reverse order
    # Step value is -1, start and stop value at 0
    
    if word == reversed_word:
        return True
    else:
        return False

status=check_palindrome("malayalam")
if(status):
    print("word is palindrome")
else:
    print("word is not palindrome")