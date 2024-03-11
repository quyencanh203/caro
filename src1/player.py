from entity import * 

class Player(Entity):
    def __init__(self, text) -> None:
        super().__init__(text)

    def player_move(self):
        return 'X'

    

        
