from PyQt5 import QtCore, QtGui, QtWidgets

from tarifario import Ui_MainWindow  # importing our generated file

import sys

class mywindow(QtWidgets.QMainWindow):

    def __init__(self):

        super(mywindow, self).__init__()

        self.ui = Ui_MainWindow()
        
        self.ui.setupUi(self)

        #Leyendo la salida del combobox de empresas
        self.ui.cb_emp.activated[str].connect(self.show_photo)

        #Leyendo la salida de los 03 radiobutton:
        self.ui.rb_transp.toggled.connect(self.show_button_transp)
        self.ui.rb_impor.toggled.connect(self.show_button_impor)
        self.ui.rb_riesgos.toggled.connect(self.show_button_riesgos)

        # Leyendo la salida de los qlineEdit:
        self.ui.line_gastos.editingFinished.connect(self.formato_moneda_gastos)
        self.ui.line_monto.editingFinished.connect(self.formato_moneda_monto)
        self.ui.line_honorarios.textChanged.connect(self.formato_moneda_honorarios)
        self.ui.line_facturacion.textChanged.connect(self.formato_moneda_facturacion)
        self.ui.line_igv.textChanged.connect(self.formato_moneda_igv)
        self.ui.line_total.textChanged.connect(self.formato_moneda_total)

        #Calculando la parte de los botones
        self.ui.pb_impor.clicked.connect(self.importaciones)
        self.ui.pb_transp.clicked.connect(self.transportes)
        self.ui.pb_riesgos.clicked.connect(self.riesgos)
        

    
    def show_photo(self):

        photo = self.ui.cb_emp.currentText()
        if photo == "--Seleccione--":
            self.ui.photo.setPixmap(QtGui.QPixmap("img/protegia.png"))
            self.ui.cb_siniestro.hide()
            self.ui.lbl_siniestro.hide()      
        elif photo == "Rimac":
            self.ui.photo.setPixmap(QtGui.QPixmap("img/rimac.png"))
            self.ui.cb_siniestro.hide()
            self.ui.lbl_siniestro.hide()
        elif photo == "La Positiva":
            self.ui.photo.setPixmap(QtGui.QPixmap("img/la_positiva.png"))
            self.ui.cb_siniestro.hide()
            self.ui.lbl_siniestro.hide()
        elif photo == "Mapfre":
            self.ui.photo.setPixmap(QtGui.QPixmap("img/mapfre.jpg"))
            self.ui.cb_siniestro.hide()
            self.ui.lbl_siniestro.hide()
        elif photo == "Pacifico":
            self.ui.photo.setPixmap(QtGui.QPixmap("img/pacifico.jpg"))
            self.ui.cb_siniestro.show()
            self.ui.lbl_siniestro.show()
        elif photo == "Chubb":
            self.ui.photo.setPixmap(QtGui.QPixmap("img/chubb.png"))
            self.ui.cb_siniestro.hide()
            self.ui.lbl_siniestro.hide()

    def show_button_transp(self):
        radioBtn = self.sender()
        if radioBtn.isChecked():
            self.ui.pb_transp.show()
        else:
            self.ui.pb_transp.hide()

    def show_button_impor(self):
        radioBtn = self.sender()
        if radioBtn.isChecked():
            self.ui.pb_impor.show()
        else:
            self.ui.pb_impor.hide()

    def show_button_riesgos(self):
        radioBtn = self.sender()
        if radioBtn.isChecked():
            self.ui.pb_riesgos.show()
        else:
            self.ui.pb_riesgos.hide()

    def formato_moneda_gastos(self):
        monedas = self.ui.line_gastos.text()
        lista = []
        for moneda in monedas:
            lista.append(moneda)
        for l in lista:
            if l == ",":
                lista.remove(",")
        lista = ''.join(map(str, lista))
        monedas = format(float(lista), '0,.2f')
        self.ui.line_gastos.setText(monedas)

    def formato_moneda_monto(self):
        monedas = self.ui.line_monto.text()
        lista = []
        for moneda in monedas:
            lista.append(moneda)
        for l in lista:
            if l == ",":
                lista.remove(",")
        lista = ''.join(map(str, lista))
        monedas = format(float(lista), '0,.2f')
        self.ui.line_monto.setText(monedas)

    def formato_moneda_honorarios(self):
        monedas = self.ui.line_honorarios.text()
        lista = []
        for moneda in monedas:
            lista.append(moneda)
        for l in lista:
            if l == ",":
                lista.remove(",")
        lista = ''.join(map(str, lista))
        monedas = format(float(lista), '0,.2f')
        self.ui.line_honorarios.setText(monedas)

    def formato_moneda_facturacion(self):
        monedas = self.ui.line_facturacion.text()
        lista = []
        for moneda in monedas:
            lista.append(moneda)
        for l in lista:
            if l == ",":
                lista.remove(",")
        lista = ''.join(map(str, lista))
        monedas = format(float(lista), '0,.2f')
        self.ui.line_facturacion.setText(monedas)

    def formato_moneda_igv(self):
        monedas = self.ui.line_igv.text()
        lista = []
        for moneda in monedas:
            lista.append(moneda)
        for l in lista:
            if l == ",":
                lista.remove(",")
        lista = ''.join(map(str, lista))
        monedas = format(float(lista), '0,.2f')
        self.ui.line_igv.setText(monedas)

    def formato_moneda_total(self):
        monedas = self.ui.line_total.text()
        lista = []
        for moneda in monedas:
            lista.append(moneda)
        for l in lista:
            if l == ",":
                lista.remove(",")
        lista = ''.join(map(str, lista))
        monedas = format(float(lista), '0,.2f')
        self.ui.line_total.setText(monedas)

    def transportes(self):
        if self.ui.line_monto.text() != "" or self.ui.line_gastos.text() != "":
            montos = self.ui.line_monto.text()
            lista_monto = []
            for monto in montos: 
                lista_monto.append(monto)
            for l in lista_monto:
                if l == ",":
                    lista_monto.remove(",")
            lista_monto = ''.join(map(str, lista_monto))
            monto = float(lista_monto)

            gastos =  self.ui.line_gastos.text()
            lista_gasto = []
            for gasto in gastos: 
                lista_gasto.append(gasto)
            for l in lista_gasto:
                if l == ",":
                    lista_gasto.remove(",")
            lista_gasto = ''.join(map(str, lista_gasto))
            gasto = float(lista_gasto)

            total = 0
            if self.ui.cb_emp.currentText() == "--Seleccione--":
                print("Debe seleccionar alguna de las compañias")
            elif self.ui.cb_emp.currentText() == "Chubb" or self.ui.cb_emp.currentText() == "La Positiva":
                if monto < 0:
                    pass
                elif monto > 1 and monto < 2481:
                    self.ui.line_honorarios.setText("100")
                    honorarios = 100
                    facturacion = honorarios + gasto
                    total = facturacion * 1.18
                    igv = total - facturacion
                    igv = str(igv)
                    facturacion = str(facturacion)
                    total = str(total)
                    self.ui.line_facturacion.setText(facturacion)
                    self.ui.line_igv.setText(igv)
                    self.ui.line_total.setText(total)
                elif monto >= 2481 and monto <= 5000:
                    honorarios = monto * 0.0403
                    self.imprimir_datos(honorarios, gasto)
                elif monto >= 10001 and monto <= 20000:
                    honorarios = ((monto - 10000) * 0.0349) + 390
                    self.imprimir_datos(honorarios, gasto)
                elif monto >= 20001 and monto <= 40000:
                    honorarios = ((monto - 20000) * 0.0323) + 739
                    self.imprimir_datos(honorarios, gasto)
                elif monto >= 40001 and monto <= 80000:
                    honorarios = ((monto - 40001) * 0.0295) + 1385
                    self.imprimir_datos(honorarios, gasto)
                elif monto >= 80001 and monto <= 160000:
                    honorarios = ((monto - 80000) * 0.0269) + 2565
                    self.imprimir_datos(honorarios, gasto)
                else:
                    pass

            elif self.ui.cb_emp.currentText() == "Rimac":
                if monto < 0:
                    pass
                elif monto > 1 and monto < 2500:
                    self.ui.line_honorarios.setText("0")
                    honorarios = 0
                    facturacion = honorarios + gasto
                    igv = facturacion * 1.18
                    total = igv - facturacion
                    igv = str(igv)
                    facturacion = str(facturacion)
                    total = str(total)
                    self.ui.line_facturacion.setText(facturacion)
                    self.ui.line_igv.setText(igv)
                    self.ui.line_total.setText(total)
                elif monto >= 2501 and monto <= 7500:
                    honorarios = monto * 0.035
                    self.imprimir_datos(honorarios, gasto)
                elif monto >= 7501 and monto <= 17500:
                    honorarios = ((monto - 7500) * 0.0327) + 262.5
                    self.imprimir_datos(honorarios, gasto)
                elif monto >= 17501 and monto <= 37500:
                    honorarios = ((monto - 17500) * 0.0306) + 589.5
                    self.imprimir_datos(honorarios, gasto)
                elif monto >= 37501 and monto <= 75000:
                    honorarios = ((monto - 37500) * 0.0286) + 1201.5
                    self.imprimir_datos(honorarios, gasto)
                elif monto >= 75001 and monto <= 160000:
                    honorarios = ((monto - 75000) * 0.0262) + 2274
                    self.imprimir_datos(honorarios, gasto)
                else:
                    #Los honorarios se calcularan de forma directa con la empresa
                    pass                

            elif self.ui.cb_emp.currentText() == "Pacifico":
                if monto < 0:
                    pass
                elif monto > 1 and monto < 1333:
                    self.ui.line_honorarios.setText("50")
                    honorarios = 50
                    facturacion = honorarios + gasto
                    igv = facturacion * 1.18
                    total = facturacion * 1.18
                    igv = total - facturacion
                    facturacion = str(facturacion)
                    total = str(total)
                    self.ui.line_facturacion.setText(facturacion)
                    self.ui.line_igv.setText(igv)
                    self.ui.line_total.setText(total)
                elif monto >= 1333 and monto <= 2500:
                    honorarios = monto * 0.035
                    self.imprimir_datos(honorarios, gasto)
                elif monto >= 2501 and monto <= 5000:
                    honorarios = ((monto - 2500) * 0.03) + 87.5
                    self.imprimir_datos(honorarios, gasto)
                elif monto >= 5001 and monto <= 10000:
                    honorarios = ((monto - 5000) * 0.025) + 162.5
                    self.imprimir_datos(honorarios, gasto)
                elif monto >= 10001 and monto <= 20000:
                    honorarios = ((monto - 10000) * 0.0225) + 287.5
                    self.imprimir_datos(honorarios, gasto)
                elif monto >= 20001 and monto <= 40000:
                    honorarios = ((monto - 20000) * 0.02) + 512.5
                    self.imprimir_datos(honorarios, gasto)
                elif monto >= 40001 and monto <= 80000:
                    honorarios = ((monto - 40000) * 0.0175) + 912.5
                    self.imprimir_datos(honorarios, gasto)
                elif monto >= 80001 and monto <= 160000:
                    honorarios = ((monto - 80000) * 0.015) + 1612.5
                    self.imprimir_datos(honorarios, gasto)
                elif monto >= 160001 and monto <= 320000:
                    honorarios = ((monto - 160000) * 0.0125) + 2812.5
                    self.imprimir_datos(honorarios, gasto)
                elif monto >= 320001 and monto <= 640000:
                    honorarios = ((monto - 320000) * 0.01) + 4812.5
                    self.imprimir_datos(honorarios, gasto)
                elif monto >= 640001 and monto <= 1000000:
                    honorarios = ((monto - 640000) * 0.0075) + 8012.5
                    self.imprimir_datos(honorarios, gasto)
                elif monto >= 1000000 and monto <= 2000000:
                    honorarios = ((monto - 1000000) * 0.005) + 10712.5
                    self.imprimir_datos(honorarios, gasto)
                else:
                    #Los honorarios se calcularan de forma directa con la empresa
                    pass         

            elif self.ui.cb_emp.currentText() == "Mapfre":
                if monto < 0:
                    pass
                elif monto > 1 and monto < 2481:
                    self.ui.line_honorarios.setText("100")
                    honorarios = 100
                    facturacion = honorarios + gasto
                    total = facturacion * 1.18
                    igv = total - facturacion
                    igv = str(igv)
                    facturacion = str(facturacion)
                    total = str(total)
                    self.ui.line_facturacion.setText(facturacion)
                    self.ui.line_igv.setText(igv)
                    self.ui.line_total.setText(total)
                elif monto >= 2481 and monto <= 5000:
                    honorarios = monto * 0.0403
                    self.imprimir_datos(honorarios, gasto)

                elif monto >= 5001 and monto <= 10000:
                    honorarios = ((monto - 5000) * 0.0377) + 201.5
                    self.imprimir_datos(honorarios, gasto)
                elif monto >= 10001 and monto <= 20000:
                    honorarios = ((monto - 10000) * 0.0349) + 390
                    self.imprimir_datos(honorarios, gasto)
                elif monto >= 20001 and monto <= 40000:
                    honorarios = ((monto - 20000) * 0.0323) + 739
                    self.imprimir_datos(honorarios, gasto)
                elif monto >= 40001 and monto <= 80000:
                    honorarios = ((monto - 40000) * 0.0295) + 1385
                    self.imprimir_datos(honorarios, gasto)
                elif monto >= 80001 and monto <= 160000:
                    honorarios = ((monto - 80000) * 0.0269) + 2565
                    self.imprimir_datos(honorarios, gasto)
                elif monto >= 160001 and monto <= 320000:
                    honorarios = ((monto - 160000) * 0.015) + 4717
                    self.imprimir_datos(honorarios, gasto)
                elif monto >= 320001 and monto <= 640000:
                    honorarios = ((monto - 320000) * 0.0125) + 7117
                    self.imprimir_datos(honorarios, gasto)
                elif monto >= 640001 and monto <= 1280000:
                    honorarios = ((monto - 640000) * 0.01) + 11117
                    self.imprimir_datos(honorarios, gasto)
                else:
                    #Los honorarios se calcularan de forma directa con la empresa
                    pass         

        pass
        # print("prueba")
    
    def importaciones(self):
        if self.ui.line_monto.text() != "" or self.ui.line_gastos.text() != "":
            montos = self.ui.line_monto.text()
            lista_monto = []
            for monto in montos: 
                lista_monto.append(monto)
            for l in lista_monto:
                if l == ",":
                    lista_monto.remove(",")
            lista_monto = ''.join(map(str, lista_monto))
            monto = float(lista_monto)

            gastos =  self.ui.line_gastos.text()
            lista_gasto = []
            for gasto in gastos: 
                lista_gasto.append(gasto)
            for l in lista_gasto:
                if l == ",":
                    lista_gasto.remove(",")
            lista_gasto = ''.join(map(str, lista_gasto))
            gasto = float(lista_gasto)

            if self.ui.cb_emp.currentText() == "--Seleccione--":
                print("Debe seleccionar alguna de las compañias")

            elif self.ui.cb_emp.currentText() == "Rimac":
                if monto < 0:
                    pass
                elif monto > 1 and monto <= 2500:
                    self.ui.line_honorarios.setText("0")
                    honorarios = 0
                    facturacion = honorarios + gasto
                    total = facturacion * 1.18
                    igv = total - facturacion
                    igv = str(igv)
                    facturacion = str(facturacion)
                    total = str(total)
                    self.ui.line_facturacion.setText(facturacion)
                    self.ui.line_igv.setText(igv)
                    self.ui.line_total.setText(total)
                elif monto >= 2501 and monto <= 7500:
                    honorarios = monto * 0.035
                    self.imprimir_datos(honorarios, gasto)
                elif monto >= 7501 and monto <= 17500:
                    honorarios = ((monto - 7500) * 0.0327) + 262.5
                    self.imprimir_datos(honorarios, gasto)
                elif monto >= 17501 and monto <= 37500:
                    honorarios = ((monto - 17501) * 0.0306) + 589.5
                    self.imprimir_datos(honorarios, gasto)
                elif monto >= 37501 and monto <= 75000:
                    honorarios = ((monto - 37500) * 0.0286) + 1201.5
                    self.imprimir_datos(honorarios, gasto)
                elif monto >= 75001 and monto <= 160000:
                    honorarios = ((monto - 75001) * 0.0262) + 2274
                    self.imprimir_datos(honorarios, gasto)
                else:
                    #Los honorarios se calcularan de forma directa con la empresa
                    pass

            elif self.ui.cb_emp.currentText() == "Pacifico":
                if monto < 0:
                    pass
                elif monto > 1 and monto <= 5000:
                    self.ui.line_honorarios.setText("96")
                    honorarios = 96
                    facturacion = honorarios + gasto
                    total = facturacion * 1.18
                    igv = total - facturacion
                    igv = str(igv)
                    facturacion = str(facturacion)
                    total = str(total)
                    self.ui.line_facturacion.setText(facturacion)
                    self.ui.line_igv.setText(igv)
                    self.ui.line_total.setText(total)
                elif monto >= 5001 and monto <= 10000:
                    self.ui.line_honorarios.setText("180")
                    honorarios = 180
                    facturacion = honorarios + gasto
                    total = facturacion * 1.18
                    igv = total - facturacion
                    igv = str(igv)
                    facturacion = str(facturacion)
                    total = str(total)
                    self.ui.line_facturacion.setText(facturacion)
                    self.ui.line_igv.setText(igv)
                    self.ui.line_total.setText(total)
                elif monto >= 10001 and monto <= 25000:
                    self.ui.line_honorarios.setText("275")
                    honorarios = 275
                    facturacion = honorarios + gasto
                    total = facturacion * 1.18
                    igv = total - facturacion
                    igv = str(igv)
                    facturacion = str(facturacion)
                    total = str(total)
                    self.ui.line_facturacion.setText(facturacion)
                    self.ui.line_igv.setText(igv)
                    self.ui.line_total.setText(total)
                elif monto >= 25001 and monto <= 50000:
                    self.ui.line_honorarios.setText("470")
                    honorarios = 470
                    facturacion = honorarios + gasto
                    total = facturacion * 1.18
                    igv = total - facturacion
                    igv = str(igv)
                    facturacion = str(facturacion)
                    total = str(total)
                    self.ui.line_facturacion.setText(facturacion)
                    self.ui.line_igv.setText(igv)
                    self.ui.line_total.setText(total)
                elif monto >= 50001 and monto <= 100000:
                    self.ui.line_honorarios.setText("800")
                    honorarios = 800
                    facturacion = honorarios + gasto
                    total = facturacion * 1.18
                    igv = total - facturacion
                    igv = str(igv)
                    facturacion = str(facturacion)
                    total = str(total)
                    self.ui.line_facturacion.setText(facturacion)
                    self.ui.line_igv.setText(igv)
                    self.ui.line_total.setText(total)
                elif monto > 100000:
                    pass

            elif self.ui.cb_emp.currentText() == "Mapfre":
                if monto < 0:
                    pass
                elif monto > 1 and monto <= 2000:
                    self.ui.line_honorarios.setText("50")
                    honorarios = 50
                    facturacion = honorarios + gasto
                    total = facturacion * 1.18
                    igv = total - facturacion
                    igv = str(igv)
                    facturacion = str(facturacion)
                    total = str(total)
                    self.ui.line_facturacion.setText(facturacion)
                    self.ui.line_igv.setText(igv)
                    self.ui.line_total.setText(total)
                elif monto >= 2001 and monto <= 5000:
                    honorarios = monto * 0.025
                    self.imprimir_datos(honorarios, gasto)
                elif monto >= 5001 and monto <= 10000:
                    honorarios = ((monto - 5000) * 0.0225) + 125
                    self.imprimir_datos(honorarios, gasto)
                elif monto >= 10001 and monto <= 20000:
                    honorarios = ((monto - 10000) * 0.02) + 237.5
                    self.imprimir_datos(honorarios, gasto)
                elif monto >= 20001 and monto <= 40000:
                    honorarios = ((monto - 20000) * 0.0175) + 437.5
                    self.imprimir_datos(honorarios, gasto)
                elif monto >= 40001 and monto <= 80000:
                    honorarios = ((monto - 40000) * 0.015) + 787.5
                    self.imprimir_datos(honorarios, gasto)
                elif monto >= 80001 and monto <= 160000:
                    honorarios = ((monto - 80000) * 0.0125) + 1387.5
                    self.imprimir_datos(honorarios, gasto)
                elif monto >= 160001 and monto <= 320000:
                    honorarios = ((monto - 160000) * 0.01) + 2387.5
                    self.imprimir_datos(honorarios, gasto)
                elif monto >= 320001 and monto <= 640000:
                    honorarios = ((monto - 320000) * 0.0075) + 3987.5
                    self.imprimir_datos(honorarios, gasto)
                else:
                    #Los honorarios se calcularan de forma directa con la empresa
                    pass

            elif self.ui.cb_emp.currentText() == "Chubb" or self.ui.cb_emp.currentText() == "La Positiva":
                if monto < 0:
                    pass
                elif monto > 1 and monto <= 2480:
                    self.ui.line_honorarios.setText("100")
                    honorarios = 100
                    facturacion = honorarios + gasto
                    total = facturacion * 1.18
                    igv = total - facturacion
                    igv = str(igv)
                    facturacion = str(facturacion)
                    total = str(total)
                    self.ui.line_facturacion.setText(facturacion)
                    self.ui.line_igv.setText(igv)
                    self.ui.line_total.setText(total)
                elif monto >= 2481 and monto <= 5000:
                    honorarios = monto * 0.0403
                    self.imprimir_datos(honorarios, gasto)
                elif monto >= 5001 and monto <= 10000:
                    honorarios = ((monto - 5000) * 0.0377) + 201.5
                    self.imprimir_datos(honorarios, gasto)
                elif monto >= 10001 and monto <= 20000:
                    honorarios = ((monto - 10000) * 0.0349) + 390
                    self.imprimir_datos(honorarios, gasto)
                elif monto >= 20001 and monto <= 40000:
                    honorarios = ((monto - 20000) * 0.0323) + 739
                    self.imprimir_datos(honorarios, gasto)
                elif monto >= 40001 and monto <= 80000:
                    honorarios = ((monto - 40000) * 0.0295) + 1385
                    self.imprimir_datos(honorarios, gasto)
                elif monto >= 80001 and monto <= 160000:
                    honorarios = ((monto - 80000) * 0.0269) + 2565
                    self.imprimir_datos(honorarios, gasto)
                else:
                    #Los honorarios se calcularan de forma directa con la empresa
                    pass

    def riesgos(self):

        if self.ui.line_monto.text() != "" or self.ui.line_gastos.text() != "":
            montos = self.ui.line_monto.text()
            lista_monto = []
            for monto in montos: 
                lista_monto.append(monto)
            for l in lista_monto:
                if l == ",":
                    lista_monto.remove(",")
            lista_monto = ''.join(map(str, lista_monto))
            monto = float(lista_monto)

            gastos =  self.ui.line_gastos.text()
            lista_gasto = []
            for gasto in gastos: 
                lista_gasto.append(gasto)
            for l in lista_gasto:
                if l == ",":
                    lista_gasto.remove(",")
            lista_gasto = ''.join(map(str, lista_gasto))
            gasto = float(lista_gasto)

            if self.ui.cb_emp.currentText() == "--Seleccione--":
                print("Debe seleccionar alguna de las compañias")

            elif self.ui.cb_emp.currentText() == "Chubb" or self.ui.cb_emp.currentText() == "La Positiva":
                if monto < 0:
                    pass
                elif monto > 1 and monto <= 2480:
                    self.ui.line_honorarios.setText("100")
                    honorarios = 100
                    facturacion = honorarios + gasto
                    total = facturacion * 1.18
                    igv = total - facturacion
                    igv = str(igv)
                    facturacion = str(facturacion)
                    total = str(total)
                    self.ui.line_facturacion.setText(facturacion)
                    self.ui.line_igv.setText(igv)
                    self.ui.line_total.setText(total)
                elif monto >= 2481 and monto <= 5000:
                    honorarios = monto * 0.0403
                    self.imprimir_datos(honorarios, gasto)
                elif monto >= 5001 and monto <= 10000:
                    honorarios = ((monto - 5000) * 0.0377) + 201.5
                    self.imprimir_datos(honorarios, gasto)
                elif monto >= 10001 and monto <= 20000:
                    honorarios = ((monto - 10000) * 0.0349) + 390
                    self.imprimir_datos(honorarios, gasto)
                elif monto >= 20001 and monto <= 40000:
                    honorarios = ((monto - 20000) * 0.0323) + 739
                    self.imprimir_datos(honorarios, gasto)
                elif monto >= 40001 and monto <= 80000:
                    honorarios = ((monto - 40000) * 0.0295) + 1385
                    self.imprimir_datos(honorarios, gasto)
                elif monto >= 80001 and monto <= 160000:
                    honorarios = ((monto - 80000) * 0.0269) + 2565
                    self.imprimir_datos(honorarios, gasto)
                elif monto >= 160001 and monto <= 320000:
                    honorarios = ((monto - 160000) * 0.0242) + 4717
                    self.imprimir_datos(honorarios, gasto)
                elif monto >= 320001 and monto <= 640000:
                    honorarios = ((monto - 80000) * 0.0215) + 8589
                    self.imprimir_datos(honorarios, gasto)
                elif monto >= 640001 and monto <= 1280000:
                    honorarios = ((monto - 640000) * 0.0202) + 15469
                    self.imprimir_datos(honorarios, gasto)
                elif monto >= 1280001 and monto <= 2560000:
                    honorarios = ((monto - 1280000) * 0.0188) + 28397
                    self.imprimir_datos(honorarios, gasto)
                elif monto >= 2560001 and monto <= 3560000:
                    honorarios = ((monto - 2560000) * 0.0175) + 52461
                    self.imprimir_datos(honorarios, gasto)
                else:
                    #Los honorarios se calcularan de forma directa con la empresa
                    pass

            elif self.ui.cb_emp.currentText() == "Mapfre" or self.ui.cb_emp.currentText() == "Rimac":
                if monto < 0:
                    pass
                elif monto > 1 and monto <= 2480:
                    self.ui.line_honorarios.setText("100")
                    honorarios = 100
                    facturacion = honorarios + gasto
                    total = facturacion * 1.18
                    igv = total - facturacion
                    igv = str(igv)
                    facturacion = str(facturacion)
                    total = str(total)
                    self.ui.line_facturacion.setText(facturacion)
                    self.ui.line_igv.setText(igv)
                    self.ui.line_total.setText(total)
                elif monto >= 2481 and monto <= 5000:
                    honorarios = monto * 0.0403
                    self.imprimir_datos(honorarios, gasto)
                elif monto >= 5001 and monto <= 10000:
                    honorarios = ((monto - 5000) * 0.0377) + 201.5
                    self.imprimir_datos(honorarios, gasto)
                elif monto >= 10001 and monto <= 20000:
                    honorarios = ((monto - 10000) * 0.0349) + 390
                    self.imprimir_datos(honorarios, gasto)
                elif monto >= 20001 and monto <= 40000:
                    honorarios = ((monto - 20000) * 0.0323) + 739
                    self.imprimir_datos(honorarios, gasto)
                elif monto >= 40001 and monto <= 80000:
                    honorarios = ((monto - 40000) * 0.0295) + 1385
                    self.imprimir_datos(honorarios, gasto)
                elif monto >= 80001 and monto <= 160000:
                    honorarios = ((monto - 80000) * 0.0269) + 2565
                    self.imprimir_datos(honorarios, gasto)
                elif monto >= 160001 and monto <= 320000:
                    honorarios = ((monto - 160000) * 0.0242) + 4717
                    self.imprimir_datos(honorarios, gasto)
                elif monto >= 320001 and monto <= 640000:
                    honorarios = ((monto - 80000) * 0.0215) + 8589
                    self.imprimir_datos(honorarios, gasto)
                elif monto >= 640001 and monto <= 1280000:
                    honorarios = ((monto - 640000) * 0.0202) + 15469
                    self.imprimir_datos(honorarios, gasto)
                elif monto >= 1280001 and monto <= 2560000:
                    honorarios = ((monto - 1280000) * 0.0188) + 28397
                    self.imprimir_datos(honorarios, gasto)
                elif monto >= 2560001 and monto <= 3560000:
                    honorarios = ((monto - 2560000) * 0.0175) + 52461
                    self.imprimir_datos(honorarios, gasto)
                else:
                    #Los honorarios se calcularan de forma directa con la empresa
                    pass

            elif self.ui.cb_emp.currentText() == "Pacifico":
                if monto < 0:
                    pass
                elif monto >= 1 and monto < 953:
                    self.ui.line_honorarios.setText("40")
                    honorarios = 40
                    facturacion = honorarios + gasto
                    total = facturacion * 1.18
                    igv = total - facturacion
                    igv = str(igv)
                    facturacion = str(facturacion)
                    total = str(total)
                    self.ui.line_facturacion.setText(facturacion)
                    self.ui.line_igv.setText(igv)
                    self.ui.line_total.setText(total)
                elif monto >= 953 and monto <= 2500:
                    honorarios = (monto * 0.042)
                    self.imprimir_datos_especial(honorarios, gasto)
                elif monto >= 2501 and monto <= 5000:
                    honorarios = ((monto - 2500) * 0.036) + 105
                    self.imprimir_datos_especial(honorarios, gasto)
                elif monto >= 5001 and monto <= 10000:
                    honorarios = ((monto - 5000) * 0.03) + 195
                    self.imprimir_datos_especial(honorarios, gasto)
                elif monto >= 10001 and monto <= 20000:
                    honorarios = ((monto - 10000) * 0.027) + 345
                    self.imprimir_datos_especial(honorarios, gasto)
                elif monto >= 10001 and monto <= 20000:
                    honorarios = ((monto - 10000) * 0.027) + 345
                    self.imprimir_datos_especial(honorarios, gasto)
                elif monto >= 20001 and monto <= 40000:
                    honorarios = ((monto - 20000) * 0.024) + 615
                    self.imprimir_datos_especial(honorarios, gasto)
                elif monto >= 40001 and monto <= 80000:
                    honorarios = ((monto - 40000) * 0.021) + 1095
                    self.imprimir_datos_especial(honorarios, gasto)
                elif monto >= 80001 and monto <= 160000:
                    honorarios = ((monto - 80000) * 0.018) + 1935
                    self.imprimir_datos_especial(honorarios, gasto)
                elif monto >= 160001 and monto <= 320000:
                    honorarios = ((monto - 160000) * 0.015) + 3375
                    self.imprimir_datos_especial(honorarios, gasto)
                elif monto >= 320001 and monto <= 640000:
                    honorarios = ((monto - 320000) * 0.012) + 5775
                    self.imprimir_datos_especial(honorarios, gasto)
                elif monto >= 640001 and monto <= 1000000:
                    honorarios = ((monto - 640000) * 0.009) + 9615
                    self.imprimir_datos_especial(honorarios, gasto)
                elif monto >= 1000001 and monto <= 2000000:
                    honorarios = ((monto - 1000000) * 0.008) + 12855
                    self.imprimir_datos_especial(honorarios, gasto)
                elif monto >= 2000001 and monto <= 4000000:
                    honorarios = ((monto - 2000000) * 0.007) + 20855
                    self.imprimir_datos_especial(honorarios, gasto)
                elif monto >= 4000001 and monto <= 8000000:
                    honorarios = ((monto - 4000000) * 0.006) + 34855
                    self.imprimir_datos_especial(honorarios, gasto)
                elif monto >= 8000001 and monto <= 16000000:
                    honorarios = ((monto - 8000000) * 0.005) + 58855
                    self.imprimir_datos_especial(honorarios, gasto)
                elif monto >= 16000001 and monto <= 32000000:
                    honorarios = ((monto - 16000000) * 0.004) + 98855
                    self.imprimir_datos_especial(honorarios, gasto)
                else:
                    pass

    def imprimir_datos(self, honorarios, gasto):
        facturacion = honorarios + gasto
        total = facturacion * 1.18
        igv = total - facturacion
        igv = str(igv)
        facturacion = str(facturacion)
        total = str(total)
        honorarios = str(honorarios)
        self.ui.line_honorarios.setText(honorarios)
        self.ui.line_facturacion.setText(facturacion)
        self.ui.line_igv.setText(igv)
        self.ui.line_total.setText(total)

    def imprimir_datos_especial(self, honorarios, gasto):
        
        if self.ui.cb_siniestro.currentText() == "--Seleccione--":
            pass
        elif self.ui.cb_siniestro.currentText() == "No aplica":
            facturacion = honorarios + gasto
            total = facturacion * 1.18
            igv = total - facturacion
            igv = str(igv)
            facturacion = str(facturacion)
            total = str(total)
            honorarios = str(honorarios)
            self.ui.line_honorarios.setText(honorarios)
            self.ui.line_facturacion.setText(facturacion)
            self.ui.line_igv.setText(igv)
            self.ui.line_total.setText(total)
        elif self.ui.cb_siniestro.currentText() == "Deshon.":
            honorarios = honorarios * 1.15
            facturacion = honorarios + gasto
            total = facturacion * 1.18
            igv = total - facturacion
            igv = str(igv)
            facturacion = str(facturacion)
            total = str(total)
            honorarios = str(honorarios)
            self.ui.line_honorarios.setText(honorarios)
            self.ui.line_facturacion.setText(facturacion)
            self.ui.line_igv.setText(igv)
            self.ui.line_total.setText(total)
        elif self.ui.cb_siniestro.currentText() == "Deshon. 3-D":
            honorarios = honorarios * 0.75
            facturacion = honorarios + gasto
            total = facturacion * 1.18
            igv = total - facturacion
            igv = str(igv)
            facturacion = str(facturacion)
            total = str(total)
            honorarios = str(honorarios)
            self.ui.line_honorarios.setText(honorarios)
            self.ui.line_facturacion.setText(facturacion)
            self.ui.line_igv.setText(igv)
            self.ui.line_total.setText(total)      
        elif self.ui.cb_siniestro.currentText() == "Deshon. Din. en Bancos":
            honorarios = honorarios * 0.7
            facturacion = honorarios + gasto
            total = facturacion * 1.18
            igv = total - facturacion
            igv = str(igv)
            facturacion = str(facturacion)
            total = str(total)
            honorarios = str(honorarios)
            self.ui.line_honorarios.setText(honorarios)
            self.ui.line_facturacion.setText(facturacion)
            self.ui.line_igv.setText(igv)
            self.ui.line_total.setText(total)
        elif self.ui.cb_siniestro.currentText() == "Lucro Cesante der. ince":
            honorarios = honorarios * 1.1
            facturacion = honorarios + gasto
            total = facturacion * 1.18
            igv = total - facturacion
            igv = str(igv)
            facturacion = str(facturacion)
            total = str(total)
            honorarios = str(honorarios)
            self.ui.line_honorarios.setText(honorarios)
            self.ui.line_facturacion.setText(facturacion)
            self.ui.line_igv.setText(igv)
            self.ui.line_total.setText(total)
        elif self.ui.cb_siniestro.currentText() == "Lucro Cesante der. RT":
            honorarios = honorarios * 1.1
            facturacion = honorarios + gasto
            total = facturacion * 1.18
            igv = total - facturacion
            igv = str(igv)
            facturacion = str(facturacion)
            total = str(total)
            honorarios = str(honorarios)
            self.ui.line_honorarios.setText(honorarios)
            self.ui.line_facturacion.setText(facturacion)
            self.ui.line_igv.setText(igv)
            self.ui.line_total.setText(total)
        elif self.ui.cb_siniestro.currentText() == "Ramos Técnicos":
            honorarios = honorarios * 1.25
            facturacion = honorarios + gasto
            total = facturacion * 1.18
            igv = total - facturacion
            igv = str(igv)
            facturacion = str(facturacion)
            total = str(total)
            honorarios = str(honorarios)
            self.ui.line_honorarios.setText(honorarios)
            self.ui.line_facturacion.setText(facturacion)
            self.ui.line_igv.setText(igv)
            self.ui.line_total.setText(total)
        elif self.ui.cb_siniestro.currentText() == "Responsabilidad Civil":
            honorarios = honorarios * 1.25
            facturacion = honorarios + gasto
            total = facturacion * 1.18
            igv = total - facturacion
            igv = str(igv)
            facturacion = str(facturacion)
            total = str(total)
            honorarios = str(honorarios)
            self.ui.line_honorarios.setText(honorarios)
            self.ui.line_facturacion.setText(facturacion)
            self.ui.line_igv.setText(igv)
            self.ui.line_total.setText(total)

app = QtWidgets.QApplication([])

application = mywindow()

application.show()

sys.exit(app.exec())