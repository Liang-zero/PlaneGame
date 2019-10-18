class Gameqingkuang:
    def __init__(self,gameSet):
        self.gameSet=gameSet
        self.game_active=False
        self.plane_left =self.gameSet.heartCount
        self.score=0
        self.final_score=0
        self.level=0