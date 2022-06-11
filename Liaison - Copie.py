import sys

from PySide2.QtWidgets import QApplication, QtWidgets
from menu import MenuBarDemo
from Fenetre_1 import Ui_Dialog

def affichFen1():
    Fen1.show()

app = QApplication(sys.argv)
demo = MenuBarDemo()

Fen1 = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Fen1)

demo.show()

ui.nouveau.clicked.connected(affichFen1)
sys.exit(app.exec_())
