#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import  QMainWindow, QWidget, QApplication
from gui import Ui_main
from busqueda import buscar


class Main(QMainWindow):
	def __init__(self, parent=None):
		QWidget.__init__(self, parent)
		self.ui = Ui_main()
		self.ui.setupUi(self)
                self.ui.btn_buscar.clicked.connect(self.buscar)
		
        def buscar(self):
            query = self.ui.txt_buscar.text()
            lista_videos =  buscar(query)
            for video in lista_videos:
                print 'https://www.youtube.com' + video['href']+"title "+video['title']



        def salir(self):
	    print "saliendo del programa"
	    sys.exit()

            

if __name__ == "__main__":
	app = QApplication(sys.argv)
	myapp = Main()
	myapp.show()
	sys.exit(app.exec_())

