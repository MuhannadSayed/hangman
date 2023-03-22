# here we start 

word = 'SWEDEN'
reveal = list(len(word)*'_')
print(reveal)

lives = 7
gameDone = False
while gameDone == False:
    guess = input('Gissa en bokstav ... Oops ordet är på engelska')
    guess = guess.upper()

    if guess == word:
        gameDone = True
if gameDone:
    print('WOHOO , DET ÄR KLART ')
else : 
    print('Tyvärr!!!! ordet är : ' , word)
