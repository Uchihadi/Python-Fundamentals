#lex_auth_0127382206342184961397

def check_anagram(data1,data2):
    lst = []
    for i in data1:
        for j in data2:
            if i == j:
                return True
    
    #start writing your code here

print(check_anagram("eat","tea"))