from Snapshot import Snapshot

# Originator
class Editor:

    def __init__(self):
        self.text = ""

    def setText(self, text):
        self.text = text

    def createSnapshot(self):
        return Snapshot(self, self.text)

    def appendLine(self, line):
        self.text += line + '\n'

    def printText(self):
        print(self.text)



