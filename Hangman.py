import  time, datetime

name = input('What is your name?\n')

def greet():
    current_Time = int(datetime.datetime.now().hour)
    if current_Time >= 0 and current_Time < 12:
        return ('Good Morning!')
    elif current_Time >= 12 and current_Time < 18:
        return ('Good Afternoon!')
    else:
        return ('Good Evening!')
print(greet() + ' ' + name + ' ' + '\n' + "Lets Play Hangman!" )

# wait for a sec 
time.sleep(1)


# setup the word and hidden list
word = list("apple")
hidden = []

len_word = "_" * len(word)

attempts = 0
Chances = 4

# loop until either the player has won or lost
isGameOver = False
while not isGameOver:

    # display the current board, guessed letters, and attempts remaining
    print(f"You have {Chances - attempts} attempts remaining")

    print('The current word is:' + len_word)
    #print(f"The current word is: {' '.join(hidden)}")       

    print("     ------")
    print("     |    |")
    print("     |    " + ("O" if attempts > 0 else ""))
    print("     |    " + ("/\\" if attempts > 1 else ""))
    print("     |    " + ("|" if attempts > 2 else ""))
    print("     |    " + ("/\\" if attempts > 3 else ""))
    print(" --------")

    # ask the player for a character
    letterGuessed = input("Please Guess a letter: ")

    print('\n')

    if letterGuessed in word:
        # if the player guessed correct, show all matched letters and print message
        print(f"You guessed correctly! {letterGuessed} is in the word")
        for i in range(len(word)):
            character = word[i]
            if character == letterGuessed:
                hidden[i] = word[i]
                word[i] = "_"
    else:
        # if player guessed wrong, print failure message and increment attempts
        print(f"You guessed wrong! {letterGuessed} is NOT in the word")
        attempts += 1

    # if the player has won print a win message and stop looping
    if all("_" == char for char in word):
        print("Congratulations, You Won!")
        isGameOver = True

    # if the player has lost, print failing and stop looping
    if attempts >= Chances:
        print("You lost, Rest in peace! ( ⌣̩̩́_⌣̩̩̀ ) ")
        isGameOver = True
