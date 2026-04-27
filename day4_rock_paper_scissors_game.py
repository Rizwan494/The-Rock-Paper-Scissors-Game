import random
user_choice = int(input("What do you chose? type 0 for Rock, 1 for paper and 2 for Scissors "))
computer_choice = random.randint(0, 2)
print(f"computer choice {computer_choice}")

if user_choice > 3 or user_choice < 0:
    print("User picked invalid choice, you lost")

elif user_choice == computer_choice:
    print("Draw")

elif user_choice == 0 and computer_choice == 2:
    print("You win")

elif user_choice == 2 and computer_choice == 0:
    print("You lost")

elif user_choice == 0 and computer_choice == 1:
    print("You lost")

elif user_choice == 1 and computer_choice == 0:
    print("You win")

elif user_choice == 1 and computer_choice == 2:
    print("You lost")

elif user_choice == 2 and computer_choice == 1:
    print("You win")