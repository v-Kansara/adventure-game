# Imports
###############
import random
import time
from Rooms.Room_2 import room2
from Rooms.Room_Basement import basement
from otherFunctions import HELP

# Run room 1 function with player object
###############
def room1(player):
    room1_complete = False
    while not room1_complete:
        print("ROOM 1")
        print("------")
        print()
        print("You enter the lobby of the grand castle. You see a group of people huddled in the corner, whispering in some sort of strange language, maybe talking about you. To your left are stairs leading down to the basement, and in front of you is a door to ... room 2. There seems to be a small piece of junk on the floor and a loose paper all scrunched up as well.")
        print("Type 'ME' if you want your stats OR type 'HELP' if you are stuck on this question.")
        response = (input("The choice is yours. What do you do?: ")).split() # Asks player what they want to do
        print()

        # Check if player wants help for what to do
        if ("Help" in response) or ("HELP" in response) or ("help" in response):
            print(HELP("1", 1))
            print()
            time.sleep(5)

        # Checks if player wants to get their stats
        elif ("ME" in response) or ("Me" in response) or ("me" in response):
            player.ME()
            time.sleep(3)

        # Checks if player wants to go down the stairs
        elif ("stairs" in response) or ("Stairs" in response) or ("Basement" in response) or ("basement" in response) or ("Left" in response) or ("left" in response):
            print("You turn left and head down the stairs to the basement, leaving the rest ... for someone else.")
            print()
            time.sleep(3)
            room1_complete = True # Ends room1 loop before moving player to basement
            basement(player) # Sends player to basement function

        # Checks if player wants to go to door of room 2
        elif ("Door" in response) or ("door" in response) or ("room" in response and "2" in response) or ("Room" in response and "2" in response) or ("front" in response) or ("Front" in response) or ("Forward" in response) or ("forward" in response):
            print("You walk forward and tug on the door to room 2. It doesn't budge. You pull harder until you almost break the door out of the wall. It makes a creaking sound as it opens and you are shrouded with darkness. You step forward into the room ... to continue your journey elsewhere.")
            print()
            time.sleep(5)
            room1_complete = True
            room2(player) # Sends player to room 2 function

        # Checks if player wants to go to the group of people
        elif ("people" in response) or ("People" in response) or ("group" in response) or ("Group" in response) or ("other" in response) or ("Others" in response):
            print("You walk over where the mysterious group of huddle people are. You want a sidekick (cause why not?), but you'll need to pay them for their services. You check your pockets and find nothing but dust. Guess not today. You leave the huddle, but as you walk forward, your foot catches on the leg of some wooden table. You shout in pain, and fall down the stairs to the basement.")
            print()
            time.sleep(5)
            room1_complete = True
            basement(player)

        # Checks if player wants to pick up junk on the floor
        elif ("small" in response) or ("Small" in response) or ("junk" in response) or ("Junk" in response) or ("piece" in response) or ("Piece" in response):
            print("You pick up a dull, round, coin shaped object from off the ground. It's dusty and you estimate it to have been rusting for at least the past 100 years. WHOOOOoooooooSH! Suddenly, a cool gust of wind blows by and the coin looks as good as new. It has something written on it ... Heads = 75% ... Tails = 25%. You think the mysterious coin will land heads more than half the time. ")
            time.sleep(10)
            print()
            player.pickUpItem("coin") # Pick-Up Method on player object adds 'coin' item to their inventory
            time.sleep(3)
            print("After considering your options, you decide to flip the coin to see which room (Basement or Room 2) you'll go to.")
            # Asks player which room they want to go to if the coin lands heads or tails
            coinHeads = (input("If the coin comes up heads, you will go to: ")).split() # Asks player which room is heads
            print()
            time.sleep(3)
            coinResult = random.randint(0, 100) # Gets a random integer as coin flip result
            if ("basement" in coinHeads) or ("Basement" in coinHeads):
                if coinResult <= 75: # Coin is biased to land heads 75% of time
                    print("It's your lucky day! The coin lands heads, and you decide to go to the basement.")
                    print()
                    time.sleep(3)
                    room1_complete = True
                    basement(player)

                else:
                    print("You're very unlucky. The coin lands tails, and you decide to go to room 2.")
                    print()
                    time.sleep(3)
                    room1_complete = True
                    room2(player)

            elif ("room2" in coinHeads) or ("room" in coinHeads and "2" in coinHeads) or ("Room2" in coinHeads) or ("Room" in coinHeads and "2" in coinHeads):
                if coinResult <= 75:
                    print("It's your lucky day! The coin lands heads, and you decide to go to room 2.")
                    print()
                    time.sleep(3)
                    room1_complete = True
                    room2(player)

                else:
                    print("You're very unlucky. The coin lands tails, and you decide to go to the basement.")
                    print()
                    time.sleep(3)
                    room1_complete = True
                    basement(player)

            else: # Checks if player's response was valid: If not, sends them to basement
                print("That is not a valid response. Since you couldn't pick properly, the game sends you to the basement as punishment.")
                print()
                time.sleep(3)
                room1_complete = True
                basement(player)
        
        # Checks if player wants to pick up loose paper
        elif ("Loose" in response) or ("loose" in response) or ("paper" in response) or ("Paper" in response) or ("scrunched" in response) or ("Scrunched" in response):
            player.addMoney(100) # addMoney Method on player object increases value of player's balance by input amt
            room1_paper_complete = False
            while not room1_paper_complete:
                print("You yank up the crumpled bill from the ground. It's hard to clearly see it, but it looks like a $100 to you. By now, you're way too far away from the stairs to the basement, but you are close enough to reach the door to room 2. The crowd of people also grows closer, and you have to make a decision.")
                print("Type 'HELP' if you are stuck on this question.")
                time.sleep(3)
                decision = (input("What do you do?: ")).split()
                print()

                if ("Help" in decision) or ("HELP" in decision) or ("help" in decision):
                    print(HELP("1", 2))
                    print()
                    time.sleep(5)

                # Checks if player wants to go to room 2
                elif ("room" in decision and "2" in decision) or ("Room" in decision and "2" in decision) or ("door" in decision) or ("Door" in decision):
                    print("You look at the group of people, but decide against it. You walk over to the door to room 2, and tug on it. As you step into the doorway, you smile, taking your crisp $100 with you.")
                    print()
                    time.sleep(5)
                    room1_paper_complete = True # Ends room1 paper loop
                    room1_complete = True
                    room2(player)

                # Checks if player wants to go talk to group of people
                elif ("people" in decision) or ("People" in decision) or ("group" in decision) or ("Group" in decision) or ("other" in decision) or ("Others" in decision) or ("talk" in decision) or ("Talk" in decision) or ("crowd" in decision) or ("Crowd" in decision):
                    print("You wander over to the group of people and ask if anyone is willing to accompany you. One person raises their hand, and you gleefully pay them $20 for their services. They thank you, and you both walk over to the door to room 2, continuing your adventure.")
                    player.addMoney(-20)
                    # Asks player what sidekick's name is
                    sidekickName = input("Before you continue, you ask your sidekick what their name is. What is their name?: ")
                    print()
                    player.getSidekick(sidekickName) # getSidekick Method on player object sets player.sidekick to True
                    room1_paper_complete = True
                    room1_complete = True
                    room2(player)

                else:
                    print("That is not a valid response. Please choose again.")
                    print()
                    time.sleep(3)

        else: # Checks if player's response was valid: If not, continue loop and go back to start of room 1
            print("That is not a valid response. Please do a command that is listed above.")
            print()
            time.sleep(3)
