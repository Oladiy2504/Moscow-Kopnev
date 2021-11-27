import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QApplication


class Form(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.screen = ''
        self.data = ''
        for i in self.buttonGroup_digits.buttons():
            i.clicked.connect(self.run)
        self.btn_clear.clicked.connect(self.clear)
        for i in self.buttonGroup_binary.buttons():
            i.clicked.connect(self.operation)
        self.btn_eq.clicked.connect(self.result)

    def clear(self):
        self.screen = ''
        self.data = ''
        self.table.display(0)

    def run(self):
        if self.data and self.data[-1].isdigit():
            self.screen += self.sender().text()
        else:
            self.screen = self.sender().text()
        self.data += self.sender().text()
        print(self.data)
        self.table.display(int(self.screen))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    sys.exit(app.exec())