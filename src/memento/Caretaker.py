
class Caretaker:

    def __init__(self, editor):
        self.memorized_states = []
        self.editor = editor

    def makeBackup(self):
        print("Creating Snapshot")
        snapshot = self.editor.createSnapshot()
        self.memorized_states.append(snapshot)

    def rollback(self):
        print("Restore Snapshot")
        if len(self.memorized_states) > 0:
            self.memorized_states[-1].restore()
        else:
            print("No saved snapshots")
