import random

print("=== Number Guessing Game ===")

secret = random.randint(1, 100)

attempts = 0
low = 1
high = 100

while True:
    
    guess = int(input(f"Guess a number ({low}-{high}): "))
    attempts += 1
    
    if guess < secret:
        low = guess + 1
        print("Too low! Try higher!")
    
    elif guess > secret:
        high = guess - 1
        print("Too high! Try lower!")
    
    else:
        print(f"Correct! The number was {secret}")
        print(f"You got it in {attempts} attempts!")
        break
