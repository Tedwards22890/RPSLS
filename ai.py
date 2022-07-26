from player import Player
import random
class Ai(Player):
    def __init__(self):
        super().__init__()
        self.ai_namer()
        
    def set_gesture(self):
        self.gesture =str(random.randrange(0,4))


    def ai_namer(self):
        names=["Sheldon","Penny","Leonard","Amy","Howard","Bernadette","Raj","Priya","Stuart","Barry","Missy"]
        self.name=random.choice(names)
