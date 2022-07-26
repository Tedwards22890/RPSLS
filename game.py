from user import user


class Game:
    def __init__(self):
        self.player_one = None
        self.player_two = None


    def player_select(self):
        user_choice = input("Enter 1 for single player or 2 for multi player")
        if user_choice == "1":
            self.player_one = User().gesture
            self.player_two = Ai().gesture
        elif user_choice == "2":
            self.player_one = User()
            self.player_two = User()
    def run(self):
        pass
    