from Snapshot import Snapshot
from consts import RADIUS_STEP, X_MAX, Y_MAX

# Originator
class Player:

    def __init__(self):
        self.position = [5 * RADIUS_STEP, 2 * RADIUS_STEP]

    def setPosition(self, position):
        print(f"Restored position {position[0]}: {position[1]}")
        self.position[0] = position[0]
        self.position[1] = position[1]

    def createSnapshot(self):
        return Snapshot(self, self.position)

    def move(self, position):
        if 0 < self.position[0] + position[0] < X_MAX:
            self.position[0] += position[0] * RADIUS_STEP
        if 0 < self.position[1] + position[1] < Y_MAX:
            self.position[1] += position[1] * RADIUS_STEP

    def getPosition(self):
        return self.position



