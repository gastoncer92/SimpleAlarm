# from PySide6.QtGui import *
# from PySide6.QtCore import *
import sys
from PySide6.QtWidgets import *


class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        self.dial = QDial()
        self.dial.setNotchesVisible(True)

        self.spinbox = QSpinBox()

        layout = QVBoxLayout()
        layout.addWidget(self.dial)
        layout.addWidget(self.spinbox)

        # set de los máximos disponibles
        self.dial.setMaximum(150)
        self.spinbox.setMaximum(150)

        self.setLayout(layout)

        # se busca conectar ambos objetos mediante señales
        self.dial.valueChanged.connect(self.spinbox.setValue)
        self.spinbox.valueChanged.connect(self.dial.setValue)

        self.dial.valueChanged.connect(self.print_value)

    def print_value(self, value):
        print("El valor es {0}".format(value))


app = QApplication(sys.argv)
form = Form()
form.show()
app.exec()
