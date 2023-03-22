# here we start 

import os
from random import choice
from words import selected_word
from images import hangman


#word = 'SWEDEN'
word = selected_word()
reveal = list(len(word)*'_')


lives = 7
gameDone = False

def check_letter(letter,word):
    global reveal
    for i in range(0,len(word)):
        letter = word[i]
        if guess == letter:
            reveal[i] = guess
    if '_' not in reveal:
        return True
    else: 
        return False


def status(): 
    os.system('clear')
    print(hangman[7-lives] , word)
    print(' '.join([str(e) for e in reveal]))
    print ('Du har ', lives , 'försök kvar')



while gameDone == False and lives > 0:
    status()
    guess = input('Gissa en bokstav ... Oops ordet är på engelska')
    guess = guess.upper()

    if guess == word:
        gameDone = True
        reveal = word
    if len(guess) == 1 and guess in word:
        gameDone = check_letter(guess,word)
    else : 
        lives -=1
    status()
if gameDone:
    print('WOHOO , DET ÄR KLART ')
else : 
    print('Tyvärr!!!! ordet är : ' , word)
