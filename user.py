from player import Player
class User(Player):
    def __init__(self):
        super().__init__()
        #self.namer()


    def set_gesture(self):
        for x in range(len(self.attacks)):
            print(f"{self.attacks[x]['number']}) {self.attacks[x]['name']}")
        #self.gesture=input("0) Rock\n1) Paper\n2) Scissors\n3) Lizard\n4) Spock\nChoose your gesture: ")


    
    def namer(self):
        self.name=input("What is your name: ")
        print(f"Welcome {self.name}")
