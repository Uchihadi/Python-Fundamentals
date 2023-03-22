#lex_auth_01269444890062848087

def find_correct(word_dict):
    list_answer = []
    correct_ans = 0
    wrong_ans = 0
    almost_correct_ans = 0
    
    for key, value in word_dict.items():
        if (key == value):
            correct_ans += 1
        elif (len(key) != len(value)): #if the length is wrong; if words are not similar thence it will go to this loop
            wrong_ans += 1 #The count for wrong answer will be added
        else:
            first_word = key # Declare the Key as a new variable first_word
            second_word = value # Declare the Value as a new variable second_word
            count = 0
            index = 0
            
            for letter1 in first_word: #Starting count only after else statement
                letter2 = second_word[index]
                if (letter1 != letter2):
                    count += 1
                    index += 1 #Increasing the index in letter2
                else:
                    index += 1
        
            if (count < 3):
                almost_correct_ans += 1
            else:
                wrong_ans += 1
            
    list_answer += [correct_ans] + [almost_correct_ans] + [wrong_ans] #Appending the list with correct and wrong answers
    return list_answer
                    
    
    #start writing your code here

word_dict={"THEIR": "THEIR","BUSINESS":"BISINESS","WINDOWS":"WINDMILL","WERE":"WEAR","SAMPLE":"SAMPLE"}
print(find_correct(word_dict))