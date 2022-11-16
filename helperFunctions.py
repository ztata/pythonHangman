import random

def repeatGame():
    validInput = False
    while validInput == False:
        userInput = input("Would you like to guess again (Y/N)?: ")
        if userInput.strip().lower() == "y":
            return True
        elif userInput.strip().lower() == "n":
            print("See you soon!")
            return False
        else:
            print("You have to either enter a Y or an N to continue")

def chooseGameMode():
    userInput = input("enter y to enter your own word or anything else to use an auto generated word: ")
    if userInput.strip().lower() == "y":
        return True
    else:
        return False

randomWords = [
    "blubber",
    "phoenix",
    "staircase",
    "squidward",
    "spacecraft",
    "trireme",
    "antidisestablishmentarianism",
    "glutinous",
    "gilded",
    "balsam",
]

def chooseRandomWord():
    num = random.randint(0, len(randomWords)-1)
    return randomWords[num]

def createUnderscoreString(word):
    wordLength = len(word)-1
    tempList = []
    while wordLength >= 0:
        tempList.append("_")
        wordLength -= 1
    
    result = "".join(tempList)
    return result
    


