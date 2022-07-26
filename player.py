class Player:

    def __init__(self):
        self.score = 0
        self.name=None
        self.gesture=None
        self.attacks = [
            {'number':'0','name':'Rock'},
            {'number':'1','name':'Paper'},
            {'number':'2','name':'Scizzors'},
            {'number':'3','name':'Lizard'},
            {'number':'4','name':'Spock'}
        ]

    def clear_gesture(self):
        self.gesture=None
    

    

