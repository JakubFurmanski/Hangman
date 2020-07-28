from random import randrange
from random import randint


categories = ["animals", "food", "home"]
words = ["dog", "cat", "elephant", "spaghetti", "ketchup", "milk", "bed", "bath", "wardrobe"]



def hangman():
    print("Welcome to The Hangman. Press ENTER to play")
    x = input()
    randomWord = categories[randrange(3)]
    print("Your category: " + randomWord + ". Guess a word!")

    if randomWord == "animals":
        correctWord = words[randint(0, 2)]
    elif randomWord == "food":
        correctWord = words[randint(3, 5)]
    elif randomWord == "home":
        correctWord = words[randint(6, 8)]

    correctWordCharacters = len(correctWord)
    hiddenWord = "-" * correctWordCharacters
    print(hiddenWord)

    hiddenWordList = list(hiddenWord)
    correctWordList = list(correctWord)

    counter = 0
    lives = 5

    while 1 < 2:
        playerInput = input()
        if playerInput in correctWordList:
            index = correctWordList.index(playerInput)
            hiddenWordList[index] = playerInput
            hiddenWord = "".join(hiddenWordList)
            print(hiddenWord)
            counter+=1
            correctWordList[index] = "."

            if counter == correctWordCharacters:
                print("Good job! Do you want to play again? Y/N")
                desire_to_play = input()
                if desire_to_play == "Y":
                    hangman()
                elif desire_to_play == "N":
                    exit()
                else:
                    wantToPlayAgain()

        else:
            lives-=1;
            if lives == 0:
                print("Game over. Try again")
                hangman()
            elif lives == 1:
                print("Wrong,", lives, "life left")
            else:
                print("Wrong,", lives, "lives left")



def wantToPlayAgain():
    print("Good job! Do you want to play again? Y/N")
    desire_to_play = input()
    if desire_to_play == "Y":
        hangman()
    elif desire_to_play == "N":
        print("Bye")
        exit()
    else:
        wantToPlayAgain()

hangman()






