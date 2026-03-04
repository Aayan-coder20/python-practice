import random 

while True:
    choice = input("Roll the dice? (yes/no): ")
    if choice.lower() == 'yes':
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        print(f"({dice1} , {dice2})")
    elif choice.lower() == 'no':
        print("Thanks for Playing.")
        break
    else:
        print("Invalid choice.")

