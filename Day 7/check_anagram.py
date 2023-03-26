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
    
    count = 0
    if (len(d1) == len(d2)):
        for i in d1:
            for j in d2:
                if(i == j):
                    a = d1.index(i)
                    b = d2.index(j)
                    if(a == b):
                        return False
                    else:
                        count += 1
    if(len(second) == len(first)):
        return True
    else:
        return False
    #start writing your code here

print(check_anagram("about","table"))