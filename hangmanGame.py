import helperFunctions
import os
import time

#NEED TO ADD SOME VALIDATION SO BOTH WORDS AND GUESSES ARE ONLY ALPHA CHARACTERS
repeat = True
while repeat:
    wordToGuess = ""
    hangmanSourceList = [["O"],["-","|","-"],["|","|"]]
    man = [[],[],[]]
    row = 0
    column = 0
    answer = "_______"
    guesses = []
    numGuesses = 0
    numwrongGuesses = 0
    wrongGuesses = []
    rightAnswer = False
    print("Welcome to hangman")
    chooseOwnWord = helperFunctions.chooseGameMode()
    if chooseOwnWord:
        wordToGuess = input("Please enter the word you would like the other player to guess (alpha characters only): ")
        answer = helperFunctions.createUnderscoreString(wordToGuess)
    else:
        wordToGuess = helperFunctions.chooseRandomWord()
        answer = helperFunctions.createUnderscoreString(wordToGuess)
    
    while numwrongGuesses < 6:
        if "_" not in answer:
            rightAnswer = True
            break
        print("The Scaffold")
        print("------------")
        for x in man:
            print(" ".join(map(str, x)))

        
        print("Current word: " + answer)
        if len(wrongGuesses) > 0:
            print("Wrong Guesses: ")
            for x in range(len(wrongGuesses)):
             print(wrongGuesses[x], end =" ")
            print(" ")
        userInput = input("Guess a letter: ")
        if userInput in guesses:
            print("You have already guessed that letter! Try another next time")
            time.sleep(3)
            os.system('cls')
            continue
        elif userInput in wordToGuess:
            print("Got one!")  
            i = 0
            while i < len(wordToGuess):
                if wordToGuess[i] == userInput:
                    guessList = list(answer)
                    guessList[i] = userInput
                    answer = ''.join(guessList)
                i += 1
            numGuesses += 1
            guesses.append(userInput)
            time.sleep(3)
            os.system('cls')
            continue
        else:
            print("Sorry, that is not a match!")
            wrongGuesses.append(userInput)
            numGuesses += 1
            numwrongGuesses += 1
            if column == len(hangmanSourceList[row]):
                row += 1
                column = 0
                man[row].append(hangmanSourceList[row][column])
                column+=1          
            else:
                if row == 0:
                    man[row].append(" ")
                    man[row].append(hangmanSourceList[row][column])
                    man[row].append(" ")
                elif row == 2:
                    man[row].append(" ")
                    man[row].append(hangmanSourceList[row][column])
                else:
                    man[row].append(hangmanSourceList[row][column])
                column += 1     
            time.sleep(3)
            os.system('cls')
            continue
        print(" ")
    

    if rightAnswer:
        print("Congratulations, you have solved my puzzle of letters in " + str(numGuesses) + " guesses!")
        print("The word was " + wordToGuess)
    else:
        print("Better luck next time!")
        print("The word was " + wordToGuess)
     
    repeat = helperFunctions.repeatGame()
    os.system('cls')


print("Thanks for playing!")