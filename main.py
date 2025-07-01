#This file contains the main logic for the follower comparison game

# Import required modules and resources
import random
from art import logo,vs_logo,line,clr_scr# Imported from art.py (logo, vs symbol, screen clear command)
from game_data import data#This contains the list of famous people with their follower data

# Define global variables to track player's score and life status
scores = 0
player_life = 1

# This function compares user's choice with the person who has more followers
def comparison(user_choice):
    global player_life, scores

    # Determine who has more followers
    highest_follower = max(person1["follower_count"], person2["follower_count"])
    if user_choice == highest_follower:
        player_life = 1      # Player remains alive
        scores += 1          # Increase score
    else:
        player_life = 0      # Wrong answer → game over

# This function runs the main game round (printing, input, and comparison)
def game():
    # Show first person's info
    print(line)  # Separator line
    print(f"Compare A: {person1["name"]}, a {person1["description"]}, from {person1["country"]}.")

    # VS logo between two choices
    print(vs_logo)

    # Show second person's info
    print(f"Against B: {person2["name"]}, a {person2["description"]}, from {person2["country"]}.")
    print(line)        #Separator line

    # Get valid input from the user
    while True:
        user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
        if user_choice == 'a' or user_choice == 'b':
            break
        else:
            print("Invalid input!")

    # Compare user's choice with actual popular person
    if user_choice == "a":
        comparison(person1["follower_count"])
    else:
        comparison(person2["follower_count"])

#  Game Loop – runs until the player makes a mistake
while True:
    # Select two different people randomly from the data
    person1, person2 = random.sample(data, 2)

    # Clear the screen and show game logo
    print(clr_scr)#this line clear screen
    print(logo)#this line print the game logo

    # If player is alive, continue the game
    if player_life == 1:
        if scores > 0:
            print(f"You're right! Current score: {scores}.")
        game()
    # Player gave wrong answer, game ends
    else:
        print(f"Sorry, that's wrong. Final score: {scores}.")
        print(line)
        break
