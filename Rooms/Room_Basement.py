# Imports
###############
import random
import time
from Rooms.Room_8 import room8
from otherFunctions import HELP

# Run basement function with player object
###############
def basement(player):
    basement_complete = False
    while not basement_complete:
        print("BASEMENT")
        print("------")
        print()
        print("You enter a very bright room, and despite being in the basement, you are blinded by the amount of white light. You call for help, listening to hear if anyone is there, and you hear a faint response. Behind you stands a hooded figure who appears to be running towards you. You quickly consider your options and you think that you can either run for your life or wait for him to approach you.")
        print("Type 'ME' if you want your stats OR type 'HELP' if you are stuck on this question.")
        response = (input("The choice is yours. What do you do?: ")).split() # Asks player what they want to do
        print()

        # Check if player wants help for what to do
        if ("Help" in response) or ("HELP" in response) or ("help" in response):
            print(HELP("basement", 1))
            print()
            time.sleep(5)

        # Checks if player wants to get their stats
        elif ("ME" in response) or ("Me" in response) or ("me" in response):
            player.ME()
            time.sleep(3)

        # Checks if player wants to run away from hooded man
        elif ("run" in response) or ("Run" in response) or ("away" in response) or ("Away" in response):
            basement_run_complete = False
            while not basement_run_complete:
                print("You run as fast as you can, but the man starts to chase after you, holding his axe upright ... You look ahead and see an unnamed door that you could go to, or you could fight him.")
                print("Type 'HELP' if you are stuck on this question.")
                decision = (input("The choice is yours. What do you do?: ")).split()
                print()

                if ("Help" in decision) or ("HELP" in decision) or ("help" in decision):
                    print(HELP("basement", 2))
                    print()
                    time.sleep(5)

                # Checks if player wants to open unnamed door while being chased
                elif ("door" in decision) or ("Door" in decision) or  ("unnamed" in decision) or ("Unnamed" in decision):
                    print("You quickly run over to the door and fling it open. You launch yourself through, shutting it behind you. You feel relieved, until you start to feel weightless, like you're floating ... You look down ... You're falling down the bottomless pit, which will eventually bring your end. You wonder to yourself ... 'How did I get here?'")
                    print()
                    time.sleep(3)
                    player.gameOver() # gameOver Method ends game for player and prevents game from repeating
                    basement_run_complete = True # Ends basement_run_complete loop
                    basement_complete = True # Ends basement loop

                # Checks if player wants to fight hooded figure
                elif ("fight" in decision) or ("Fight" in decision):
                    print("You stop and turned to face the man. He swings his axe at you, and you barely dodge it. You try and avoid his swings, until you see it. The infinity gauntlet. The man notices your attention to it and lifts up high ... and snaps. It is inevitable, and you slowly start to turn into dust, leaving forever ...")
                    print()
                    time.sleep(3)
                    player.gameOver()
                    basement_run_complete = True
                    basement_complete = True

                else:
                    print("That is not a valid response. Please choose again.")
                    print()
                    time.sleep(3)

        # Checks if player wants to wait for hooded figure to reach them
        elif ("wait" in response) or ("Wait" in response) or ("approach" in response) or ("Approach" in response) or ("reach" in response) or ("Reach" in response):
            basement_wait_complete = False
            while not basement_wait_complete:
                print("You let him reach you, and he asks for some money. You can either refuse to give him money and deny it, or you can pay him $10.")
                print("Type 'HELP' if you are stuck on this question.")
                decision = (input("The choice is yours. What do you do?: ")).split()
                print()

                if ("Help" in decision) or ("HELP" in decision) or ("help" in decision):
                    print(HELP("basement", 3))
                    print()
                    time.sleep(5)

                # Checks if player refuses to give them money
                elif ("refuse" in decision) or ("Refuse" in decision) or  ("deny" in decision) or ("Deny" in decision) or ("don't" in decision) or ("Don't" in decision) or ("do" in decision and "not" in decision):
                    print("You refuse to give him the money, and he knocks you out, and all you see is darkness as you feel the man dragging you across the floor ...")
                    print()
                    time.sleep(3)
                    # Checks if player has more than 10 health
                    if player.health > 10:
                        player.increaseHealth(-10) # increaseHealth Method on player object increases player's health by amt
                        time.sleep(3)
                        basement_wait_complete = True # Ends basement_wait_complete loop
                        basement_complete = True
                        room8(player) # Sends player to room 8 function
                    else:
                        print("You lose all your health and cease to exist.")
                        print()
                        time.sleep(3)
                        player.gameOver()
                        basement_wait_complete = True
                        basement_complete = True

                # Checks if player wants to pay hooded figure
                elif ("pay" in decision) or ("Pay" in decision) or ("give" in decision) or ("Give" in decision):
                    # Checks if user has $10 in their balance
                    if player.balance >= 10:
                        print("You pay the man $10, and he thanks you profusely. In return, he opens a portal to somewhere else, which you gladly step into to continue your journey, leaving the man behind in the basement ...")
                        print()
                        time.sleep(3)
                        player.addMoney(-10) # addMoney Method on player object adds money to player's balance
                        time.sleep(3)
                        basement_wait_complete = True
                        basement_complete = True
                        room8(player)

                    else:
                        print("You don't have enough money to give him, so he knocks you out, and all you see is darkness as you feel the man dragging you across the floor ...")
                        print()
                        time.sleep(3)
                        if player.health > 10:
                            player.increaseHealth(-10)
                            time.sleep(3)
                            basement_wait_complete = True
                            basement_complete = True
                            room8(player)
                        else:
                            print("You lose all your health and cease to exist.")
                            print()
                            time.sleep(3)
                            player.gameOver()
                            basement_wait_complete = True
                            basement_complete = True

                else:
                    print("That is not a valid response. Please choose again.")
                    print()
                    time.sleep(3)

        else: # Checks if player's response was valid. If not, send them back to start of basement.
            print("That is not a valid response. Please choose again.")
            print()
            time.sleep(3)
