from english_words import english_words_lower_alpha_set

words = ""

with open('Script.txt','r+') as Script:
    lines = Script.read().split(" ")
    for word in lines:
        if(word in english_words_lower_alpha_set):
            if(not len(word) <= 2):
                words = words + (f"{word}\n")
    foundWords = open("WordsFound.txt", "w")
    foundWords.write(words)