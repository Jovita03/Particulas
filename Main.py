from PySide2.QtWidgets import QMainWindow, QApplication
from Mainwindow import Mainwindow
import sys

app = QApplication()#inicia la aplicacion de qt
window = Mainwindow()
window.show()#esto permite que sea visible la interfaz 

sys.exit(app.exec_())#se garantiza se haya hecho el proceso correctamente
