import random

options = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," "]

while(True):
    input = random.choice(options)
    script = open("Script.txt", "a")
    script.write(input)