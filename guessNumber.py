import random

rd = random.randint(1, 99)
guess, c = 0, 0
while guess != rd and guess != "exit":
    guess = input("Enter a guess b/w 1 to 99: ")

    if guess == "exit": break

    guess = int(guess)
    c += 1

    if guess < rd:
        print("Too low...")
    elif guess > rd:
        print("Too high")
    else:
        print("Right!, You took only ", c, "tries.")

input()
