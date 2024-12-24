# Snake Water Gun Game
import random


def get_user_choice():
    while True:
        user_choice = input(
            "Enter your choice (Snake, Water, Gun): ").strip().capitalize()
        if user_choice in ['Snake', 'Water', 'Gun']:
            return user_choice
        else:
            print("Invalid choice! Please enter Snake, Water, or Gun.")


def get_computer_choice():
    choices = ['Snake', 'Water', 'Gun']
    computer_choice = random.choice(choices)
    return computer_choice


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif user_choice == 'Snake':
        return "You win!" if computer_choice == 'Water' else "Computer wins!"
    elif user_choice == 'Water':
        return "You win!" if computer_choice == 'Gun' else "Computer wins!"
    elif user_choice == 'Gun':
        return "You win!" if computer_choice == 'Snake' else "Computer wins!"

print("Let's play Snake, Water, and Gun!")
while True:
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    result = determine_winner(user_choice, computer_choice)
    print(result)
    play_again = input(
        "Do you want to play again? (yes/no): ").strip().lower()
    if play_again != 'yes':
        print("Thanks for playing!")
        break

