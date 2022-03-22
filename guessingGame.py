import random
number = random.randint(1,9)
print(number)

chances = 0
while chances < 5:
    guess = int(input("guess number"))
    if guess == number:
        print("You Won")
        break
    elif guess < number:
        print("Guess a larger number")
    else:
        print("Guess a lower number")
    chances = chances + 1
    if not chances  < 5:
        print("You lose! The number was ", number)