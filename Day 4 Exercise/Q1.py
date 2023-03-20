#lex_auth_012693825794351104168

# def find_common_characters(msg1,msg2):
#     msg1_letters = set(msg1) # output characters using the set functions
#     msg2_letters = set(msg2)
#     letters = ""
    
#     # Finding the intersection
#     intersect = "".join(msg1_letters & msg2_letters)
    
#     if len(intersect) == 0:
#         return -1
    
#     return intersect

def find_common_characters(msg1,msg2):
    str=""
    for i in msg1:
        if i in msg2:
            if i not in str:
                str=str+i
    if(str):
        return str.replace(" ","")
    else:
        return -1


#Provide different values for msg1,msg2 and test your program
msg1="I like Python"
msg2="Java is a very popular language"
common_characters=find_common_characters(msg1,msg2)
print(common_characters)