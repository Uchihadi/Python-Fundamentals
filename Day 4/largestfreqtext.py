#lex_auth_0127382283825971201450

def max_frequency_word_counter(data):
    word = ""
    frequency = 0
    words = data.lower()
    words = words.split()
    unique = []
    freq = {}
    maxi = []
    
    for i in words:
        if i not in unique:
            unique.append(i)
            
    
    for i in range(0,len(unique)):
        count = words.count(unique[i])
        freq.update({unique[i]:count})
    

    for key,value in freq.items():
        if(frequency< value):
            frequency = value
            word = key
            
    
    for key,value in freq.items():
        if(frequency == value):
            maxi.append(key)
        

    #start writing your code here
    #Populate the variables: word and frequency
    word  = maxi[0]
    
    for i in range(1,len(maxi)):
        if(len(word)<len(maxi[i])):
            word = maxi[i]


    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work
    print(word,frequency)

    #start writing your code here
    #Populate the variables: word and frequency


    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work
    #print(word,frequency)


#Provide different values for data and test your program.
data="Work like you do not need money, love like you have never been hurt, and dance like no one is watching"
max_frequency_word_counter(data)