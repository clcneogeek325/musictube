#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import  QMainWindow, QWidget, QApplication
from gui import Ui_main

class Main(QMainWindow):
	def __init__(self, parent=None):
		QWidget.__init__(self, parent)
		self.ui = Ui_main()
		self.ui.setupUi(self)
		

if __name__ == "__main__":
	app = QApplication(sys.argv)
	myapp = Main()
	myapp.show()
	sys.exit(app.exec_())

