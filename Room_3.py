# Imports
###############
import random
import time
from Rooms.Room_5 import room5
from Rooms.Room_Basement import basement
from otherFunctions import HELP

# Run room 3 function with player object
###############
def room3(player):
    room3_complete = False
    while not room3_complete:
        print("ROOM 3")
        print("------")
        print()
        print("You wake up dazed and confused, but you see some dim light above you. Picking yourself up, you see a broken stall in front of you, with a vendor who's already waiting for you. You approach the vendor, and he offers you some options: ")
        print("1. You can give 30 health points for a sword")
        print("2. You can give $10 (If you have it) for an ability to slow down time")
        print("3. You can give the your lucky coin (If you have it) for 50 shield points")
        print("4. Decline his offer and go to the door to the basement")
        print("Type 'ME' if you want your stats OR type 'HELP' if you are stuck on this question.")
        response = (input("You consider the options and decide to: ")).split() # Asks player what they want to do
        print()

        # Check if player wants help for what to do
        if ("Help" in response) or ("HELP" in response) or ("help" in response):
            print(HELP("3", 1))
            print()
            time.sleep(5)

        # Checks if player wants to get their stats
        elif ("ME" in response) or ("Me" in response) or ("me" in response):
            player.ME()
            time.sleep(3)
        
        # Checks if player wants to sacrifice 30 health for the sword
        elif ("30" in response) or ("health" in response) or ("Health" in response) or ("sword" in response) or ("Sword" in response) or ("1" in response):
            # Checks if player has over 30 health
            if player.health > 30:
                print("You ask the vendor for the sword, and he gladly hands it over to you. You give up 30 health points as payment. The vendor guides you to the door and sends you on your journey, now equipped with a magnificent sword.")
                print()
                time.sleep(2)
                player.pickUpItem("sword") # pickUpItem Method on player object adds item to player's inventory
                player.increaseHealth(-30) # increaseHealth Method on player object increases player's health by input amt
                time.sleep(3)
                room3_complete = True # Ends room3 loop before moving player to room 5
                room5(player) # Sends player to room 5 function

            else:
                print("You don't have enough health points to trade for a sword. Please choose a different option.")
                print()
                time.sleep(3)

        # Checks if player wants to give $10 for ability to slow down time
        elif ("$10" in response) or ("slow" in response) or ("Slow" in response) or ("time" in response) or ("Time" in response) or ("2" in response):
            # Checks if player has $10 or more
            if player.balance >= 10.0:
                print("You ask the vendor for the ability to slow down time, and he fishes it out from his cabinet. You give $10 to him as payment. The vendor guides you to the door and sends you on your journey, now with your magical potion to slow down time. ")
                print()
                time.sleep(2)
                # gainAbility Method on player object adds ability to player's abilities
                player.gainAbility("slow-down-time")
                player.addMoney(-10.0) # addMoney Method on player object increases player's balance by input amt
                time.sleep(3)
                room3_complete = True
                room5(player)

            else:
                print("You don't have enough money to trade for that ability. Please choose a different option.")
                print()
                time.sleep(3)

        # Checks if player wants to sacrifice lucky coin for shield
        elif ("lucky" in response) or ("Lucky" in response) or ("coin" in response) or ("Coin" in response) or ("50" in response) or ("shield" in response) or ("Shield" in response) or ("3" in response):
            # Checks if player has lucky coin
            if "coin" in player.inventory:
                print("You ask the vendor for the 50 shield points, and he gives them to you in exchange for your lucky coin. The vendor guides you to the door and sends you on your journey, now with additional shield points to protect you. ")
                print()
                time.sleep(2)
                player.loseItem("coin") # loseItem Method on player object removes item from player's inventory
                player.increaseHealth(50)
                time.sleep(3)
                room3_complete = True
                room5(player)

            else:
                print("You don't have a lucky coin. Please choose a different option.")
                print()
                time.sleep(3)

        # Checks if player wants to decline vendor's offer
        elif ("basement" in response) or ("Basement" in response) or ("door" in response) or ("Door" in response) or ("decline" in response) or ("Decline" in response) or ("4" in response):
            print("You decline the vendor's offer, and walk over to the door. It swings open with ease, and you continue your journey elsewhere.")
            print()
            time.sleep(2)
            room3_complete = True
            basement(player) # Sends player to basement function

        else: # Checks if player's response was valid: If not, continue loop and go back to start of room 1
            print("That is not a valid response. Please choose an option listed above.")
            print()
            time.sleep(3)