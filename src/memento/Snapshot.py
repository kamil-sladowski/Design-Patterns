
class Snapshot:

    def __init__(self, player, position):
        self.player = player
        self.x = position[0]
        self.y = position[1]

    def restore(self):
        self.player.setPosition([self.x, self.y])