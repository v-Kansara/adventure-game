# Imports
###############
import random
from PlayerClass import Player
from intro import intro
from Rooms.Room_Basement import basement

# Start Game
###############
def main():
    print("Welcome, Welcome, Welcome to the Crazy Wizard Castle Adventure Game! Please follow the steps below to create your character")

    # Player inputs of name and adjectives
    playerName = input("Who are you, great adventurer?: ")
    inputAdjectives = input("What 3 adjectives describe you best? (Write SKIP if you want to skip and get 3 random adjectives, or write your adjectives with a comma followed by a space - E.g. Brave, Courageous, Strong): ")

    Adjectives_LIST = ["ambitious", "aggressive", "brave", "bright", "calm", "compassionate", "courageous", "confident", "determined", ]
    playerAdjectives = [adjective for adjective in inputAdjectives.split(", ")] # Creates list of words from user input

    if len(playerAdjectives) > 3: # Checks if length of adjectives list is greater than 3 words
        for i in range(0, len(playerAdjectives) - 3):
            playerAdjectives.pop(3) # Remove any adjectives besides initial 3

    if inputAdjectives == "SKIP" or inputAdjectives == "skip": # Checks if user skipped the step
        playerAdjectives.pop(0)
        for i in range(0, 3):
            playerAdjectives.append(random.choice(Adjectives_LIST)) # Randomly assigns adjectives to user

    player = Player(playerName, playerAdjectives) # replace with playerAdjectives
        
    intro(player) # Calls the intro Function to initiate the storyline

main() # Calls the main Function to start the game