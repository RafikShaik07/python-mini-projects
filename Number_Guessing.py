import random
number_to_guess = random.randint(1, 50)

while True:
    try:
        guess = int(input("Guess a number between 1 to 50 : "))
        if guess < number_to_guess:
            print("Too Low!")
        elif guess > number_to_guess:
            print("Too High!")
        else:
            print("Congrats You guessed the number")
            break
        
    except ValueError:
        print("Enter a valid number!")