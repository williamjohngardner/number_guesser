import random

user_guess = int(input("Enter a number between 1 & 100 and challenge the computer to guess: "))
counter = 0

while counter <= 5:

    computer_guess = int(random.randint(1, 100))
    print("The computer guessed: " + str(computer_guess))

    if computer_guess == user_guess:
        print("The computer guessed correctly in " + str(counter + 1) + " turns.")
        exit()

    elif computer_guess > user_guess:
        print("The computer's guess is greater than your number.  It will guess again: ")
        counter += 1
        if computer_guess - user_guess <= 5:
            print("The computer is REALLY close to your number!!!")

    elif computer_guess < user_guess:
        print("The computer's guess is less than your number.  It will guess again: ")
        counter += 1
        if user_guess - computer_guess <= 5:
            print("The computer is REALLY close to your number!!!")

else:
    print("You win!  The computer did not guess your number in 5 turns!")