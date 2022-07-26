from user import User
from ai import Ai


class Game:
    def __init__(self):
        self.p1 = None
        self.p2 = None


    def player_select(self):
        user_choice = input("Enter 1 for single player or 2 for multi player")
        if user_choice == "1":
            self.p1 = User()
            self.p2 = Ai()
        elif user_choice == "2":
            self.p1 = User()
            print("Plyer 2:")
            self.p2 = User()

    def combat(self):
        while (self.p1.score <2 and self.p2.score<2):
            print(f"Current score:\n{self.p1.name}: {self.p1.score}")
            print(f"{self.p2.name}: {self.p2.score}")
            self.p1.set_gesture()
            self.p2.set_gesture()
            print(f"{")
            if (self.p1.gesture==self.p2.gesture):



    def run(self):
        self.player_select()
    