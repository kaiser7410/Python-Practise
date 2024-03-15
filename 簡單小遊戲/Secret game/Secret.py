import random

secret = random.randint(1, 100)
minValue = 1
maxValue = 100

while True:
    guess = input(f"Make your guess(between the {minValue} and {maxValue}): ")
    if int(guess) < minValue or int(guess) > maxValue:
        print("Your guess is not within the range.")
        continue
    
    if int(guess) == secret:
        print(f"The secret is {secret}.")
        break
    elif int(guess) < secret:
        minValue = int(guess)
    elif int(guess) > secret:
        maxValue = int(guess)