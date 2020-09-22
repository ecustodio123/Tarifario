# numero = 500002583.589

# # Dos decimales de precisión:
# # print(format(numero, '0.2f'))

# # Jusitificación a la derecha con diez caracteres, un decimal de precisión:
# # print(format(numero, '>10.1f'))

# # Jusitificación a la izquierda con diez caracteres, un decimal de precisión:
# # print(format(numero, '<10.1f'))

# # Separador de miles:
# print(format(numero, '0,.2f'))
# # print(format(numero, '0,.1f'))

# # Notación científica:
# # print(format(numero, 'e'))
# # print(format(numero, '0.2E'))

import sys
from PyQt5 import QtWidgets, QtGui

def MyWindow():

    app = QtWidgets.QApplication(sys.argv)

    window = QtWidgets.QWidget()
    window.setGeometry(100, 100, 600, 400)
    window.setWindowIcon(QtGui.QIcon("img/protegia.png"))
    # label1 = QtWidgets.QLabel(window)
    # label2 = QtWidgets.QLabel(window)
    # label1.setText('PyQT5 Gui Programming')
    # label2.setPixmap(QtGui.QPixmap("img/rimac.png"))
    # label1.move(120,20)
    # label1.move(250,20)

    window.setWindowTitle("PyQT5 First LEsson")

    window.show()
    sys.exit(app.exec())

MyWindow()