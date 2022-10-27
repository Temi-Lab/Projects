import random

secret_num = random.randint(0, 100)
guess_limit = 0 
print("Instructions: You have ten tries to guess a number from 0-100.")

try:    

    while guess_limit < 10:
        guess = int(input("Guess: "))

        if guess > secret_num:
            print("Lower")
            guess_limit += 1
        elif guess < secret_num:
            print("Higher")
            guess_limit += 1
        elif guess == secret_num:
            print("You Have Won!")
            break
    else: 
        print("You LOST!")


except:
    print("Has to be an integer")
    while guess_limit < 10:
        guess = int(input("Guess: "))

        if guess > secret_num:
            print("Lower")
            guess_limit += 1
            
        elif guess < secret_num:
            print("Higher")
            guess_limit += 1
        elif guess == secret_num:
            print("You Have Won!")
            break
    else: 
        print("You LOST!")

 
