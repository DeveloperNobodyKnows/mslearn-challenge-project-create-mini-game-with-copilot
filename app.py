# Description: This is a simple rock, paper, scissors game that will be played in the terminal

# import necessary modules for the game
import random

# The player will be prompted to choose rock, paper, or scissors
def player_choice():
    # The player's choice will be stored in a variable
    player = input("Choose rock, paper, or scissors: ").lower()
    # If the player's choice is not rock, paper, or scissors, they will be prompted to choose again
    while player != "rock" and player != "paper" and player != "scissors":
        player = input("Invalid choice. Choose rock, paper, or scissors: ").lower()
    return player

# The computer will randomly choose rock, paper, or scissors
def computer_choice():
    # The computer's choice will be stored in a variable
    computer = random.choice(["rock", "paper", "scissors"])
    return computer

# The game will determine the winner based on the player's and computer's choices
def determine_winner(player, computer):
    # If the player and computer choose the same item, the game will be a tie
    if player == computer:
        return "It's a tie!"
    # If the player chooses rock and the computer chooses scissors, the player wins
    elif player == "rock" and computer == "scissors":
        return "You win!"
    # If the player chooses paper and the computer chooses rock, the player wins
    elif player == "paper" and computer == "rock":
        return "You win!"
    # If the player chooses scissors and the computer chooses paper, the player wins
    elif player == "scissors" and computer == "paper":
        return "You win!"
    # If the player chooses rock and the computer chooses paper, the computer wins
    elif player == "rock" and computer == "paper":
        return "Computer wins!"
    # If the player chooses paper and the computer chooses scissors, the computer wins
    elif player == "paper" and computer == "scissors":
        return "Computer wins!"
    # If the player chooses scissors and the computer chooses rock, the computer wins
    elif player == "scissors" and computer == "rock":
        return "Computer wins!"

# The player will receive points based on the outcome of the game
def update_score(winner, player_score, computer_score):
    # If the game is a tie, the player and computer will receive 0 points
    if winner == "It's a tie!":
        player_score += 0
        computer_score += 0
    # If the player wins, the player will receive 1 point
    elif winner == "You win!":
        player_score += 1
    # If the computer wins, the computer will receive 1 point
    elif winner == "Computer wins!":
        computer_score += 1
    return player_score, computer_score

# display the score after each round
def display_score(player_score, computer_score):
    print(f"Player: {player_score} Computer: {computer_score}")

# keep track of total rounds played and update it after each round
def display_rounds_played(rounds_played):
    rounds_played += 1
    return rounds_played

# keep track of total wins for the player
def display_total_wins(player_score):
    print(f"Total wins: {player_score}")


# The game will continue until the player decides to stop playing. Display who won after each game and the score. If the game ends display the total number of rounds played and total player wins
def play_game():
    # Initialize the player's score, computer's score, and the number of rounds played
    player_score = 0
    computer_score = 0
    rounds_played = 0
    # The game will continue until the player decides to stop playing
    while True:
        print()
        # Call the player_choice function to get the player's choice
        player = player_choice()
        # Call the computer_choice function to get the computer's choice
        computer = computer_choice()
        # Call the determine_winner function to determine the winner of the game
        winner = determine_winner(player, computer)
        # Call the update_score function to update the player's and computer's scores
        player_score, computer_score = update_score(winner, player_score, computer_score)
        # Call the display_score function to display the score after each round
        display_score(player_score, computer_score)
        # Call the display_rounds_played function to display the total number of rounds played
        rounds_played = display_rounds_played(rounds_played)
        print(f"Round {rounds_played}: {winner}")
        # If the player decides to stop playing, the game will end and the total number of rounds played and total player wins will be displayed
        if input("Do you want to play again? (yes/no): ").lower() != "yes":
            print()
            print()
            print("Game Over!")
            display_total_wins(player_score)
            print(f"Total rounds played: {rounds_played}")
            break


# Call the functions to play the game
play_game()
