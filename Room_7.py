# Imports
###############
import random
import time
from Rooms.Room_9 import room9

# Run room 7 function with player object
###############
def room7(player):
    room7_complete = False
    while not room7_complete:
        print("ROOM 7")
        print("------")
        print()
        print("You walk into an arena, filled with thousands upon thousands of spectators, all eager to watch your duel with two other wizards, both of which are highly intelligent as well. Here are the rules of the duel:")
        print()
        time.sleep(3)
        print("You will have to use a wand to defeat the other two wizards.")
        print()
        time.sleep(1)
        print("The round starts with you, then goes to Bob and then to Hank. The duel will keep going until only one wizard remains.")
        print()
        time.sleep(3)
        print("Your wand's strength (% chance of turning someone into a tree) will have a randomized chance of being anywhere from 0% effective to 100% effective.")
        print()
        time.sleep(3)
        print("Bob has a wand that has a 40% chance of turning you into an orange while Hank has a wand that has a 60% chance of turning you into a flower vase. Since neither knows what level wand you will get, they will always target each other unless if only either Bob or Hank remains to fight you.")
        print()
        time.sleep(8)
        print("It's time now. Your wand's strength is ... ")
        print()
        time.sleep(3)
        player_wandStrength = random.randint(0, 9)
        print(str((player_wandStrength) * 10) + "%!") # Randomly sets player's wand strength
        print()

        # Checks if player turns Hank into a tree
        if (random.randint(0, 9)) <= (player_wandStrength):
            print("You successfully turn Hank into a tree!")
            print()
            time.sleep(3)
            player_won_A = False
            while not player_won_A:
                # Checks if Bob turns player into an orange
                if (random.randint(0, 9)) <= 3:
                    print("Unfortunately, Bob manages to turn you into an orange with his spell.")
                    print()
                    time.sleep(3)
                    player.gameOver() # gameOver Method ends game for player and prevents game from repeating
                    player_won_A = True # Ends player_won_A loop
                    room7_complete = True # Ends room7 loop
                else:
                    # If not, Bob's spell doesn't work and player survives
                    print("Bob tries to turn you into an orange and his spell doesn't work, so now it's your turn. You cast your spell towards Bob.")
                    print()
                    time.sleep(3)
                    # Checks if player turns Bob into a tree after he misses the player
                    if (random.randint(0, 9)) <= (player_wandStrength):
                        print("You cast your spell on Bob, and he turns into a tree! You win, and are escorted out with your giant trophy, eager to face the next challenge ...")
                        print()
                        time.sleep(3)
                        player_won_A = True
                        room7_complete = True
                        room9(player) # Sends player to room 9 function
                    else:
                        # Checks if player misses Bob and returns them to the loop where its Bob's turn
                        print("You try to turn Bob into a tree, but your spell doesn't work, so now it's his turn, and he casts his spell towards you.")
                        print()
                        time.sleep(3)

        # Checks if player misses Hank on the first try
        else:
            print("You try to turn Hank into a tree, but your spell doesn't work, so now it's Bob's turn, and he casts his spell towards Hank.")
            print()
            time.sleep(3)
            player_won_A = False
            while not player_won_A:
                # Checks if Bob turns Hank into an orange
                if (random.randint(0, 9)) <= 3: # *
                    print("Bob manages to turn Hank into an orange with his spell, so now it's your turn, and you cast your spell towards Bob.")
                    print()
                    time.sleep(3)
                    player_won_A_Loop1 = False
                    while not player_won_A_Loop1:
                        # Checks if player turns Bob into a tree
                        if (random.randint(0, 9)) <= (player_wandStrength):
                            print("You cast your spell on Bob, and he turns into a tree! You win, and are escorted out with your giant trophy, eager to face the next challenge ...")
                            print()
                            time.sleep(3)
                            player_won_A_Loop1 = True # Ends player_won_A_Loop1 loop
                            player_won_A = True
                            room7_complete = True
                            room9(player)
                        else: # Checks if player misses Bob
                            print("You try to turn Bob into a tree, but your spell doesn't work, so now it's his turn, and he casts his spell towards you.")
                            print()
                            time.sleep(3)
                            # Checks if Bob turns player into an orange
                            if (random.randint(0, 9)) <= 3:
                                print("Unfortunately, Bob manages to turn you into an orange with his spell.")
                                print()
                                time.sleep(3)
                                player.gameOver()
                                player_won_A_Loop1 = True # Not really true, just to end the loop
                                player_won_A = True # Not really true, just to end the loop
                                room7_complete = True
                            else: # Checks if Bob misses and sends player back to loop where it is their turn against Bob
                                print("Bob tries to turn you into an orange and his spell doesn't work, so now it's your turn. You cast your spell towards Bob.")
                                print()
                                time.sleep(3)

                # Checks if Bob misses Hank
                else:
                    player_won_A_Loop2 = False
                    while not player_won_A_Loop2:
                        print("Bob tries to turn Hank into an orange and his spell doesn't work, so now it's Hank's turn. Hank casts a spell towards Bob.")
                        print()
                        time.sleep(3)
                        # Checks if Hank turns Bob into a flower vase
                        if (random.randint(0, 9)) <= 5:
                            print("Hank casts his spell on Bob, and Bob turns into a flower vase! Now it's your turn, and you cast your spell towards Hank.")
                            print()
                            time.sleep(3)
                            player_won_A_Loop2_p1 = False
                            while not player_won_A_Loop2_p1:
                                # Checks if player turns Hank into a tree
                                if (random.randint(0, 9)) <= (player_wandStrength):
                                    print("You cast your spell on Hank, and he turns into a tree! You win, and are escorted out with your giant trophy, eager to face the next challenge ...")
                                    print()
                                    time.sleep(3)
                                    player_won_A_Loop2_p1 = True # Ends player_won_A_Loop2_p1 loop
                                    player_won_A_Loop2 = True # Ends player_won_A_Loop2 loop
                                    player_won_A = True
                                    room7_complete = True
                                    room9(player)
                                else: # Checks if player misses Hank
                                    print("You try to turn Hank into a tree, but your spell doesn't work, so now it's his turn, and he casts his spell towards you.")
                                    print()
                                    time.sleep(3)
                                    # Checks if Hank turns player into a flower vase
                                    if (random.randint(0, 9)) <= 5:
                                        print("Unfortunately, Hank turns you into a flower vase with his spell.")
                                        print()
                                        time.sleep(3)
                                        player.gameOver()
                                        player_won_A_Loop2_p1 = True # Not really true, just to end the loop
                                        player_won_A_Loop2 = True # Not really true, just to end the loop
                                        player_won_A = True # Not really true, just to end the loop
                                        room7_complete = True
                                    # Checks if Hanks misses and sends player to loop where it is their turn against Hank
                                    else: 
                                        print("Hank tries to turn you into an orange and his spell doesn't work, so now it's your turn. You cast your spell towards Hank.")
                                        print()
                                        time.sleep(3)

                        # Checks if Hank misses Bob
                        else: # *
                            print("Hank tries to turn Bob into a flower vase, but his spell doesn't work, so now it's Bob's turn, and he casts his spell towards Hank.")
                            print()
                            time.sleep(3)
                            player_won_A_Loop2_p2 = False
                            while not player_won_A_Loop2_p2:
                                if (random.randint(0, 9)) <= 3:
                                    player_won_A_Loop2_p2 = True # Ends player_won_A_Loop2_p2 loop
                                    player_won_A_Loop2 = True # Sends player back to first if statement labeled *
                                else:
                                    player_won_A_Loop2_p2 = True 
