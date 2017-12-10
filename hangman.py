# Mike Bland
# hangman game

import random
"""
def f(x):
    for line in x:
        print(line)
"""
wrong = 0
def insertLetter(spaces, letter, pos):
    #_ _ _ _
    #0123456
    #pos * 2 --> location in spaces
    pos = pos * 2
    spaces = spaces[0: pos] + letter + spaces[pos + 1:]
    return spaces


def readWords():
    wordList = []
    with open('wordlist.10000.txt') as wordFile:
        count = 0
        for line in wordFile:
            if len(line) > 4 and len(line) < 7:
                wordList.append(line[0:-1])
                      
    return wordList

pic = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
pic[0] =  '         +---------+'
pic[1] =  '         |         |'
pic[2] =  '                   |'
pic[3] =  '                   |'
pic[4] =  '                   |'
pic[5] =  '                   |'
pic[6] =  '                   |'
pic[7] =  '                   |'
pic[8] =  '                   |'
pic[9] =  '                   |'
pic[10] = '                   |'
pic[11] = '                   |'
pic[12] = '                   |'
pic[13] = '                   |'
pic[14] = '                   |'
pic[15] = '                   |'
pic[16] = ' ------------------+'

word =  random.choice(readWords())
length = len(word)
guesses = 0
correct = 0
print (word)



spaces = "_ " * len(word)


def f(x):
    for line in x:
       print(line)

for i in range(len(word)+ 2):
    guess = input("Enter a letter: ")
    guesses = guesses +1

    if wrong == length:
        print("Word not guessed: Game Over!")
        break
         

    elif guess in word:
        pos = word.index(guess)
        spaces = insertLetter(spaces, guess, pos)
        correct = correct + 1

        if correct == length and guesses > wrong:
            print("word ", word, " is correct: Game Over")
            break


    else:
        wrong = wrong + 1
        print("Letter not found!")

        if wrong ==1 and wrong < length:
            pic[2] = '       +---+       |'
            pic[3] = '       +   +       |'
            pic[4] = '       +---+       |'

        if wrong == 2 and wrong < length:
            pic[5] = '      +-----+      |'
            pic[6] = '      +     +      |'
            pic[7] = '      +     +      |'
            pic[8] = '      +     +      |'
            pic[9] = '      +-----+      |'

        if wrong == 3 and wrong < length:
            pic[5] = '----- +-----+ -----|'
            
        if wrong == 4 and wrong < length:
            pic[10] = '     /       \     |'
            pic[11] = '    /         \    |'
            pic[12] = '   /           \   |'




    pic[17] = spaces
    f(pic)



