# Imports
###############
import random
import time
from Rooms.Room_7 import room7
from Rooms.Room_9 import room9
from Rooms.Room_Maze import maze
from otherFunctions import HELP

# Run room 8 function with player object
###############
def room8(player):
    room8_complete = False
    while not room8_complete:
        print("ROOM 8")
        print("------")
        print()
        print("You enter a lavish room, filled with gold and jewelery. Before you can start exploring, a small, cone-shaped figure emerges from the shadows, and presents himself to be the minion of the wizard. He comes with a scroll, that has a message saying: ")
        print()
        time.sleep(3)
        print("Those who want the gold must first posses the three golds of being brave, knowledgable & skilled.")
        print()
        time.sleep(3)
        print("You shake your head in confusion, but he approaches you and starts to act more threateningly towards you. You look around and decide that you can either run away to the door behind you, try and fight the minion or look around the room for anything else to do.")
        print("Type 'ME' if you want your stats OR type 'HELP' if you are stuck on this question.")
        response = (input("The choice is yours. What do you do?: ")).split()
        print()

        # Check if player wants help for what to do
        if ("Help" in response) or ("HELP" in response) or ("help" in response):
            print(HELP("8", 1))
            print()
            time.sleep(5)

        # Checks if player wants to get their stats
        elif ("ME" in response) or ("Me" in response) or ("me" in response):
            player.ME()
            time.sleep(3)

        # Checks if player decides to run away from minion
        elif ("run" in response) or ("Run" in response) or ("away" in response) or ("Away" in response) or ("behind" in response) or ("Behind" in response):
            print("You don't want any trouble, and decide to run away before the minion can come after you. You quickly spin around and open the door to a different room, perhaps sealing your fate ...")
            print()
            time.sleep(3)
            room8_complete = True # Ends room8 loop
            room9(player) # Sends player to room 9 function

        # Checks if user wants to fight minion
        elif ("fight" in response) or ("Fight" in response) or ("attack" in response) or ("Attack" in response):
            print("After considering your options, you decide to fight the minion. You check your inventory to see what weapons you have: ")
            print(player.inventory)
            print()
            time.sleep(3)

            # Checking if player has both weapons in inventory
            if ("giant-axe" in player.inventory) and ("sword" in player.inventory):
                weaponChoice = (input("You check your inventory, and you have both a giant axe and a sword. You have to decide one, so you randomly pick one weapon, which is: ")).split()
                # Checks which weapon player picks
                if ("sword" in weaponChoice) or ("Sword" in weaponChoice):
                    player.setWeapon("sword") # setWeapon Method on player object sets player's current weapon to that weapon
                else:
                    player.setWeapon("giant-axe")

            # Checks if player only has a sword in inventory 
            elif ("sword" in player.inventory):
                player.setWeapon("sword")

            # Checks if player only has a giant-axe in inventory
            elif ("giant-axe" in player.inventory):
                player.setWeapon("giant-axe")

            else: # If not above, then player doesn't have any weapons in their inventory
                print("You don't have any weapons in your inventory, so you'll have to fight the minion with your hands, though it could be very dangerous.")
                print()
                time.sleep(3)

            # Checking the player's equipped weapon (or hands)
            if player.weapon == "sword" or player.weapon == "giant-axe":
                player_won = False
                while not player_won:
                    print("After choosing your weapon, you approach the minion and figure that you can either swing at him or try and slash him.")
                    print("Type 'HELP' if you are stuck on this question.")
                    decision = (input("The choice is yours. What do you do?: ")).split()
                    print()

                    if ("Help" in decision) or ("HELP" in decision) or ("help" in decision):
                        print(HELP("8", 2))
                        print()
                        time.sleep(5)

                    # Checks if player wants to swing at minion
                    elif ("swing" in decision) or ("Swing" in decision):
                        if random.randint(0, 1) == 1: # Randomly generates value to determine if player defeats minion
                            print("You swing at the minion, and you get a direct hit! You eliminate him and gain some new stats: ")
                            print()
                            time.sleep(3)
                            player.moreLoyal(20) # moreLoyal Method on player object increases player's loyalty points by amt
                            time.sleep(3)
                            player.getSkilled(30) # getSkilled Method on player object increases player's skill points by amt
                            time.sleep(3)
                            player_won = True # Ends player_won loop
                            room8_complete = True # Ends room 8 loop
                            room9(player)
                        else:
                            print("You swing at the minion, but you miss, so he casts a spell on you which turns you into a frog. You croak and croak until your mind goes blank and you feel dizzy. How did you every get in that decision? ...")
                            print()
                            time.sleep(3)
                            player.gameOver() # gameOver Method ends game for player and prevents game from repeating
                            player_won = True
                            room8_complete = True

                    # Checks if player wants to slash minion
                    elif ("slash" in decision) or ("Slash" in decision):
                        print("You try to slash the minion into pieces, but you miss wildly and your weapon hit the floor, breaking it and falling down into the hole. In a mad dash to safety, you dive down the hole, sliding down, though your weapon is nowhere to be found. As you get up from your fall, you suddenly see thousands of spectators ...")
                        print()
                        player.increaseHealth(-10) # increaseHealth Method on player object increases player's health by amt
                        time.sleep(3)
                        player.loseItem(player.weapon) # loseItem Method on player object makes player lose specified item
                        time.sleep(3)
                        player_won = True
                        room8_complete = True
                        room7(player) # Sends player to room 7 function

                    else:
                        print("That is not a valid response. Please choose again.")
                        print()
                        time.sleep(3)

            else:
                print("You'll have to go with your hands, so you approach the minion and try to attack him before he inflicts damage on you. ")
                print()
                time.sleep(3)
                print("You go up to the wizard and throw a few punches, but he swiftly dodges them and casts a spell on you, turning you into an irrelevant speck of dust. You no longer feel anything as you start shrinking, and you wonder how you got yourself into a situation like that ...")
                print()
                time.sleep(3)
                player.gameOver()
                room8_complete = True

        # Checks if player wants to look around for something else to do
        elif ("look" in response) or ("Look" in response) or ("around" in response) or ("Around" in response) or ("else" in response) or ("Else" in response):
            player_won = False
            while not player_won:
                print("You decide to search the room for anything else that you can do, and luckily, you spot an open window. You walk over to the window, and contemplate whether to jump out our not. Since you have no choice, you jump outside and quickly hold onto the side of the castle. Your feet dangle high above the ground, which you can no longer see. A dragon appears out of nowhere, and you sense that the perfect moment to jump on it is near.")
                print("Type 'HELP' if you are stuck on this question.")
                decision = (input("The choice is yours. Do you jump on the dragon or stay on the side of the castle?: ")).split()
                print()

                if ("Help" in decision) or ("HELP" in decision) or ("help" in decision):
                        print(HELP("8", 3))
                        print()
                        time.sleep(5)

                # Checks if player wants to stay on side of castle
                elif ("stay" in decision) or ("Stay" in decision) or ("remain" in decision) or ("Remain" in decision):
                    print("You decide to take the safe route of staying on the side of the castle, but a strong gust of cold air comes by, and your hand slips, causing you to start falling down. As the end is near, you wonder to yourself, 'Why didn't I jump on the dragon?' ...")
                    print()
                    time.sleep(3)
                    player.gameOver()
                    player_won = True
                    room8_complete = True

                # Checks if player wants to jump on dragon
                elif ("jump" in decision) or ("Jump" in decision) or ("dragon" in decision) or ("Dragon" in decision):
                    print("You swiftly jump on the dragon, barely clinging on to its slippery scales. It brings you down near the ground before slowly letting you climb off of it. As it flies away, its tail hits your arm and cuts you, though almost instantly turning into a scar of the dragon. You look forward, and see the new challenege in front of you ...")
                    print()
                    time.sleep(5)
                    player.increaseHealth(-5)
                    time.sleep(3)
                    player_won = True
                    room8_complete = True
                    maze(player) # Sends player to maze function

                else:
                    print("That is not a valid response. Please choose again.")
                    print()
                    time.sleep(3)

        else: # Checks if player's response is valid. If not, send back to start of room 8
            print("That is not a valid response. Please choose again.")
            print()
            time.sleep(3)
