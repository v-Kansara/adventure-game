# Imports
###############
import time
from Rooms.Room_Vault import vault
from mazeLocations import *

# Run maze function with player object
###############
def maze(player):
    print("MAZE")
    print("-----")
    print()
    print("You find yourself in a maze, surrounded by shrubs and trees. An old and frailing map helps guide you, though there is a catch with the maze. If you act too greedily, then you might not get the reward you want. You start at the entrance of the maze, but you see an opening at the other side of the maze, which could possibly be the end. You shrug your shoulders and walk confidently towards the maze. ")
    print("Note: You can only go in these directions - Forward (↑), Downward (↓), Leftwards (←) or Rightwards (→) - (E.g. If you are at point 1, you can not go forward, but you can go left, even though it looks like forwards is the right path). Please type a number for the direction (1, 2, 3 or 4) as your response to each question, DON'T type the direction or next checkpoint number.")
    print()
    time.sleep(15)
    maze_complete = False
    while not maze_complete:

        # Checks where player is in the maze by the positionOnMaze instance
        if player.positionOnMaze == 1:
            # Loops over and print multiple text strings of ASCII Art to represent the maze
            for i in range(0, len(maze_location_1)):
                print(maze_location_1[i])
            print()
            time.sleep(1)
            print("You are at checkpoint 1 in the maze. You can only go left (←) to checkpoint 2.")
            # Asks player where they want to go
            move = input("Press 1 to go forward, 2 to go downwards, 3 to go leftwards or 4 to go rightwards: ")
            if move == "3":
                print("You go left to checkpoint 2.")
                print()
                # changeMazeMoves Method on player object adds next position to list of checkpoints player has already went to and moves the player to the indicated position
                player.changeMazeMoves(2)
            else: # Prevents player from going anywhere else besides specified options
                print("That is not a valid choice. Please choose again.")
                print()
                time.sleep(3)

        elif player.positionOnMaze == 2:
            for i in range(0, len(maze_location_2)):
                print(maze_location_2[i])
            print()
            time.sleep(1)
            print("You are at checkpoint 2 in the maze. You can either go left (←) to checkpoint 3, forward (↑) to checkpoint 4 or right (→) to checkpoint 1.")
            move = input("Press 1 to go forward, 2 to go downwards, 3 to go leftwards or 4 to go rightwards: ")
            if move == "1":
                print("You go forward to checkpoint 4.")
                print()
                player.changeMazeMoves(4)
            elif move == "3":
                print("You go left to checkpoint 3.")
                print()
                player.changeMazeMoves(3)
            elif move == "4":
                print("You go right to checkpoint 1.")
                print()
                player.changeMazeMoves(1)
            else: 
                print("That is not a valid choice. Please choose again.")
                print()
                time.sleep(3)

        elif player.positionOnMaze == 3:
            for i in range(0, len(maze_location_3)):
                print(maze_location_3[i])
            print()
            time.sleep(1)
            print("You are at checkpoint 3 in the maze. You can either go right (→) to checkpoint 2 or go forwards (↑) to checkpoint 9.")
            move = input("Press 1 to go forward, 2 to go downwards, 3 to go leftwards or 4 to go rightwards: ")
            if move == "1":
                print("You go forward to checkpoint 9.")
                print()
                player.changeMazeMoves(9)
            elif move == "4":
                print("You go right to checkpoint 2.")
                print()
                player.changeMazeMoves(2)
            else: 
                print("That is not a valid choice. Please choose again.")
                print()
                time.sleep(3)

        elif player.positionOnMaze == 4:
            for i in range(0, len(maze_location_4)):
                print(maze_location_4[i])
            print()
            time.sleep(1)
            print("You are at checkpoint 4 in the maze. You can either go right (→) to checkpoint 5, forward (↑) to checkpoint 7 or downward (↓) to checkpoint 2.")
            move = input("Press 1 to go forward, 2 to go downward, 3 to go leftwards or 4 to go rightwards: ")
            if move == "1":
                print("You go forward to checkpoint 7.")
                print()
                player.changeMazeMoves(7)
            elif move == "2":
                print("You go downward to checkpoint 2.")
                print()
                player.changeMazeMoves(2)
            elif move == "4":
                print("You go right to checkpoint 5.")
                print()
                player.changeMazeMoves(5)
            else: 
                print("That is not a valid choice. Please choose again.")
                print()
                time.sleep(3)

        elif player.positionOnMaze == 5:
            for i in range(0, len(maze_location_5)):
                print(maze_location_5[i])
            print()
            time.sleep(1)
            print("You are at checkpoint 5 in the maze. You can either go left (←) to checkpoint 4 or forwards (↑) to checkpoint 6.")
            move = input("Press 1 to go forward, 2 to go downward, 3 to go leftwards or 4 to go rightwards: ")
            if move == "1":
                print("You go forward to checkpoint 6.")
                print()
                player.changeMazeMoves(6)
            elif move == "3":
                print("You go left to checkpoint 4.")
                print()
                player.changeMazeMoves(4)
            else: 
                print("That is not a valid choice. Please choose again.")
                print()
                time.sleep(3)

        elif player.positionOnMaze == 6:
            for i in range(0, len(maze_location_6)):
                print(maze_location_6[i])
            print()
            time.sleep(1)
            print("You are at checkpoint 6 in the maze. You can either go left (←) to checkpoint 7 or downwards (↓) to checkpoint 5.")
            move = input("Press 1 to go forward, 2 to go downward, 3 to go leftwards or 4 to go rightwards: ")
            if move == "2":
                print("You go downwards to checkpoint 5.")
                print()
                player.changeMazeMoves(5)
            elif move == "3":
                print("You go left to checkpoint 7.")
                print()
                player.changeMazeMoves(7)
            else: 
                print("That is not a valid choice. Please choose again.")
                print()
                time.sleep(3)

        elif player.positionOnMaze == 7:
            for i in range(0, len(maze_location_7)):
                print(maze_location_7[i])
            print()
            time.sleep(1)
            print("You are at checkpoint 7 in the maze. You can either go left (←) to checkpoint 8, downwards (↓) to checkpoint 4 or right (→) to checkpoint 6.")
            move = input("Press 1 to go forward, 2 to go downward, 3 to go leftwards or 4 to go rightwards: ")
            if move == "2":
                print("You go downwards to checkpoint 4.")
                print()
                player.changeMazeMoves(4)
            elif move == "3":
                print("You go left to checkpoint 8.")
                print()
                player.changeMazeMoves(8)
            elif move == "4":
                print("You go right to checkpoint 6.")
                print()
                player.changeMazeMoves(6)
            else: 
                print("That is not a valid choice. Please choose again.")
                print()
                time.sleep(3)

        elif player.positionOnMaze == 8:
            for i in range(0, len(maze_location_8)):
                print(maze_location_8[i])
            print()
            time.sleep(1)
            print("You are at checkpoint 8 in the maze. You can either go left (←), downwards (↓) to checkpoint 9 or right (→) to checkpoint 7.")
            move = input("Press 1 to go forward, 2 to go downward, 3 to go leftwards or 4 to go rightwards: ")
            if move == "2":
                print("You go downwards to checkpoint 9.")
                print()
                player.changeMazeMoves(9)
            elif move == "3":
                print("You go left to a dead end, where you are teleported to the bottomless pit of despair.")
                print()
                player.gameOver() # gameOver Method ends game for player and prevents game from repeating
                maze_complete = True # Ends maze loop
            elif move == "4":
                print("You go right to checkpoint 7.")
                print()
                player.changeMazeMoves(7)
            else: 
                print("That is not a valid choice. Please choose again.")
                print()
                time.sleep(3)

        elif player.positionOnMaze == 9:
            for i in range(0, len(maze_location_9)):
                print(maze_location_9[i])
            print()
            time.sleep(1)
            print("You are at checkpoint 9 in the maze. You can either go left (←) to checkpoint 10, downwards (↓) to checkpoint 3 or forwards (↑) to checkpoint 8.")
            move = input("Press 1 to go forward, 2 to go downward, 3 to go leftwards or 4 to go rightwards: ")
            if move == "1":
                print("You go forwards to checkpoint 8.")
                print()
                player.changeMazeMoves(8)
            elif move == "2":
                print("You go downwards to checkpoint 3.")
                print()
                player.changeMazeMoves(3)
            elif move == "3":
                print("You go left to checkpoint 10.")
                print()
                player.changeMazeMoves(10)
            else: 
                print("That is not a valid choice. Please choose again.")
                print()
                time.sleep(3)

        elif player.positionOnMaze == 10:
            for i in range(0, len(maze_location_10)):
                print(maze_location_10[i])
            print()
            time.sleep(1)
            print("Congratulations! You made it to checkpoint 10 in the maze.")
            # Checks list of player's maze positions to see if they took the shortest path
            if player.mazeMoves == [1, 2, 3, 9, 10]:
                print("Since you decided to be greedy and take the shortest path, you will only be rewarded with the imagination of a small bag of treasures. Too bad, so sad. Better luck next time!")
                print()
                time.sleep(3)
                player.gameOver()
                maze_complete = True
            else:
                print("Your quick thinking and resourcefulness allowed you to efficiently go through the maze! You are awared a giant lock pick that will open the secret vault, containing all the treasures that you desire!")
                print()
                time.sleep(3)
                maze_complete = True
                vault(player, "lock-pick")  # Sends player to vault with a 'lock-pick' as their MethodToWin   
