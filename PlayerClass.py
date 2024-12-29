# Imports
###############
import time
import random

# Creating & Defining Player Object
###############
class Player:

    # Init Method to define initial instances of the Player object - Name, Knowledge, Loyalty, Health, Abilities, Items
    def __init__(self, name, adjectives):
        self.name = name
        self.health = 100
        self.knowledge = 0
        self.loyalty = 0
        self.inventory = []
        self.abilities = []
        self.adjectives = adjectives
        self.balance = 0.0
        self.sidekick = [False, ""]
        self.positionOnMaze = 1
        self.mazeMoves = [1]
        self.weapon = ""
        self.skillPoints = 0

    # Player function to get their own stats
    def ME(self):
        print("Here are your stats:")
        print()
        time.sleep(1)

        print("Your name: " + self.name)
        print()
        time.sleep(1)

        print("Your health level: " + str(self.health))
        print()
        time.sleep(1)

        print("Your knowledge level: " + str(self.knowledge))
        print()
        time.sleep(1)

        print("Your loyalty points: " + str(self.loyalty))
        print()
        time.sleep(1)

        print("Your adjectives: ")
        print(self.adjectives)
        print()
        time.sleep(1)

        print("Your balance: " + str(self.balance))
        print()
        time.sleep(1)

        print("Your skill points: " + str(self.skillPoints))
        print()
        time.sleep(1)

        print("Your inventory: ")
        if self.inventory == []:
            print("Nothing in inventory yet")
        elif len(self.inventory) == 1:
            print("1", self.inventory[0])
        else:
            for item in range(0, len(self.inventory) - 1):
                print((item + 1), self.inventory[item])
        print()
        time.sleep(1)

        print("Your abilities: ")
        if self.abilities == []:
            print("No abilities yet")
        elif len(self.abilities) == 1:
            print("1", self.abilities[0])
        else:
            for item in range(0, len(self.abilities) - 1):
                print((item + 1), self.inventory[item])
        print()

        if self.sidekick[0] == True:
            print("Your sidekick: " + self.sidekick[1])
            print()

    # Other methods to change instances of Player object
    # Increases player's health
    def increaseHealth(self, amt): 
        self.health += amt
        print("Your health is now: " + str(self.health))
        print()

    # Increases player's loyalty points
    def moreLoyal(self, loyaltyIncrease):
        self.loyalty += loyaltyIncrease
        print("Your loyalty points are now: " + str(self.loyalty))
        print()
    
    # Adds item to player's inventory
    def pickUpItem(self, item):
        self.inventory.append(item)
        print("A " + item + " has been added to your inventory! This is now your inventory: ")
        for item in range(0, len(self.inventory)):
            print((item + 1), self.inventory[item])
        print()

    # Removes item from player's inventory
    def loseItem(self, item):
        self.inventory.remove(item)
        print("A " + item + " has been removed from your inventory! This is now your inventory: ")
        for item in range(0, len(self.inventory)):
            print((item + 1), self.inventory[item])
        print()

    # Adds a sidekick to player
    def getSidekick(self, sidekick):
        self.sidekick = [True, sidekick]
        print("You now have a sidekick! Their name is " + sidekick + ", and they will give you certain boosts in the final battle!")
        print()
        time.sleep(3)

    # Increases player's balance
    def addMoney(self, amt):
        self.balance += amt
        print("Your balance is now: " + str(self.balance))
        print()

    # Adds ability to player's abilities
    def gainAbility(self, ability):
        self.abilities.append(ability)
        print("You have gained an ability: " + ability + "! Here are all your abilities now: ")
        for single_ability in range(0, len(self.abilities)):
            print(self.abilities[single_ability])
        print()
    
    # Removes ability from player's abilities
    def forgetAbility(self):
        if len(self.abilities) > 0:
            num = random.randint(0, len(self.abilities) - 1)
            ability = self.abilities[num]
            self.abilities.pop(num)
            print("You have forgotten an ability: " + ability + ". Here are all your abilities now: ")
            for single_ability in range(0, len(self.abilities)):
                print(self.abilities[single_ability])
            print()
        else:
            print()

    # Increases player's knowledge
    def increaseKnowledge(self, amt):
        self.knowledge += amt
        print("Your knowledge level is now: " + str(self.knowledge))
        print()

    # Changes player's position and checkpoints passed on maze
    # Only on player object as it relates to player and is used frequently when checking where player is or where they want to go
    def changeMazeMoves(self, newPos):
        self.mazeMoves.append(newPos)
        print("Here are the checkpoints you have visited so far: ")
        print(self.mazeMoves)
        print()
        time.sleep(3)
        self.positionOnMaze = newPos

    # Sets player's current weapon
    def setWeapon(self, item_weapon):
        self.weapon = item_weapon
        print("You decide to choose the " + self.weapon + " to fight the minion with.")
        print()
        time.sleep(3)

    # Increases player's skill points
    def getSkilled(self, skillAmt):
        self.skillPoints += skillAmt
        print("You now have: " + str(self.skillPoints) + " skill points!")
        print()

    # Ends game for player
    def gameOver(self):
        print("GAME OVER")
        print("---------")
        print()
        print("Thank you for playing this adventure game made by Vedant Kansara - AP CSP Adventure Game 2022 - 2023")