from PySide6.QtGui import *
from PySide6.QtCore import *
import sys

from PySide6.QtWidgets import *


class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        date = self.get_data()
        rates = sorted(self.rates.keys())

        dateLabel = QLabel(date)

        self.fromComboBox = QComboBox()
        self.toComboBox = QComboBox()

        self.fromComboBox.addItems(rates)
        self.toComboBox.addItems(rates)

        self.fromSpinBox = QDoubleSpinBox()
        self.fromSpinBox.setRange(0.01, 1000)
        self.fromSpinBox.setValue(1.00)

        self.toLabel = QLabel("1.00")

        layout = QGridLayout()
        layout.addWidget(dateLabel, 0, 0)
        layout.addWidget(self.fromComboBox, 1, 0)
        layout.addWidget(self.toComboBox, 2, 0)
        layout.addWidget(self.fromSpinBox, 1, 1)
        layout.addWidget(self.toLabel, 2, 1)
        self.setLayout(layout)

        self.fromComboBox.currentIndexChanged.connect(self.update_ui)
        self.toComboBox.currentIndexChanged.connect(self.update_ui)
        self.fromSpinBox.valueChanged.connect(self.update_ui)

    def get_data(self):
        self.rates = {}

        try:
            date = "Unknown"

            # como el .csv no estaba disponible en 'http://www.bankofcanada.ca/en/markets/csv/exchange_eng.csv'
            # se procede a buscarla en 'https://web.archive.org/web/20080513231016/http://www.bankofcanada.ca/en/
            # markets/csv/exchange_eng.csv'
            # y a usar el paquete standar de python para tratar importar archivos .csv

            fh = open('exchange.csv')

            for line in fh:
                line = line.rstrip()
                if not line or line.startswith(("#", "Closing")):
                    continue

                fields = line.split(",")
                if line.startswith("Date "):
                    date = fields[-1]

                else:
                    try:
                        value = float(fields[-1])
                        self.rates[fields[0]] = value
                    except ValueError:
                        pass

            return "Exchange rates date: " + date
        except Exception as e:
            return "Failued to download:\n%s" % e

    def update_ui(self):
        from_ = self.fromComboBox.currentText()
        to = self.toComboBox.currentText()

        result = (self.rates[from_] / self.rates[to]) * self.fromSpinBox.value()

        self.toLabel.setText("%0.2f" % result)


app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()
