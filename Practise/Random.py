import random

low = 1
high = 20
options = ['Rock', 'Paper', 'Scissors']
cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

number = random.randint(1, 6)
choice = random.choice(options)
random.shuffle(cards)

print(number)
print(choice)
print(cards)