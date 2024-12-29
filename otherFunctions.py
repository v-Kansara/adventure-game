# Imports
###############
import time

# HELP Function that can be accessed from any room EXCEPT for 4, 7 & Maze, because the player shouldn't be able to receive it there (4 has a riddle which the player must solve by themselves, 7 is a simulated room - Player doesn't do anything and the maze has clear inputs and describes everything, so player shouldn't need it anyway)
###############
def HELP(room, question):
    # Separate out help requests by room, then by question for each room
    # Room 1
    if room == "1":
        if question == 1:
            hint = "The question is asking what you would like to do. Here, you can either 'Go to the Basement', 'Talk to the group of people', 'Pick up the junk on the floor', 'Pick up the loose paper on the floor' or 'Go to the door to Room 2'. As long as your response contains the keywords in prior text, the game will be able to recognize what you want to do."
            return hint

        elif question == 2:
            hint = "The question is asking what you would like to do. Here, you can either 'Go to the door to Room 2' or 'Talk to the group of people'. As long as your response contains the keywords in prior text, the game will be able to recognize what you want to do."
            return hint
    
    # Room 2
    elif room == "2":
        if question == 1:
            hint = "The question is asking what you would like to do. Here, you can either 'Move forward' or 'Turn on the light bulb'. As long as your response contains the keywords in prior text, the game will be able to recognize what you want to do."
            return hint

        elif question == 2:
            hint = "The question is asking what you would like to do. Here, you can either 'Look at the painting', 'Go to the tunnel to the lab' or 'Walk forward'. As long as your response contains the keywords in prior text, the game will be able to recognize what you want to do."
            return hint

        elif question == 3:
            hint = "The question is asking what you would like to do. Here, you can either 'Inspect the lightbulb' or 'Look at the riddle on the board to your right'. As long as your response contains the keywords in prior text, the game will be able to recognize what you want to do."
            return hint

    # Room 3
    elif room == "3":
        if question == 1:
            hint = "The question is asking what you would like to do. Here, you can either 'Give 30 health for a shield', 'Give $10 to be able to slow down time' or 'Give the lucky coin for 50 shield'. As long as your response contains the keywords in prior text, the game will be able to recognize what you want to do."
            return hint

    # Room 5
    elif room == "5":
        if question == 1:
            hint = "The question is asking what you would like to do. Here, you can either 'Go to the forge in the middle of the room' or 'Go to the board to learn a skill'. As long as your response contains the keywords in prior text, the game will be able to recognize what you want to do."
            return hint

        elif question == 2:
            hint = "The question is asking what you would like to do. Here, you can either 'Give the lucky coin for a giant-axe', 'Give the sword for the giant-axe', 'Give 50 health points for the giant-axe' or 'Decline the chance & leave'. As long as your response contains the keywords in prior text, the game will be able to recognize what you want to do."
            return hint

        elif question == 3:
            hint = "The question is asking what you would like to do. Here, you can either 'Learn how to jump higher', 'Learn how to run faster' or 'Learn how to fly'. As long as your response contains the keywords in prior text, the game will be able to recognize what you want to do."
            return hint

    # Room 6
    elif room == "6":
        if question == 1:
            hint = "The question is asking what you would like to do. Here, you can either 'Go to the table with chemicals' or 'Go to the trapdoor'. As long as your response contains the keywords in prior text, the game will be able to recognize what you want to do."
            return hint

    # Room 8
    elif room == "8":
        if question == 1:
            hint = "The question is asking what you would like to do. Here, you can either 'Run away from the minion', 'Fight the minion' or 'Look around for something else to do'. As long as your response contains the keywords in prior text, the game will be able to recognize what you want to do."
            return hint

        elif question == 2:
            hint = "The question is asking what you would like to do. Here, you can either 'Slash the minion' or 'Swing at the minion'. As long as your response contains the keywords in prior text, the game will be able to recognize what you want to do."
            return hint

        elif question == 3:
            hint = "The question is asking what you would like to do. Here, you can either 'Stay on the side of the castle' or 'Jump onto the dragon'. As long as your response contains the keywords in prior text, the game will be able to recognize what you want to do."
            return hint

    # Room 9
    elif room == "9":
        if question == 1:
            hint = "The question is asking what you would like to do. Here, you can either type 'Continue', which will start the final battle and tests, or type 'ME', which will display your stats."
            return hint

    # Basement
    elif room == "basement":
        if question == 1:
            hint = "The question is asking what you would like to do. Here, you can either 'Run away from the man' or 'Wait for the man to reach you'. As long as your response contains the keywords in prior text, the game will be able to recognize what you want to do."
            return hint

        elif question == 2:
            hint = "The question is asking what you would like to do. Here, you can either 'Go to the unnamed door' or 'Fight the hooded figure'. As long as your response contains the keywords in prior text, the game will be able to recognize what you want to do."
            return hint

        elif question == 3:
            hint = "The question is asking what you would like to do. Here, you can either 'Pay the man $10' or 'Refuse to give him money'. As long as your response contains the keywords in prior text, the game will be able to recognize what you want to do."
            return hint