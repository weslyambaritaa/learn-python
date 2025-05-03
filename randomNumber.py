import random

low = 1
high = 100
options = ("rock", "paper", "scissors")
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "K", "A"]

# number = random.randint(low, high)
# number2 = random.random() #giving random number between 0 - 1

# print(number)
# print(number2)

option = random.choice(options)
random.shuffle(cards)

print(cards)