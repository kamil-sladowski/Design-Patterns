from Editor import Editor
from Caretaker import Caretaker

if __name__ == '__main__':
    text_sequence = ["aaaaaaaa", "bbbbbbbb", "ccccccc", "ddddddd", "eeeeeee"]
    e = Editor()
    e.appendLine(text_sequence[0])
    e.appendLine(text_sequence[1])
    e.appendLine(text_sequence[1])
    e.appendLine(text_sequence[2])
    e.printText()
    c = Caretaker(e)
    c.makeBackup()
    e.appendLine(text_sequence[3])
    e.appendLine(text_sequence[3])
    e.printText()
    c.rollback()
    e.printText()
