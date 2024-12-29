# Imports
###############
import time
from Rooms.Room_8 import room8
from Rooms.Room_6 import room6
from Rooms.Room_9 import room9
from Rooms.Room_4 import room4
from otherFunctions import HELP

# Run room 5 function with player object
###############
def room5(player):
    room5_complete = False
    while not room5_complete:
        print("ROOM 5")
        print("------")
        print()
        print("You walk into an empty room, and you see a burning forge in the middle of the room. There is also a board that can teach you various skills, but you can only choose one to learn.")
        print("Type 'ME' if you want your stats OR type 'HELP' if you are stuck on this question.")
        response = (input("The choice is yours. What do you do?: ")).split() # Asks player what they want to do
        print()

        # Check if player wants help for what to do
        if ("Help" in response) or ("HELP" in response) or ("help" in response):
            print(HELP("5", 1))
            print()
            time.sleep(5)

        # Checks if player wants to get their stats
        elif ("ME" in response) or ("Me" in response) or ("me" in response):
            player.ME()
            time.sleep(3)

        # Checks if player wants to go to the forge
        elif ("burning" in response) or ("Burning" in response) or ("forge" in response) or ("Forge" in response) or ("middle" in response) or ("Middle" in response):
            room5_forge_complete = False
            while not room5_forge_complete:
                print("You walk over to the forge and look at the directions. It requires one metal object or quite a bit of health points. You can either sacrifice the lucky coin (If you have it), a sword (If you have it) or 50 health points. If you want, you can also decline the opportunity and leave the forge.")
                print("Type 'HELP' if you are stuck on this question.")
                decision = (input("The choice is yours. What do you do?: ").split())
                print()

                if ("Help" in decision) or ("HELP" in decision) or ("help" in decision):
                    print(HELP("5", 2))
                    print()
                    time.sleep(5)

                # Checks if player wants to sacrifice lucky coin for giant-axe
                elif ("coin" in decision) or ("Coin" in decision) or ("lucky" in decision) or ("Lucky" in decision):
                    # Checks if player has coin in their inventory
                    if "coin" in player.inventory:
                        print("You sacrifice your coin for a giant axe that will help you defeat the final boss, a wizard. A magical door opens up and you walk through it, continuing your adventure ...")
                        print()
                        time.sleep(3)
                        player.loseItem("coin") # loseItem Method on player object removes item from player's inventory
                        time.sleep(3)
                        player.pickUpItem("giant-axe") # pickUpItem Method on player object add's item to player's inventory
                        time.sleep(3)
                        room5_forge_complete = True # Ends room5_forge_complete loop
                        room5_complete = True # Ends room5 loop before sending player to room 8
                        room8(player) # Sends player to room 8 function
                    else:
                        print("You don't have the lucky coin in your inventory. Please choose again.")
                        print()
                        time.sleep(3)
                    
                # Checks if player wants to sacrifice sword for giant-axe
                elif ("sword" in decision) or ("Sword" in decision):
                    # Checks if player has sword in their inventory
                    if "sword" in player.inventory:
                        print("You sacrifice your sword for a giant axe that will help you defeat the final boss, a wizard. A magical door opens up and you walk through it, continuing your adventure ...")
                        print()
                        time.sleep(3)
                        player.loseItem("sword")
                        time.sleep(3)
                        player.pickUpItem("giant-axe")
                        time.sleep(3)
                        room5_forge_complete = True
                        room5_complete = True
                        room8(player)
                    else:
                        print("You don't have the sword in your inventory. Please choose again.")
                        print()
                        time.sleep(3)

                # Checks if player wants to sacrifice 50 health for giant-axe
                elif ("health" in decision) or ("Health" in decision) or ("50" in response):
                    # Checks if player has more than 50 health points
                    if player.health > 50:
                        print("You sacrifice 50 health points for a giant axe that will help you defeat the final boss, a wizard. A magical door opens up and you walk through it, continuing your adventure ...")
                        print()
                        time.sleep(3)
                        player.increaseHealth(-50) # increaseHealth Method on player object increases player's health by amt
                        time.sleep(3)
                        player.pickUpItem("giant-axe")
                        time.sleep(3)
                        room5_forge_complete = True
                        room5_complete = True
                        room8(player)
                    else:
                        print("You don't have 50 health points to sacrifice. Please choose something else.")
                        print()
                        time.sleep(3)

                # Checks if player wants to decline and not make a weapon
                elif ("decline" in decision) or ("Decline" in decision) or ("Don't" in response) or ("leave" in response) or ("Leave" in response):
                    print("You decide against going to the forge, and you walk away, contemplating whether you should've stayed to get a weapon for where you'll go next ...")
                    print()
                    time.sleep(3)
                    room5_forge_complete = True
                    room5_complete = True
                    room9(player) # Sends player to room 9 function

                else:
                    print("That is not a valid response. Please choose again.")
                    print()
                    time.sleep(3)

        # Checks if player wants to learn a skill
        elif ("board" in response) or ("Board" in response) or ("skills" in response) or ("Skills" in response) or ("learn" in response) or ("Learn" in response) or ("skill" in response) or ("Skill" in response):
            room5_skills_complete = False
            while not room5_skills_complete:
                print("You walk over to the board and look at the different skills you can learn. You can either learn how to jump higher to avoid enemies, run faster and speed past people, or learn how to fly.")
                print("Type 'HELP' if you are stuck on this question.")
                decision = (input("The choice is yours. What do you do?: ").split())
                print()

                if ("Help" in decision) or ("HELP" in decision) or ("help" in decision):
                    print(HELP("5", 3))
                    print()
                    time.sleep(5)

                # Checks if player wants to learn how to jump higher
                elif ("jump" in decision) or ("Jump" in decision) or ("higher" in decision) or ("Higher" in decision):
                    print("You decide that you want to learn how to jump higher. It tells you to crouch on one leg, and using your new bouncy shoes, you jump 20 ft in the air! You bounce around the room, and eventually jump over a mysterious wall, landing in a different room ...")
                    print()
                    time.sleep(3)
                    player.gainAbility("jump") # gainAbility Method on player object adds ability to player's abilities
                    time.sleep(3)
                    room5_skills_complete = True # Ends room5_skills_complete loop
                    room5_complete = True
                    room6(player) # Sends player to room 6 function

                # Checks if player wants to learn how to run faster
                elif ("run" in decision) or ("Run" in decision) or ("faster" in decision) or ("Faster" in decision) or ("speed" in decision) or ("Speed" in decision):
                    print("You decide that you want to learn how to run faster. You zoom through the instructions, and it tells you to move your arms quickly. As soon as you move your arms though, you're spriting across the room so fast that you accidentely break through 3 doors, and end up facing a mysterious wall ...")
                    print()
                    time.sleep(3)
                    player.gainAbility("run")
                    time.sleep(3)
                    room5_skills_complete = True
                    room5_complete = True
                    room9(player)

                # Checks if player wants to learn how to fly
                elif ("fly" in decision) or ("Fly" in decision):
                    print("You decide that you want to learn how to fly. It tells you flap your arms, and imagine yourself as a bird, floating amongst the clouds ... You follow it and start to hover in the air! You quickly lose control though, and end up flying up too fast, breaking through the ceiling and ending up on your back facing up, your mind blanking ...")
                    print()
                    time.sleep(3)
                    player.gainAbility("fly")
                    time.sleep(3)
                    room5_skills_complete = True
                    room5_complete = True
                    room4(player) # Sends player to room 4 function

                else:
                    print("That is not a valid response. Please choose again.")
                    print()
                    time.sleep(3)

        else: # Checks if player's response was valid. If not, send player back to beginning of room 5
            print("That is not a valid response. Please choose again.")
            print()
            time.sleep(3)
