from player import Player
class User(Player):
    def __init__(self):
        super().__init__()
        self.namer()


    def set_gesture(self):
        while (self.gesture!="0" and self.gesture!="1" and self.gesture!="2" and self.gesture!="3" and self.gesture!="4"):
            for x in range(len(self.attacks)):
                print(f"{self.attacks[x]['number']}) {self.attacks[x]['name']}")
            self.gesture=input("Your selection: ")

    
    def namer(self):
        self.name=input("What is your name: ")
        print(f"Welcome {self.name}")


