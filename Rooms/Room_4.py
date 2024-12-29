# Imports
###############
import time
from Rooms.Room_7 import room7

# Run room 4 function with player object
###############
def room4(player):
    room4_complete = False
    while not room4_complete:
        print("ROOM 4")
        print("------")
        print()
        print("You wake up, and feel like you're in a nightmare. It is very dark, and you are on one side of a wobbly suspension bridge that can only take 2 people on it at a time. You are being chased by zombies, and you see 3 other people next to you: Bob, Tim & Mr. Cucumber. You only have 17 minutes to cross the bridge, otherwise, you'll be eaten. You can run across in 1 minute, Bob takes 2 minutes, Tim takes 5 minutes, and old Mr. Cucumber takes a whole 10 minutes to cross. Since one person needs to hold a lantern to see, 2 people can go across, but one person MUST come back with the lantern. People can stay at the other end by themselves though. Also, if two people are crossing, the total time they take is just how long the slower one takes, not both of their times combined. Everyone has to cross in time, not only you. What order of people will get everyone across in time?")
        print("Answer as if the faster person crossing would reach before the slower person. E.g. If it's you and Bob crossing, you would cross first and then Bob")
        print("*Not part of actual riddle -> Since this question is a riddle, you will not get any help to solve it.")
        print()
        # Inputs for riddle
        first_cross = (input("First person to cross the bridge: ")).split()
        second_cross = (input("Second person to cross the bridge: ")).split()
        first_back = (input("Person who comes back: ")).split()
        third_cross = (input("Third person to cross the bridge: ")).split()
        fourth_cross = (input("Fourth person to cross the bridge: ")).split()
        second_back = (input("Person who comes back: ")).split()
        fifth_cross = (input("Fifth person to cross the bridge: ")).split()
        sixth_cross = (input("Sixth person to cross the bridge: ")).split()

        # Checks if previous inputs correctly match up with answers to the riddle
        if ("i" in first_cross or "I" in first_cross or "me" in first_cross or "Me" in first_cross or "ME" in first_cross or player.name in first_cross) and ("bob" in second_cross or "Bob" in second_cross or "BOB" in second_cross) and ("i" in first_cross or "I" in first_cross or "me" in first_back or "Me" in first_back or "ME" in first_back or player.name in first_back) and ("tim" in third_cross or "Tim" in third_cross or "TIM" in third_cross) and ("cucumber" in fourth_cross or "Cucumber" in fourth_cross or "CUCUMBER" in fourth_cross) and ("bob" in second_back or "Bob" in second_back or "BOB" in second_back) and ("i" in first_cross or "I" in first_cross or "me" in fifth_cross or "Me" in fifth_cross or "ME" in fifth_cross or player.name in fifth_cross) and ("bob" in sixth_cross or "Bob" in sixth_cross or "BOB" in sixth_cross):
            print("You make it across the chasm alive, with everyone in tow. Your friends thank you for your courage and loyalty, as well as your quick thinking. You lie down, now out of danger and in time for well deserved rest. ")
            print()
            time.sleep(3)
            player.increaseKnowledge(50) # increaseKnowledge Method on player object increases player's knowledge 
            time.sleep(3)
            player.moreLoyal(25) # moreLoyal Method on player object increases player's loyalty points by input amt
            time.sleep(3)
            room4_complete = True # Ends room4 loop before moving player to room 7 
            room7(player) # Sends player to room 7 function
        
        else:
            print("You can't get everyone over in time! The zombies attack you and the fight doesn't last very long.")
            print()
            time.sleep(3)
            player.gameOver() # gameOver Method stops player from repeating game
            room4_complete = True # Ends room4 loop
