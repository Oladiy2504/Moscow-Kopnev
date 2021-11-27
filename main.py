import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


class Form(QWidget):
    def __init__(self):
        super().__init__()
        self.btn = QPushButton("->", self)
        self.side = False
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 93 * 3, 28)
        self.setWindowTitle('Circles')
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(93, 0)
        self.btn.clicked.connect(self.convert)

    def run(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Form()
    ex.show()
    sys.exit(app.exec())