#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtCore, QtGui,QtWidgets
from PyQt5.QtWidgets import  QMainWindow, QWidget, QApplication
from gui import Ui_main
from busqueda import buscar


class Main(QMainWindow):
	def __init__(self, parent=None):
                self._translate = QtCore.QCoreApplication.translate
		QWidget.__init__(self, parent)
		self.ui = Ui_main()
		self.ui.setupUi(self)
                self.ui.btn_buscar.clicked.connect(self.buscar)
		
        def buscar(self):
            query = self.ui.txt_buscar.text()
            lista_videos =  buscar(query)
            i = 0
            for video in lista_videos:
                #print 'https://www.youtube.com' + video['href']+"title "+video['title']
                item_0 = QtWidgets.QTreeWidgetItem(self.ui.tabla_resultados)
                self.ui.tabla_resultados.topLevelItem(i).setText(0, self._translate("main", "%s"%(i+1)))
                self.ui.tabla_resultados.topLevelItem(i).setText(1, self._translate("main", video['title']))
                i  = i+1 


        def salir(self):
	    print "saliendo del programa"
	    sys.exit()

            

if __name__ == "__main__":
	app = QApplication(sys.argv)
	myapp = Main()
	myapp.show()
	sys.exit(app.exec_())

