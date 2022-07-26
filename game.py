from user import User
from ai import Ai
import time
import os


class Game:
    def __init__(self):
        self.p1 = None
        self.p2 = None
        self.clear=lambda: os.system('cls')


    def player_select(self):
        user_choice = input("Enter 1 for single player or 2 for multi player: ")
        if user_choice == "1":
            time.sleep(1)
            self.p1 = User()
            self.p2 = Ai()
        elif user_choice == "2":
            time.sleep(1)
            print("Player 1: ")
            self.p1 = User()
            time.sleep(1)
            print("Player 2: ")
            self.p2 = User()

    def combat(self):
        while (self.p1.score < 2 and self.p2.score < 2):
            self.p1.set_gesture()
            self.clear()
            print(f"Current score:\n{self.p1.name}: {self.p1.score}\n {self.p2.name}: {self.p2.score}")
            time.sleep(1)
            self.p2.set_gesture()
            print(f"{self.p1.name} chooses {self.p1.attacks[int(self.p1.gesture)]['name']}")
            time.sleep(1)
            print(f"{self.p2.name} chooses {self.p2.attacks[int(self.p2.gesture)]['name']}")
            time.sleep(1)
            if (self.p1.gesture==self.p2.gesture):
                print("It's a tie!")
            elif (self.p1.gesture=="0"):
                self.rock()
            elif (self.p1.gesture=="1"):
                self.paper()
            elif (self.p1.gesture=="2"):
                self.scissor()
            elif (self.p1.gesture=="3"):
                self.lizard()
            elif (self.p1.gesture=="4"):
                self.spock()
            self.p1.clear_gesture()
            self.p2.clear_gesture()
            time.sleep(2)
            print(f"Current score:\n{self.p1.name}: {self.p1.score}\n {self.p2.name}: {self.p2.score}")
            input("Press any key to continue...")
        
        if (self.p1.score > self.p2.score):
            print(f"{self.p1.name} Wins!")
        else:
            print(f"{self.p2.name} wins!")

    def rock(self):
        if (self.p2.gesture=="1"):
            print("Rock is covered by paper")
            self.p2.score+=1
        elif (self.p2.gesture=="2"):
            print("Rock smashes scissors")
            self.p1.score+=1
        elif (self.p2.gesture=="3"):
            print("Rock crushes lizard")
            self.p1.score+=1
        elif (self.p2.gesture=="4"):
            print("Rock is vaporized!")
            self.p2.score+=1

    def paper(self):
        if (self.p2.gesture=="0"):
            print("Paper covers rock")
            self.p1.score+=1
        elif (self.p2.gesture=="2"):
            print("Paper is cut by scissors")
            self.p2.score+=1
        elif (self.p2.gesture=="3"):
            print("Paper is eaten by lizard")
            self.p2.score+=1
        elif (self.p2.gesture=="4"):
            print("Paper has disproven spock!")
            self.p1.score+=1

    def scissor(self):
        if (self.p2.gesture=="0"):
            print("Scissor are smashed by rock")
            self.p2.score+=1
        elif (self.p2.gesture=="1"):
            print("Scissor slices up paper")
            self.p1.score+=1
        elif (self.p2.gesture=="3"):
            print("scissor has decapitated lizard")
            self.p1.score+=1
        elif (self.p2.gesture=="4"):
            print("scissors was destroyed by spock")
            self.p2.score+=1

    def lizard(self):
        if (self.p2.gesture=="0"):
            print("lizard was crushed by rock")
            self.p2.score+=1
        elif (self.p2.gesture=="1"):
            print("lizard eats paper")
            self.p1.score+=1
        elif (self.p2.gesture=="2"):
            print("lizard is decapitated by scissors")
            self.p2.score+=1
        elif (self.p2.gesture=="4"):
            print("Lizard poisons spock")
            self.p1.score+=1

    def spock(self):
        if (self.p2.gesture=="0"):
            print("spock vaporizes rock")
            self.p1.score+=1
        elif (self.p2.gesture=="1"):
            print("spock has been disproven by paper")
            self.p2.score+=1
        elif (self.p2.gesture=="2"):
            print("spock has smashed scissors")
            self.p1.score+=1
        elif (self.p2.gesture=="3"):
            print("spock was poisoned by the lizard")
            self.p2.score+=1



    def run(self):
        self.player_select()
        time.sleep(1)
        self.combat()
    