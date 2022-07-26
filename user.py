from player import Player
class User(Player):
    def __init__(self):
        super().__init__()

    def gesture(self):
        for x in range(len(self.attacks)):
            print(f"{self.attacks('number','name')}:\n")
        #choice=input("1) Rock\n2) Paper\n3) Scissors\n4) Lizard\n5) Spock\nChoose your gesture: ")
        choice=input("Choose your gesture: ")
        return choice
