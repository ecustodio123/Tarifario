# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tarifario.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QLabel, QRadioButton, QPushButton, QVBoxLayout, QApplication, QWidget, QSpinBox, QLineEdit, QMessageBox)
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(432, 510)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_emp = QtWidgets.QLabel(self.centralwidget)
        self.lbl_emp.setGeometry(QtCore.QRect(40, 130, 71, 21))
        self.lbl_emp.setObjectName("lbl_emp")
        self.cb_emp = QtWidgets.QComboBox(self.centralwidget)
        self.cb_emp.setGeometry(QtCore.QRect(130, 130, 91, 21))
        self.cb_emp.setObjectName("cb_emp")
        self.lbl_monto = QtWidgets.QLabel(self.centralwidget)
        self.lbl_monto.setGeometry(QtCore.QRect(40, 165, 71, 41))
        self.lbl_monto.setObjectName("lbl_monto")
        self.line_monto = QtWidgets.QLineEdit(self.centralwidget)
        self.line_monto.setGeometry(QtCore.QRect(130, 170, 71, 20))
        self.line_monto.setObjectName("line_monto")
        self.cb_siniestro = QtWidgets.QComboBox(self.centralwidget)
        self.cb_siniestro.setGeometry(QtCore.QRect(340, 130, 71, 20))
        self.cb_siniestro.setObjectName("cb_siniestro")
        self.lbl_siniestro = QtWidgets.QLabel(self.centralwidget)
        self.lbl_siniestro.setGeometry(QtCore.QRect(250, 130, 71, 41)) 
        self.lbl_siniestro.setObjectName("lbl_siniestro")
        self.line_gastos = QtWidgets.QLineEdit(self.centralwidget)
        self.line_gastos.setGeometry(QtCore.QRect(340, 170, 71, 20))
        self.line_gastos.setObjectName("line_gastos")
        self.lbl_gastosmin = QtWidgets.QLabel(self.centralwidget)
        self.lbl_gastosmin.setGeometry(QtCore.QRect(250, 165, 71, 41))
        self.lbl_gastosmin.setObjectName("lbl_gastosmin")
        self.rb_transp = QtWidgets.QRadioButton(self.centralwidget)
        self.rb_transp.setGeometry(QtCore.QRect(40, 210, 101, 41))
        self.rb_transp.setObjectName("rb_transp")
        self.rb_impor = QtWidgets.QRadioButton(self.centralwidget)
        self.rb_impor.setGeometry(QtCore.QRect(160, 210, 101, 41))
        self.rb_impor.setObjectName("rb_impor")
        self.rb_riesgos = QtWidgets.QRadioButton(self.centralwidget)
        self.rb_riesgos.setGeometry(QtCore.QRect(290, 210, 101, 41))
        self.rb_riesgos.setObjectName("rb_riesgos")
        self.pb_transp = QtWidgets.QPushButton(self.centralwidget)
        self.pb_transp.setGeometry(QtCore.QRect(30, 260, 91, 41))
        self.pb_transp.setObjectName("pb_transp")
        self.pb_impor = QtWidgets.QPushButton(self.centralwidget)
        self.pb_impor.setGeometry(QtCore.QRect(160, 260, 91, 41))
        self.pb_impor.setObjectName("pb_impor")
        self.pb_riesgos = QtWidgets.QPushButton(self.centralwidget)
        self.pb_riesgos.setEnabled(True)
        self.pb_riesgos.setGeometry(QtCore.QRect(300, 260, 91, 41))
        self.pb_riesgos.setCursor(QtGui.QCursor(QtCore.Qt.BusyCursor))
        self.pb_riesgos.setObjectName("pb_riesgos")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 330, 91, 21))
        self.label.setObjectName("label")
        self.line_honorarios = QtWidgets.QLineEdit(self.centralwidget)
        self.line_honorarios.setGeometry(QtCore.QRect(200, 330, 113, 21))
        self.line_honorarios.setObjectName("line_honorarios")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(130, 360, 91, 21))
        self.label_2.setObjectName("label_2")
        self.line_facturacion = QtWidgets.QLineEdit(self.centralwidget)
        self.line_facturacion.setGeometry(QtCore.QRect(200, 360, 113, 21))
        self.line_facturacion.setObjectName("line_facturacion")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(130, 390, 91, 21))
        self.label_3.setObjectName("label_3")
        self.line_igv = QtWidgets.QLineEdit(self.centralwidget)
        self.line_igv.setGeometry(QtCore.QRect(200, 390, 113, 21))
        self.line_igv.setObjectName("line_igv")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(130, 420, 91, 21))
        self.label_4.setObjectName("label_4")
        self.line_total = QtWidgets.QLineEdit(self.centralwidget)
        self.line_total.setGeometry(QtCore.QRect(200, 420, 113, 21))
        self.line_total.setObjectName("line_total")
        self.photo = QtWidgets.QLabel(self.centralwidget)
        self.photo.setGeometry(QtCore.QRect(150, 30, 221, 71))
        self.photo.setText("")
        self.photo.setPixmap(QtGui.QPixmap("rimac.png"))
        self.photo.setScaledContents(False)
        self.photo.setObjectName("photo")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 432, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        #Agregando los ComboBox al objeto cb_emp 
        self.cb_emp.addItem("--Seleccione--")
        self.cb_emp.addItem("Chubb")
        self.cb_emp.addItem("La Positiva")
        self.cb_emp.addItem("Mapfre")
        self.cb_emp.addItem("Pacifico")
        self.cb_emp.addItem("Rimac")

        
        # self.cb_emp.setEditText("--Seleccione--")
        # self.cb_emp.setCurrentText("--Seleccione--")
        
        # self.cb_emp.placeholderText()
        self.cb_emp.setFrame(False)


        #Agregando los Combobox al objeto cb_siniestro
        self.cb_siniestro.addItem("No aplica")
        self.cb_siniestro.addItem("Deshon.")
        self.cb_siniestro.addItem("Deshon. 3-D")
        self.cb_siniestro.addItem("Deshon. Din. en Bancos")
        self.cb_siniestro.addItem("Lucro Cesante der. ince")
        self.cb_siniestro.addItem("Lucro Cesante der. RT")
        self.cb_siniestro.addItem("Ramos Técnicos")
        self.cb_siniestro.addItem("Responsabilidad Civil")

        #Escondiendo los PushButtons
        self.pb_riesgos.hide()
        self.pb_impor.hide()
        self.pb_transp.hide()

        #Escondiendo la parte de Siniestros
        self.lbl_siniestro.hide()
        self.cb_siniestro.hide()
        
        #Escogiendo el logo de Protegia
        self.photo.setPixmap(QtGui.QPixmap("img/protegia.png"))


        #Restringiendo que en los labels solo se pueda introducir Numeros
        self.line_gastos.setValidator(QDoubleValidator())
        self.line_monto.setValidator(QDoubleValidator())
        self.line_honorarios.setValidator(QDoubleValidator())
        self.line_facturacion.setValidator(QDoubleValidator())
        self.line_igv.setValidator(QDoubleValidator())
        self.line_total.setValidator(QDoubleValidator())
        self.line_total.setValidator(QDoubleValidator())
        
        #Arreglando los labels
        self.lbl_emp.setWordWrap(True)
        self.lbl_emp.setAlignment(Qt.AlignRight)
        self.lbl_monto.setWordWrap(True)
        self.lbl_monto.setAlignment(Qt.AlignRight)
        self.lbl_gastosmin.setWordWrap(True)
        self.lbl_gastosmin.setAlignment(Qt.AlignRight)
        self.lbl_siniestro.setWordWrap(True)
        self.lbl_siniestro.setAlignment(Qt.AlignRight)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tarifario Protegia"))
        self.lbl_emp.setText(_translate("MainWindow", "Empresa"))
        self.lbl_monto.setText(_translate("MainWindow", "Monto del Reclamo"))
        self.lbl_gastosmin.setText(_translate("MainWindow", "Gastos Min. Promedio"))
        self.lbl_siniestro.setText(_translate("MainWindow", "Tipo de Siniestro"))
        self.rb_transp.setText(_translate("MainWindow", "Transp. Terr"))
        self.rb_impor.setText(_translate("MainWindow", "Import./Export."))
        self.rb_riesgos.setText(_translate("MainWindow", "Riesgos Gen."))
        self.pb_transp.setText(_translate("MainWindow", "Transp. Terr"))
        self.pb_impor.setText(_translate("MainWindow", "Import./Export."))
        self.pb_riesgos.setText(_translate("MainWindow", "Riesgos Gen."))
        self.label.setText(_translate("MainWindow", "Honorarios"))
        self.label_2.setText(_translate("MainWindow", "Facturación"))
        self.label_3.setText(_translate("MainWindow", "IGV"))
        self.label_4.setText(_translate("MainWindow", "Total"))
        self.line_gastos.setText(_translate("MainWindow", "0.00"))
        self.line_monto.setText(_translate("MainWindow", "0.00"))
        self.line_honorarios.setText(_translate("MainWindow", "0.00"))
        self.line_facturacion.setText(_translate("MainWindow", "0.00"))
        self.line_igv.setText(_translate("MainWindow", "0.00"))
        self.line_total.setText(_translate("MainWindow", "0.00"))
        MainWindow.setWindowIcon(QtGui.QIcon("img/protegia.png"))
        MainWindow.setWindowTitle("Protegia")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())