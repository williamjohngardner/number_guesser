import random

user_guess = int(input("Choose a number and enter your guess: "))
computer_guess = int(random.randint(1, 100))
counter = 0

if user_guess == computer_guess:
    print("You guessed correctly on the first try!")
    exit()

while user_guess != computer_guess:

    if user_guess > computer_guess:
        print("Your guess is greater than the number.  Try again: ")
        if user_guess - computer_guess <= 5:
            print("You're REALLY close!!!")
        counter += 1
        if counter == 5:
            print("You've used your 5 turns")
            break
        user_guess = int(input("Choose a number and enter your guess: "))

    elif user_guess < computer_guess:
        print("Your guess is less than the number.  Try again: ")
        if computer_guess - user_guess <= 5:
            print("You're REALLY close!!!")
        counter += 1
        if counter == 5:
            print("You've used your 5 turns")
            break
        user_guess = int(input("Choose a number and enter your guess: "))

else:
    print("You guessed correctly!")
    print("You guessed in " + str(counter + 1) + " turns.")