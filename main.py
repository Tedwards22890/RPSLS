import time
from game import Game

print("Welcome to Rock, Paper, Scissors, Lizard, Spock (RPSLS!)")
print("The game will be played based on best out of three.\nThe rules are as follows:")
time.sleep(1)
print("Scissors cuts Paper")
time.sleep(1)
print("Paper covers Rock")
time.sleep(1)
print("Rock crushes Lizard")
time.sleep(1)
print("Lizard poisons Spock")
time.sleep(1)
print("Spock smashes Scissors")
time.sleep(1)
print("Scissors decapitates Lizard")
time.sleep(1)
print("Lizard eats Paper")
time.sleep(1)
print("Paper disproves Spock")
time.sleep(1)
print("Spock vaporizes Rock")
time.sleep(1)
print("(and as it always has) Rock crushes Scissors")
game=Game()
keep_playing=True
while (keep_playing==True):
    game.run()
    choice=input("Play again? (y) or any other key to exit: ")
    if (choice=="y" or choice=="Y"):
        keep_playing=True
    else:
        keep_playing=False
time.sleep(1)
print("Thanks for playing RPSLS!")
time.sleep(1)
print("Created/designed/programmed by Travis Edwards")
time.sleep(1)
print("Special thanks to Kyra Marie for help with play testing!")