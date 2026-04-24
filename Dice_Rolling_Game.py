import random
while True:
    choice = input(f"Do you want to roll the dice? (y/n): ").lower()
    if choice == "y":
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(f"You rolled {die1} and {die2}")
    elif choice == "n":
        print("Thanks for playing!")
        break
    else:
        print("Invalid choice. Please enter 'y' or 'n'.")


  