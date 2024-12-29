# Imports
###############
import random
import time
from Rooms.Room_Vault import vault
from otherFunctions import HELP

# Run room 9 function with player object
###############
def room9(player):
    room9_complete = False
    while not room9_complete:
        print("ROOM 9")
        print("------")
        print()
        print("You enter a massive corridor, and you see a figure facing towards you at the other end. He slowly approaches you and introduces himself as the castle's owner, the supreme wizard. He tells you that since you have come all this way, you must fight him to get his riches. If not, he will eliminate you and your story will be forgotten. He explains all the tests and battles he will throw at you. You will have to face 3 challenges and face the wizard in a duel, but you only have 2 lives, so if you mess up more than once, it's the end for you. If you have a sidekick, you will get 3 lives. Type 'ME' if you want your stats OR type 'HELP' if you are stuck on this question.")
        response = (input("Otherwise, type 'Continue': ")).split() # Asks player what they want to do
        print()
        # Checks if player has a sidekick; If yes, they get 3 lives, if not, they get only 2 lives
        if player.sidekick[0] == True:
            player_lives = 3 # Sets player's lives for battle (Not an instance of player object; Just local to room 9 function)
        else:
            player_lives = 2

        # Check if player wants help for what to do
        if ("Help" in response) or ("HELP" in response) or ("help" in response):
            print(HELP("9", 1))
            print()
            time.sleep(5)

        # Checks if player wants to get their stats
        elif ("ME" in response) or ("Me" in response) or ("me" in response):
            player.ME()
            time.sleep(3)

        # Checks if player wants to continue
        elif ("CONTINUE" in response) or ("Continue" in response) or ("continue" in response):
            print("TEST 1")
            print("------")
            print()
            time.sleep(3)
            numToSqrt = random.randint(1, 100000)
            numCorrect = round((numToSqrt ** 0.5), 3) # Rounds sqrt of random number to nearest thousandth
            print("What is the square root of " + str(numToSqrt) + "? Round to the nearest thousandTH.")
            answer = (input("What is your answer?: ")).split()
            print()

            # Checks if player's answer was correct
            if str(numCorrect) in answer:
                print("That was correct! You can move on to the next question with all lives remaining")
                print()
                time.sleep(3)
                print("You now have: " + str(player_lives) + " lives left!")
                print()
                time.sleep(3)
                test1_complete = True # Allows player to move on to test 2

            else:
                print("That was incorrect! The correct answer was " + str(numCorrect) + ". You have lost one life.")
                print()
                time.sleep(3)
                player_lives -= 1 # Subtracts 1 life from player's total lives
                print("You now have: " + str(player_lives) + " lives left!")
                print()
                time.sleep(3)
                test1_complete = True

            # Checks if test 1 completed
            if test1_complete:
                print("TEST 2")
                print("------")
                print()
                time.sleep(3)
                print("This time, your loyalty will be checked. If you have any loyalty points, you pass. If not, you FAIL.")
                print()
                time.sleep(3)

                # Check if player's loyalty points are greater than 0
                if player.loyalty > 0:
                    print("Congratulations! You have " + str(player.loyalty) + " loyalty points! You pass the second test and move on to the third and final test.")
                    print()
                    time.sleep(3)
                    test2_complete = True # Allows player to move on to test 3
                else:
                    print("You have 0 loyalty points. Because you can't be loyal, you FAIL this test. You have lost one life.")
                    print()
                    time.sleep(3)
                    player_lives -= 1
                    print("You now have: " + str(player_lives) + " lives left!")
                    print()
                    time.sleep(3)
                    test2_complete = True
                    if player_lives == 0:
                        print("You have lost all lives for the final battle. Better luck next time ...")
                        print()
                        time.sleep(3)
                        # gameOver Method on player object ends game for player and prevents game from repeating
                        player.gameOver() 
                        test2_complete = False # Prevents player from moving on
                        room9_complete = True # Ends room9 loop
                
                # Checks if test 2 was completed
                if test2_complete:
                    print("TEST 3")
                    print("------")
                    print()
                    time.sleep(3)
                    print("For the 3rd and Final Test, you will have to type a sentence and if you take too long, you will FAIL.")
                    print()
                    time.sleep(3)
                    print("Type the sentence exactly as it is. (Include all capitals and punctuation, b/c it must be 100% accurate to count. The time you have to beat is: 10 seconds. If you take longer, then you will fail. The high score: is 7.5 seconds. If you type faster, then you will get 50 extra points during your fight against the wizard.")
                    print()
                    time.sleep(8)
                    print("Here is the sentence you have to type: ")
                    print("Wizards watch wonders and wish for wings and wands.")
                    print("On your mark, get set, GO!")
                    print()
                    time.sleep(3)
                    start_time = time.time() # Gets time right before player can answer
                    answer = input("Type Here: ")
                    end_time = time.time() # Gets time after player has answered
                    print()
                    time.sleep(3)
                    # Checks if player typed correctly
                    if answer == "Wizards watch wonders and wish for wings and wands.":
                        # Calculates player's time by subtracting initial time from final time
                        player_time = end_time - start_time 
                        if player_time <= 10:
                            print("You took " + str(player_time) + " seconds to type the statement!")
                            print()
                            print("You took less than 10 seconds, so you pass and move on to the final battle!")
                            print()
                            time.sleep(3)
                            test3_complete = True # Allows player to move onto battle
                        else:
                            print("You took " + str(player_time) + " seconds to type the statement!")
                            print()
                            print("You took more than 10 seconds, so you fail and lose one life.")
                            print()
                            time.sleep(3)
                            player_lives -= 1
                            print("You now have: " + str(player_lives) + " lives left!")
                            print()
                            time.sleep(3)
                            # If player has 1 life left, they can move on past test 3
                            test3_complete = True
                            if player_lives == 0:
                                print("You have lost all lives for the final battle. Better luck next time ...")
                                print()
                                time.sleep(3)
                                player.gameOver()
                                test3_complete = False # test3_complete is reset to False IF player lost their last life
                                room9_complete = True
            
                    else:
                        print("You didn't type the correct statement! You are automatically disqualified & it is GAME OVER for you.")
                        print()
                        time.sleep(3)
                        player.gameOver()
                        test3_complete = False
                        room9_complete = True

                    if test3_complete:
                        print("Congratulations! You made it past all the tests that the wizard threw at you. For the final battle, you will get an extra 50 health points because I am kind.")
                        print()
                        time.sleep(3)
                        player.increaseHealth(50) # increaseHealth Method on player object increases player's health by amt
                        time.sleep(3)
                        wizard_health = 300 # Wizard's health during battle
                        wizard_counter = 0 # Necessary to track how many times wizard has hit the player
                        print("The wizard has 300 health, and he will attack with 15 points of damage each time, but once every 3 times, he will inflict a damage of 20 points. You have three different attack methods that you can use:")
                        time.sleep(1)
                        print("1. KA-BOOM (Can only use 1 time, but inflicts 75 points of damage per use)")
                        time.sleep(1)
                        print("2. Boom (Can 3 times, but inflicts 50 points of damage per use)")
                        time.sleep(1)
                        print("3. Pow (Can use 5 times, but only inflicts 15 points of damage per use)")
                        time.sleep(3)
                        print("The battle starts, and it's your turn to attack the wizard. Press 1 to use the KA-BOOM, 2 to use the Boom or 3 to use the Pow.")
                        KA_Boom_used = False # Important to prevent player from using one attack over and over again
                        Boom_counter = 0 # Tracks how many times player uses Boom Attack
                        Pow_counter = 0 # Tracks how many times player uses Pow Attack
                        player_won = False # To keep player in battle UNTIL one person is eliminated
                        while not player_won:
                            if player.health > 0:
                                attack = input("The choice is yours. What do you do?: ")
                                print()
                                if attack == "1":
                                    if not KA_Boom_used:
                                        print("You attack the wizard with the KA-BOOM Attack. The wizard loses 75 points of health.")
                                        wizard_health -= 75
                                        KA_Boom_used = True
                                        print("The wizard's health is now: " + str(wizard_health))
                                        print()
                                        time.sleep(3)
                                        if wizard_health > 0:
                                            wizard_counter += 1
                                            if (wizard_counter % 3) == 0:
                                                print("The wizard attacks you with 20 points of damange.")
                                                print()
                                                time.sleep(3)
                                                player.increaseHealth(-20)
                                                time.sleep(3)
                                            else:
                                                print("The wizard attacks you with 15 points of damage.")
                                                print()
                                                time.sleep(3)
                                                player.increaseHealth(-15)
                                                time.sleep(3)
                                        else:
                                            print("Congratulations! You did it! The wizard has finally been defeated and you quickly snag his key to the secret vault!")
                                            print()
                                            time.sleep(3)
                                            player_won = True
                                            room9_complete = True # Ends room9 loop
                                            # Sends player to vault with 'wizard' as their MethodToWin
                                            vault(player, "wizard") 
                                    else:
                                        print("You have already used the KA-BOOM Attack. Please use a different attack.")
                                        print()
                                        time.sleep(3)

                                elif attack == "2":
                                    Boom_counter += 1 # Adds 1 before using actual attack since counter starts at 0
                                    if Boom_counter <= 3:
                                        print("You attack the wizard with the Boom Attack. The wizard loses 50 points of health.")
                                        wizard_health -= 50
                                        print("The wizard's health is now: " + str(wizard_health))
                                        print()
                                        time.sleep(3)
                                        if wizard_health > 0:
                                            wizard_counter += 1
                                            if (wizard_counter % 3) == 0:
                                                print("The wizard attacks you with 20 points of damange.")
                                                print()
                                                time.sleep(3)
                                                player.increaseHealth(-20)
                                                time.sleep(3)
                                            else:
                                                print("The wizard attacks you with 15 points of damage.")
                                                print()
                                                time.sleep(3)
                                                player.increaseHealth(-15)
                                                time.sleep(3)
                                        else:
                                            print("Congratulations! You did it! The wizard has finally been defeated and you quickly snag his key to the secret vault!")
                                            print()
                                            time.sleep(3)
                                            player_won = True
                                            room9_complete = True
                                            vault(player, "wizard")
                                    else:
                                        print("You have already used the Boom Attack 3 times. Please use a different attack.")
                                        print()
                                        time.sleep(3)

                                elif attack == "3":
                                    Pow_counter += 1
                                    if Pow_counter <= 5:
                                        print("You attack the wizard with the Pow Attack. The wizard loses 15 points of health.")
                                        wizard_health -= 15
                                        print("The wizard's health is now: " + str(wizard_health))
                                        print()
                                        time.sleep(3)
                                        if wizard_health > 0:
                                            wizard_counter += 1
                                            if (wizard_counter % 3) == 0:
                                                print("The wizard attacks you with 20 points of damange.")
                                                print()
                                                time.sleep(3)
                                                player.increaseHealth(-20)
                                                time.sleep(3)
                                            else:
                                                print("The wizard attacks you with 15 points of damage.")
                                                print()
                                                time.sleep(3)
                                                player.increaseHealth(-15)
                                                time.sleep(3)
                                        else:
                                            print("Congratulations! You did it! The wizard has finally been defeated and you quickly snag his key to the secret vault!")
                                            print()
                                            time.sleep(3)
                                            player_won = True
                                            room9_complete = True
                                            vault(player, "wizard")
                                    else:
                                        print("You have already used the Pow Attack 5 times. Please use a different attack.")
                                        print()
                                        time.sleep(3)

                                else:
                                    print("That is not a valid response. Please choose again.")
                                    print()
                                    time.sleep(3)

                            else:
                                print("Oh No! The wizard manages to defeat you and you slowly start to disappear, vanquishing from the face of planet Earth, never to be seen again ...")
                                print()
                                time.sleep(3)
                                player.gameOver()
                                player_won = True
                                room9_complete = True

        else: # Checks if player's response was valid. If not, send player back to start of room 9
            print("That is not a valid response. Please choose again.")
            print()
            time.sleep(3)