import random

lowest_num = 1
highestNum = 100
answer = random.randint(lowest_num, highestNum)
guesses = 0
is_running= True

print("Python Number Guessing Game")
print(f"Select a number between {lowest_num} and {highestNum}")

while is_running :
    guess = input("Enter your guess : ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowest_num or guess > highestNum:
            print("The number is out of range")
            print(f"Please select a number between {lowest_num} and {highestNum}")
        elif guess < answer :
            print("To low! Try again")
        elif guess > answer :
            print("To high! Try again")
        else:
            print(f"Correct! You have guessed the right number! The answer was {answer}")
            print(f"Number of guesses : {guesses}")
            is_running = False

    else :
        print("Invalid guess")
        print(f"Please select a number between {lowest_num} and {highestNum}")
