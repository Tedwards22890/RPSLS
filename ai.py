from player import Player
import random
class Ai:
    def __init__(self):
        super().__init__()
        
    def gesture(self):
        choice =str(random.randrange(1,10))
        return choice