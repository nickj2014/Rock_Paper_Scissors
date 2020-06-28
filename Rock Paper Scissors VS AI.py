import random


def main():
    run = True
    choices = ["rock", "paper", "scissors"]  # Choices for random selection

    while run:  # Run forever until user chooses to exit
        p2 = random.choice(choices)  # Pick random option for player 2
        p1 = get_choice()  # Get user choice variable from function
        print(f"Player 2 chose {p2}.")
        run = check_outcome(p1, p2)  # Calculates win/tie, sets run to true/false based on user input


def get_choice():  # Get choices, handles error checking invalid input options
    while True:  # Run until correct input chosen and break out
        p1 = input("Player 1, please enter rock, paper or scissors: ")
        p1 = p1.lower()
        if p1 in ["rock", "paper", "scissors"]:
            break
        else:
            print("Invalid choice, try again.")
    return p1  # Return choice


def check_outcome(p1, p2):  # Checks all possible outcomes to determine winner or tie
    if p1 == p2:  # Check tie
        return winner_found("tie")
    elif p1 == "rock":  # Check outcomes, run winner function
        if p2 == "scissors":
            return winner_found("1")
        elif p2 == "paper":
            return winner_found("2")
    elif p1 == "paper":
        if p2 == "rock":
            return winner_found("1")
        elif p2 == "scissors":
            return winner_found("2")
    elif p1 == "scissors":
        if p2 == "paper":
            return winner_found("1")
        elif p2 == "rock":
            return winner_found("2")


def winner_found(player):  # Prints winner found in outcome, asks to repeat or not
    if player == "tie":  # Print tie message
        print("It's a tie!")
    else:
        print(f"Player {player} wins!")  # Print win message

    repeat = input("Another game? Enter yes/no: ")
    if repeat.lower() in ("y", "yes"):  # If input is yes or y, repeat
        return True
    else:  # If input is anything else, just exit
        print("Goodbye!")
        return False


main()
