#lex_auth_01269444195664691284

def encrypt_sentence(sentence):
    #start writing your code here
    list_words = sentence.split(" ")
    count = 1
    vowels = ["a", "e", "i", "o", "u"]
    temp = ""
    word = ""
    
    encoded = ""
    
    for word in list_words:
        cons = ""
        vol = ""
        if (count % 2 == 0):
            for i in word:
                if i in vowels:
                    vol += i
                else:
                    cons += i
            
            word = cons + vol
            encoded += word + " "
        
        else:
            encoded += word[::-1] + " "
            
        count += 1
    encoded = encoded.strip()
    
    return encoded
            

sentence="The sun rises in the east"
encrypted_sentence=encrypt_sentence(sentence)
print(encrypted_sentence)