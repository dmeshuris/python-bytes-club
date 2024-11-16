import random
choices = ["rock","paper","scissors"]
while true:
    computer_choice = random.choice(choices)
    user_input = input("This is a game of Rock, paper, scissors, which do you pick?")

    if user_input == "paper" and computer_choice == "rock":
        print("you won!")
    elif user_input == computer_choice:
        print("draw!")

    elif user_input == "rock" and computer_choice == "scissors":
        print("you won!")
    elif user_input == computer_choice:
        print("draw!")

    elif user_input == "scissors" and computer_choice == "rock":
        print("you won!")
    elif user_input == computer_choice:
        print("draw!")
    