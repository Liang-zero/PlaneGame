class Setting:
    def __init__(self):
        self.width=800
        self.height=1200
        self.color=(255,255,255)
        self.bulletSpeed=5
        self.planeSpeed=5
        self.enemyrlSpeed=1
        self.enemydownSpeed=5
        self.bulletCapacity=5
        self.enemyDirection=1
        self.heartCount=2
        self.speedup=5
    def chushi(self):
        self.planeSpeed = 5
        self.bulletSpeed = 5
        self.enemydownSpeed = 5
        self.enemyrlSpeed = 1

    def increase_speed(self):
        self.planeSpeed=10
        self.bulletSpeed+=5
        self.enemydownSpeed+=5
        self.enemyrlSpeed+=1

