
class Snapshot:

    def __init__(self, editor, text):
        self.editor = editor
        self.text = text

    def restore(self):
        self.editor.setText(self.text)