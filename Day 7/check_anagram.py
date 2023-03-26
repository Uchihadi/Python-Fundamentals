#lex_auth_0127382206342184961397

# Accepts two strings and return True if one string is a special anagram of another string
# Special Annagram: 1) Contain Repeating Characters 
# 2) None of characters repeat at same position
# 3) Length of the strings should be the same

def check_anagram(data1,data2):
    first = data1.lower()
    second = data2.lower()
    
    d1 = []
    d2 = []

    for i in range(0, len(first)):
        d1.append(first[i])
        d1 = sorted(d1)
    for i in range(0, len(second)):
        d2.append(second[i])
        d2 = sorted(d2)

    print (d1)
    print (d2)

    if d1 != d2:
        return False
    
    lst = []
    for i in data1:
        for j in data2:
            if len(i) == len(j):
                if i == j:
                    return True
    #start writing your code here

print(check_anagram("about","table"))