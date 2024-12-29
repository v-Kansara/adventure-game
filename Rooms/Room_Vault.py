# Imports
###############
import time

# Run vault function with player object
###############
def vault(player, methodToWin):
    print("VAULT")
    print("-----")
    print()

    # Checks how player made it to vault
    if methodToWin == "lock-pick":
        print("Welcome, user, to the Secret Vault! You have made it! Due to your cunning abilities and wits, you strategically went through the game and beat it! Now just imagine all the riches in the world, right at your fingertips! Congratulations for making it this far and I wish you luck on your next adventure!")
        print()
        
    elif methodToWin == "wizard":
        print("Welcome, user, to the Secret Vault! You have made it! Due to your bravery and courage, you defeated the wizard and beat the game! Now just imagine all the riches in the world, right at your fingertips! Congratulations for making it this far and I wish you luck on your next adventure!")
    
    time.sleep(3)
    player.addMoney(1000000) # addMoney Method on player object increases player's balance by input amt
    time.sleep(3)
    player.moreLoyal(50) # moreLoyal Method on player object increases player's loyalty points by input amt
    time.sleep(3)
    player.increaseKnowledge(100) # increaseKnowledge Method on player object increases player's knowledge by input amt
    time.sleep(3)
    player.getSkilled(50) # getSkilled Method on player object increases player's skill points by input amt
    time.sleep(3)
    print("Here are the stats you ended the game off with:")
    print("----------------")
    print()
    player.ME() # ME Method on player object shows player their stats
    print("Once again, congratulations player! I hope to see you soon!")
    print()

    player.gameOver() # gameOver instance ends game for player and prevents game from repeating
    time.sleep(3)
