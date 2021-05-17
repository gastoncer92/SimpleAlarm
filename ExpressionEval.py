from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import sys

import math


class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        self.resultList = QTextBrowser()
        self.resultInput = QLineEdit("Enter an expression and press return key")

        layout = QVBoxLayout()
        layout.addWidget(self.resultList)
        layout.addWidget(self.resultInput)
        self.setLayout(layout)

        self.resultInput.selectAll()
        self.resultInput.setFocus()

        self.resultInput.returnPressed.connect(self.compute)

    def compute(self):
        try:
            text = self.resultInput.text()
            self.resultList.append("{0} = <b>{1}</b>".format(text, eval(text)))

        except:
            self.resultList.append("<font color=red><b>Expression invalid</b></font>")


            #####################################################
            #                                                   #
            #                                                   #
            #                                                   #
            #####################################################


app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()
