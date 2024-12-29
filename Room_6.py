# Imports
###############
import time
from Rooms.Room_Basement import basement
from Rooms.Room_9 import room9
from otherFunctions import HELP

# Run room 6 function with player object
###############
def room6(player):
    room6_complete = False
    while not room6_complete:
        print("ROOM 6")
        print("------")
        print()
        print("You are in a lab, and in front of you, there are 6 chemicals on a table. Next to you, there is a trap door that leads to the basement.")
        print("Type 'ME' if you want your stats OR type 'HELP' if you are stuck on this question.")
        response = (input("The choice is yours. What do you do?: ")).split() # Asks player what they want to do
        print()

        # Check if player wants help for what to do
        if ("Help" in response) or ("HELP" in response) or ("help" in response):
            print(HELP("6", 1))
            print()
            time.sleep(5)

        # Checks if player wants to get their stats
        elif ("ME" in response) or ("Me" in response) or ("me" in response):
            player.ME()
            time.sleep(3)

        # Checks if player wants to go to the table with chemicals
        elif ("chemicals" in response) or ("Chemicals" in response) or ("chemical" in response) or ("Chemical" in response) or ("table" in response) or ("Table" in response):
            print("You decide to go to the table with the chemicals, and you also notice the door to get out of the room. The door is in front of you, though there is a catch to open it: Only a combination of two of specific chemicals on the table will be able to open the door, the other combinations of chemicals will either do nothing or light the room on fire. Here is what you already know:")
            print()
            time.sleep(1)
            print("3 out of the 6 chemicals start a fire; 2 out of the 6 chemicals do nothing; 1 chemical out of the 6 opens the door; You have to use a combination of only 2 chemicals at a time to try and open the door.")
            print()
            time.sleep(3)
            print("If one of the chemicals does nothing, then a combination with a chemical that starts a fire will end up doing nothing.")
            print()
            time.sleep(3)
            print("If one of the chemicals starts a fire and the other opens the door, then a fire will start.")
            time.sleep(3)
            print()
            print("1. Chemical A + Chemical E = Fire")
            time.sleep(1)
            print("2. Chemical D + Chemical F = Nothing")
            time.sleep(1)
            print("3. Chemical B + Chemical A = Fire")
            time.sleep(1)
            print("4. Chemical F + Chemical E = Opens Door")
            time.sleep(1)
            print("5. Chemical D + Chemical B = Fire")
            time.sleep(1)
            print("6. Chemical F + Chemical C = Nothing")
            print()
            time.sleep(1)
            used_chemicals = False
            while not used_chemicals:
                decision = (input("If all of this is true, then which combination of 2 chemicals (Besides FE) will open the door? Answer using the letters of the two chemicals (E.g. EF, AB, etc.): ")).split()
                print()

                # Checks if player enters right combination of chemicals
                if ("EC" in decision) or ("CE" in decision) or ("ec" in decision) or ("Ec" in decision) or ("eC" in decision) or ("ce" in decision):
                    print("You throw the mixture of Chemical E & Chemical C on the door, and it breaks open! You walk past the rubble, continuing your adventure with a little more knowledge, something that could help you later on ...")
                    print()
                    time.sleep(3)
                    # increaseKnowledge Method on player object increase player's knowledge by amt
                    player.increaseKnowledge(25) 
                    time.sleep(3)
                    used_chemicals = True # Ends loop to see if player actually used different chemicals
                    room6_complete = True # Ends room6 loop 
                    room9(player) # Sends player to room 9 function

                elif ("EF" in decision) or ("FE" in decision) or ("ef" in decision) or ("Ef" in decision) or ("eF" in decision) or ("fe" in decision):
                    print("That is already known. Please find the other combination that breaks the door.")
                    print()
                    time.sleep(3)

                else: # ELSE happens when player entered wrong chemical combination
                    print("You throw the mixture of the two chemicals, and they accidentaly land on an Air conditioner (Why is that in the castle?) which almost immediately gets disintegrated, but the chemicals short it and light the whole room on fire! You quickly search for any other way to escape, but the trap door has sealed itself and you are stuck there, the room slowly engulfing in flames, you wonder to yourself, 'Why did I come here?' ...")
                    print()
                    time.sleep(5)
                    player.gameOver() # gameOver Method ends the game for the player and prevents game to repeat
                    used_chemicals = True 
                    room6_complete = True

        # Checks if player wants to go to the trap door
        elif ("trap" in response) or ("Trap" in response) or ("trapdoor" in response) or ("Trapdoor" in response) or ("basement" in response) or ("Basement" in response):
            print("You take a look at the table, but decide against it and open the trap door. There is a ladder, and you start to climb down it, until you step past a rung and lose your footing. Your hands start to sweat and you slide of the ladder, falling down the narrow vent-like passage to the basement, thudding against the sides of the walls as you go ...")
            print()
            time.sleep(3)
            player.increaseHealth(-20)
            time.sleep(3)
            room6_complete = True
            basement(player) # Sends player to basement function

        else:
            print("That is not a valid response. Please choose again.")
            print()
            time.sleep(3)