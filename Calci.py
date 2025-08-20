import sys
import math
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit
from PyQt5.QtCore import Qt

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Modern Calculator")
        self.setFixedSize(400, 500)
        self.initUI()

    def initUI(self):
        # Main Layout
        vbox = QVBoxLayout()
        self.setLayout(vbox)

        # Display
        self.display = QLineEdit()
        self.display.setAlignment(Qt.AlignRight)
        self.display.setFixedHeight(60)
        self.display.setStyleSheet("font-size: 24px; padding: 10px; background: #222; color: white; border-radius: 10px;")
        vbox.addWidget(self.display)

        # Buttons Grid
        grid = QGridLayout()
        vbox.addLayout(grid)

        buttons = [
            ('C', 0, 0), ('⌫', 0, 1), ('%', 0, 2), ('/', 0, 3),
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('*', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('+', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('x²', 4, 2), ('=', 4, 3),
            ('√', 5, 0), ('1/x', 5, 1)
        ]

        for btn_text, row, col in buttons:
            button = QPushButton(btn_text)
            button.setFixedSize(80, 60)
            button.setStyleSheet("""
                QPushButton {
                    background-color: #333;
                    color: white;
                    font-size: 18px;
                    border-radius: 10px;
                }
                QPushButton:hover {
                    background-color: #555;
                }
                QPushButton:pressed {
                    background-color: #777;
                }
            """)

            if btn_text == "=":
                button.setStyleSheet("""
                    QPushButton {
                        background-color: #FF9500;
                        color: white;
                        font-size: 20px;
                        border-radius: 10px;
                    }
                    QPushButton:hover { background-color: #FFB84D; }
                    QPushButton:pressed { background-color: #E67E00; }
                """)
                button.clicked.connect(self.evaluate)

            elif btn_text == "C":
                button.clicked.connect(self.clear)

            elif btn_text == "⌫":
                button.clicked.connect(self.backspace)

            elif btn_text == "x²":
                button.clicked.connect(self.square)

            elif btn_text == "√":
                button.clicked.connect(self.sqrt)

            elif btn_text == "1/x":
                button.clicked.connect(self.reciprocal)

            elif btn_text == "%":
                button.clicked.connect(self.percent)

            else:
                button.clicked.connect(lambda checked, text=btn_text: self.add_to_display(text))

            grid.addWidget(button, row, col)

    def add_to_display(self, text):
        self.display.setText(self.display.text() + text)

    def clear(self):
        self.display.clear()

    def backspace(self):
        self.display.setText(self.display.text()[:-1])

    def square(self):
        try:
            value = float(self.display.text())
            self.display.setText(str(value ** 2))
        except:
            self.display.setText("Error")

    def sqrt(self):
        try:
            value = float(self.display.text())
            if value >= 0:
                self.display.setText(str(math.sqrt(value)))
            else:
                self.display.setText("Error")
        except:
            self.display.setText("Error")

    def reciprocal(self):
        try:
            value = float(self.display.text())
            if value != 0:
                self.display.setText(str(1 / value))
            else:
                self.display.setText("Error")
        except:
            self.display.setText("Error")

    def percent(self):
        try:
            value = float(self.display.text())
            self.display.setText(str(value / 100))
        except:
            self.display.setText("Error")

    def evaluate(self):
        try:
            result = str(eval(self.display.text()))
            self.display.setText(result)
        except:
            self.display.setText("Error")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec_())
