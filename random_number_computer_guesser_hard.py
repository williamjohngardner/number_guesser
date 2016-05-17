import random

user_guess = int(input("Enter a number between 1 & 100 and challenge the computer to guess: "))
counter = 0
minimum = 1
maximum = 100

while counter <= 4:

    computer_guess = int(random.randint(minimum, maximum))
    print("The computer guessed: " + str(computer_guess))

    if computer_guess == user_guess:
        print("The computer guessed correctly in " + str(counter + 1) + " turns.")
        exit()

    else:
            if computer_guess > user_guess:
                maximum = computer_guess - 1
                counter += 1
                if computer_guess - user_guess <= 5:
                    print("The computer's guess is VERY close!")
            elif computer_guess < user_guess:
                minimum = computer_guess + 1
                counter += 1
                if user_guess - computer_guess <= 5:
                    print("The computer's guess is VERY close!")

else:
    print("You win!  The computer did not guess your number in 5 turns!")