from isWordGuessed import isWordGuessed
from getGuessedWord import getGuessedWord
from getAvailableLetters import getAvailableLetters

def hangaroo(secretWord):
    
    print('Mabuhay! Welcome sa Hangaroo!')
    print('Ang salitang ito ay may', len(secretWord), "na letra.")
    
    mistakesMade = 0
    lettersGuessed = []

    while 8 - mistakesMade > 0:
        
        if isWordGuessed(secretWord, lettersGuessed) == True:
            print('.............')
            print('Nanalo ka! Pagpupugay!')
            break
        
        else:
            print('.............') 
            print('May natitira ka pang', 8 - mistakesMade, 'na hula.')
            print('Mga pagpipilian na letra:', getAvailableLetters(lettersGuessed))
            guess = str(input('Manghula ng letra: ')).lower()
            
        if guess in secretWord and guess not in lettersGuessed:
        	lettersGuessed.append(guess)
            
        	print('Tama!: ', getGuessedWord(secretWord, lettersGuessed))
            
        elif guess in lettersGuessed:
            
        	print("Naku, napili mo na ang letrang iyan!: ", getGuessedWord(secretWord, lettersGuessed))
            
        elif guess not in secretWord:
            
        	print("Naku, wala yan sa secret word!: ", getGuessedWord(secretWord, lettersGuessed))
        	lettersGuessed.append(guess)
            
        	mistakesMade += 1
            
        if 8 - mistakesMade == 0:
            
            print('.............')
            
            print('Ops! Pasensya na ubos na ang iyong hula, and salita ay: ', secretWord)
            break
        
        else:
        	continue