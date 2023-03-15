# Q5: Write a program that prompts the user to enter a string and then counts the number of vowels and consonants in the string.

def wordcount():
    word = input("Enter the string: ")
    vowel_count = 0
    consonant_count = 0
    
    for i in word:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == "u":
            vowel_count+=1
        else:
            consonant_count += 1
    print("There are a number of", vowel_count, "vowels")
    print("There are a number of", consonant_count, "consonant")

wordcount()
        