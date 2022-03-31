from english_words import english_words_lower_alpha_set

with open('Script.txt','r+') as Script:
    lines = Script.read().split(" ")
    for word in lines:
        if(word in english_words_lower_alpha_set):
            if(not len(word) <= 2):
                foundWords = open("WordsFound.txt", "a")
                foundWords.write(f"{word}\n")
