#lex_auth_0127382206342184961397

# Accepts two strings and return True if one string is a special anagram of another string
# Special Annagram: 1) Contain Repeating Characters 
# 2) None of characters repeat at same position
# 3) Length of the strings should be the same

def check_anagram(data1,data2):
    first = data1.lower()
    second = data2.lower() #Lowering all the characters within both data sets
    
    d1 = [] #Initialise Empty List for both of data sets
    d2 = []

    for i in range(0, len(first)):
        d1.append(first[i]) #Appending each character in a word into first list
        sorted_data1 = sorted(d1)
    for i in range(0, len(second)): #Appending each character in a word into second list
        d2.append(second[i])
        sorted_data2 = sorted(d2)

    print (sorted_data1)
    print (sorted_data2)

    if sorted_data1 != sorted_data2:
        return False
    
    count = 0
    if (len(d1) == len(d2)): # First condition: If length for both data sets are same
        for i in d1:
            for j in d2:
                if(i == j):
                    a = d1.index(i) #Declare a variable as an index for each of characters in data 1
                    b = d2.index(j) #Declare a variable as an index for each of characters in data 2
                    if(a == b):
                        return False
                    else:
                        count += 1
    if(len(second) == len(first)):
        return True
    else:
        return False
    #start writing your code here

print(check_anagram("Badcredit", "Debitcard"))