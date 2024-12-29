# Imports
###############
import random
import time
import art
from Rooms.Room_3 import room3
from Rooms.Room_4 import room4
from Rooms.Room_6 import room6
from otherFunctions import HELP

# Run room 2 function with player object
###############
def room2(player):
    room2_complete = False
    while room2_complete == False:
        print("ROOM 2")
        print("------")
        print()
        print("You enter the narrow passage and step out into the room. It is pitch black, and all you can see is the reflection of a lightbulb and darkness. A string dangles from the lightbulb, and a small flash lets you know that it was recently turned on ... You stick your leg out and feel in front of you. ... Nothing. ... You can move forward, but beware of what lies past it. Each step you take, the floor creaks under your weight, the sound echoing across the whole room.")
        print("Type 'ME' if you want your stats OR type 'HELP' if you are stuck on this question.")
        response = (input("The choice is yours. What do you do?: ")).split() # Asks player what they want to do
        print()

        # Check if player wants help for what to do
        if ("Help" in response) or ("HELP" in response) or ("help" in response):
            print(HELP("2", 1))
            print()
            time.sleep(5)

        # Checks if player wants to get their stats
        elif ("ME" in response) or ("Me" in response) or ("me" in response):
            player.ME()
            time.sleep(3)

        # Checks if player chooses to walk forward
        elif ("forward" in response) or ("Forward" in response) or ("walk" in response) or ("Walk" in response) or ("front" in response) or ("Front" in response):
            room2_forward_complete = False
            while not room2_forward_complete:
                print("You continue walking forward, until your arm brushes against something sticking out of the wall. You see a sticker saying 'The Great Wave off Kanagawa', which you recognize to be the really famous Japanese painting. Just before you turn towards the painting, you see a tunnel that says 'To The Lab'. Nothing is in front of you, just a dark hallway.")
                print("Type 'HELP' if you are stuck on this question.")
                # Asks player what they want to do
                response_Forward = (input("The choice is yours. What do you do?: ")).split() 
                print()

                if ("Help" in response_Forward) or ("HELP" in response_Forward) or ("help" in response_Forward):
                    print(HELP("2", 2))
                    print()
                    time.sleep(5)

                # Checks if player chooses to look at the painting after walking forward
                elif ("painting" in response_Forward) or ("Painting" in response_Forward) or ("inspect" in response_Forward) or ("Inspect" in response_Forward) or ("The Great Wave off Kanagawa" in response_Forward) or ("look" in response_Forward) or ("Look" in response_Forward):
                    # Loop in a list of strings to print out a painting from ASCII Art
                    for i in range(0, len(art.room2Art)):
                        print(art.room2Art[i])
                    print()
                    time.sleep(5)
                    print("You turn to your right and examine the painting. All is fine, until you spot a small note in the corner of the painting. It says: 'Loyalty, Knowledge & Speed - These 3 will make or break your adventure'. You shrug to yourself and hold on to the note for safe keeping. You quickly walk over to the tunnel, sliding down and taking your cryptic advice with you.")
                    print()
                    time.sleep(3)
                    # gainAbility Method on player object adds ability to player's abilities
                    player.gainAbility("secret message") 
                    room2_forward_complete = True # Ends room2 forward loop
                    room2_complete = True # Ends room2 loop before moving player to room 6
                    time.sleep(3)
                    room6(player) # Sends player to room 6 function

                # Checks if player chooses to go to the tunnel after walking forward
                elif ("tunnel" in response_Forward) or ("Tunnel" in response_Forward) or ("lab" in response_Forward) or ("Lab" in response_Forward):
                    print("You decide to go to the lab, and slowly lower yourself into the the tunnel. Your foot slips ... but you manage to stay upright, and you slide down the tunnel, leaving the darkness for someone else. ")
                    print()
                    room2_forward_complete = True
                    room2_complete = True
                    time.sleep(3)
                    room6(player)

                # Checks if player chooses to continue walking forward after previously walking forward
                elif ("forward" in response_Forward) or ("Forward" in response_Forward) or ("walk" in response_Forward) or ("Walk" in response_Forward) or ("front" in response_Forward) or ("Front" in response_Forward):
                    print("You continue to walk forward, despite all the warnings. The creaking grows louder and louder until ... CRACK!! The wood below your feet splits into two and you fall down into the gaping black hole in the ground. You hit the ground with a thud and feel lightheaded, and you can't remember anything. You blackout, falling into a dream ...")
                    print()
                    time.sleep(3)
                    # forgetAbility Method on player object removes a random ability from player's abilities
                    player.forgetAbility() 
                    # increaseHealth Method on player object increases player's health by input amt
                    player.increaseHealth(-25)
                    room2_forward_complete = True
                    room2_complete = True
                    time.sleep(3)
                    room3(player) # Sends player to room 3 function

                else:
                    print("That is not a valid response. Please answer the question correctly.")
                    print()
                    time.sleep(3)

            # Checks if player chooses to turn on lightbulb
        elif ("light" in response) or ("Light" in response) or ("bulb" in response) or ("Bulb" in response) or ("lightbulb" in response) or ("Lightbulb" in response) or ("pull" in response) or ("Pull" in response) or ("string" in response) or ("String" in response):
            room2_light_complete = False
            while not room2_light_complete:
                print("You carefully pull on the string to turn on the lightbulb, and it brightens, only slightly, sending a dim light through the room. To your right, you see some kind of riddle on the board. The light starts flickering, and you can inspect it if you want. ")
                print("Type 'HELP' if you are stuck on this question.")
                response_Light = (input("The choice is yours. What do you do?: ")).split() # Asks player what they want to do
                print()

                # Check if player wants help for what to do
                if ("Help" in response_Light) or ("HELP" in response_Light) or ("help" in response_Light):
                    print(HELP("2", 3))
                    print()
                    time.sleep(5)

                # Checks if player wants to look at the riddle after turning on light
                elif ("right" in response_Light) or ("Right" in response_Light) or ("board" in response_Light) or ("Board" in response_Light) or ("riddle" in response_Light) or ("Riddle" in response_Light):
                    print("You turn to your right and check out the riddle, made by Albert Einstein. If you solve the riddle, your intelligence level will go up, which could help you, so you decide to take a shot at it. Here is how it goes: ")
                    print()
                    time.sleep(3)
                    print("There are five houses lined up next to each other along a street. Each house is a different color, and each homeowner is of a different nationality, drinks a different beverage, smokes a different brand of cigar, and owns a different pet.")
                    print()
                    time.sleep(3)
                    print("The Englishman lives in the house with red walls.")
                    time.sleep(1)
                    print("The Swede keeps dogs.")
                    time.sleep(1)
                    print("The Dane drinks tea.")
                    time.sleep(1)
                    print("The house with green walls is just to the left of the house with white walls.")
                    time.sleep(1)
                    print("The owner of the house with green walls drinks coffee.")
                    time.sleep(1)
                    print("The man who smokes Pall Mall keeps birds.")
                    time.sleep(1)
                    print("The owner of the house with yellow walls smokes Dunhills.")
                    time.sleep(1)
                    print("The man in the center house drinks milk.")
                    time.sleep(1)
                    print("The Norwegian lives in the first house.")
                    time.sleep(1)
                    print("The Blend smoker has a neighbor who keeps cats.")
                    time.sleep(1)
                    print("The man who smokes Blue Masters drinks beer.")
                    time.sleep(1)
                    print("The man who keeps horses lives next to the Dunhill smoker.")
                    time.sleep(1)
                    print("The German smokes Prince.")
                    time.sleep(1)
                    print("The Norwegian lives next to the house with blue walls.")
                    time.sleep(1)
                    print("The Blend smoker has a neighbor who drinks water.")
                    time.sleep(1)
                    print("*Not part of actual riddle -> Since this question is a riddle, you will not get any help to solve it.")
                    time.sleep(1)
                    # Asks player what the answer to riddle is
                    fish_owner = (input("All of this is true, so who has the fish as a pet?: ")).split()
                    print()

                    # Checks if player answers riddle correctly
                    if ("german" in fish_owner) or ("German" in fish_owner) or ("green" in fish_owner) or ("Green" in fish_owner) or ("coffee" in fish_owner) or ("Coffee" in fish_owner) or ("prince" in fish_owner) or ("Prince" in fish_owner):
                        print("You correctly solved the riddle! As you start to walk and explore the room, you trip on something and fall head first through the flooring and into a black hole in the room. I guess smartness doesn't help everywhere ...")
                        print()
                        # increaseKnowledge Method on player object increases player's knowledge
                        player.increaseKnowledge(25)
                        room2_light_complete = True # Ends room2 light loop
                        room2_complete = True
                        time.sleep(3)
                        room3(player)

                    else:
                        print("You failed the riddle! As you start to walk and explore the room, you trip on something and fall head first through the flooring and into a black hole in the room.")
                        print()
                        room2_light_complete = True
                        room2_complete = True
                        time.sleep(3)
                        room3(player)

                # Checks if player wants to inspect the light after turning it on
                elif ("light" in response_Light) or ("Light" in response_Light) or ("lightbulb" in response_Light) or ("Lightbulb" in response_Light) or ("inspect" in response_Light) or ("Inspect" in response_Light):
                    print("You look up at the flickering light, but a bright red flash temporarily blinds you and you fall backwards, your eyes flashing with lights. Your head hits the ground very hard, and you feel yourself losing consciousness, falling into a trance.")
                    print()
                    room2_light_complete = True
                    room2_complete = True
                    time.sleep(3)
                    room4(player) # Sends player to room 4 function

                else:
                    print("That is not a valid response. Please answer the question correctly.")
                    print()
                    time.sleep(3)

        else: # Checks if player's response was valid: If not, continue loop and go back to start of room 2
            print("That is not a valid response. Please answer the question correctly.")
            print()
            time.sleep(3)
