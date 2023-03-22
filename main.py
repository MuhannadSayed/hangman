# here we start 

from words import selected_word


word = 'SWEDEN'
# word = selected_word()
reveal = list(len(word)*'_')


lives = 7
gameDone = False
while gameDone == False and lives > 0:
    print(reveal)
    guess = input('Gissa en bokstav ... Oops ordet är på engelska')
    guess = guess.upper()

    if guess == word:
        gameDone = True
    if len(guess) == 1 and guess in word:
        for i in range(0,len(word)):
            letter = word[i]
            if guess == letter:
                reveal[i] = guess
        if '_' not in reveal:
            gameDone = True
    else : 
        lives -=1
if gameDone:
    print('WOHOO , DET ÄR KLART ')
else : 
    print('Tyvärr!!!! ordet är : ' , word)
