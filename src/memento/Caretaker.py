
class Caretaker:

    def __init__(self, player):
        self.memorized_states = []
        self.player = player

    def makeBackup(self):
        snapshot = self.player.createSnapshot()
        self.memorized_states.append(snapshot)
        print("Created Snapshot")

    def rollback(self):
        print("Restore Snapshot")
        if len(self.memorized_states) > 0:
            self.memorized_states.pop().restore()
        else:
            print("No saved snapshots")
