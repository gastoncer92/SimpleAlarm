#!/usr/bin/env python3
from PySide6.QtCore import QTime, QTimer
from PySide6.QtGui import Qt

from PySide6.QtWidgets import QApplication, QLabel

import sys
import time

app = QApplication(sys.argv)

due = QTime.currentTime()
message = 'Alert!'

try:
    if len(sys.argv) < 2:
        raise ValueError
    hours, minutes = sys.argv[1].split(":")

    due = QTime(int(hours), int(minutes))

    if not due.isNull():
        raise ValueError
    if len(sys.argv) > 2:
        message = ' '.join(sys.argv[2:])

except:
    print('Usage: python SimpleApp.py HH:MM Optional Message')
while QTime.currentTime() < due:
    time.sleep(5)

label = QLabel("<font color=red size=72>" + message + "</font>")
label.setWindowFlag(Qt.SplashScreen)
label.show()

QTimer.singleShot(2000, app.quit)
app.exec_()