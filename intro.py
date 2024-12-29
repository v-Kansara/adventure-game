# Imports
###############
import time
from Rooms.Room_1 import room1

# Intro Function of Adventure Game -> Will run opening remarks, greet user and describe goal of adventure game
###############
def intro(player):
    print()
    print("Hello there, " + player.name + ", a great adventure waits for you!")
    time.sleep(1)
    print("In this epic saga, you will have to explore, fight, think and so much more to make it to the secret vault located at the end of this quest! You will have to make decisions, some that could help you, others ... not so much. At each decision point in your journey, you will be told various things you can do, and at any point when you have to make a decision, if you type: HELP, then some hints will be provided for you to continue onwards. You will only be provided hints when you have to make a decision, NOT if you are solving a riddle or fighting someone. Your goal is to make it to the vault alive, as some unfortunate decisions could end you up with a GAME OVER screen. At the beginning of any room (shown by the line of hyphens), if you type: ME, then your stats will show up, such as your current health, abilities, items, etc. I don't wish to take any more of your time, so best of luck! Your journey awaits!")
    time.sleep(20)
    print()
    print("GAME STARTED")
    print("------------")
    print()

    room1(player) # Send player to room 1 function