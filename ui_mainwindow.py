# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(929, 724)
        self.actionArbir = QAction(MainWindow)
        self.actionArbir.setObjectName(u"actionArbir")
        self.actionGuardar = QAction(MainWindow)
        self.actionGuardar.setObjectName(u"actionGuardar")
        self.actionID = QAction(MainWindow)
        self.actionID.setObjectName(u"actionID")
        self.actionVelocidad = QAction(MainWindow)
        self.actionVelocidad.setObjectName(u"actionVelocidad")
        self.actionDistancia = QAction(MainWindow)
        self.actionDistancia.setObjectName(u"actionDistancia")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.plainTextEdit = QPlainTextEdit(self.tab)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(340, 20, 561, 591))
        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 10, 311, 621))
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.Blue_label = QLabel(self.groupBox)
        self.Blue_label.setObjectName(u"Blue_label")

        self.gridLayout.addWidget(self.Blue_label, 8, 0, 1, 1)

        self.Velocidad_label = QLabel(self.groupBox)
        self.Velocidad_label.setObjectName(u"Velocidad_label")

        self.gridLayout.addWidget(self.Velocidad_label, 5, 0, 1, 1)

        self.Velocidad_spinBox = QSpinBox(self.groupBox)
        self.Velocidad_spinBox.setObjectName(u"Velocidad_spinBox")
        self.Velocidad_spinBox.setMaximum(100000)

        self.gridLayout.addWidget(self.Velocidad_spinBox, 5, 1, 1, 1)

        self.inicio_pushButton = QPushButton(self.groupBox)
        self.inicio_pushButton.setObjectName(u"inicio_pushButton")

        self.gridLayout.addWidget(self.inicio_pushButton, 9, 0, 1, 2)

        self.DestinoX_label = QLabel(self.groupBox)
        self.DestinoX_label.setObjectName(u"DestinoX_label")

        self.gridLayout.addWidget(self.DestinoX_label, 1, 0, 1, 1)

        self.Red_label = QLabel(self.groupBox)
        self.Red_label.setObjectName(u"Red_label")

        self.gridLayout.addWidget(self.Red_label, 6, 0, 1, 1)

        self.Red_spinBox = QSpinBox(self.groupBox)
        self.Red_spinBox.setObjectName(u"Red_spinBox")
        self.Red_spinBox.setMaximum(255)

        self.gridLayout.addWidget(self.Red_spinBox, 6, 1, 1, 1)

        self.Blue_spinBox = QSpinBox(self.groupBox)
        self.Blue_spinBox.setObjectName(u"Blue_spinBox")
        self.Blue_spinBox.setMaximum(255)

        self.gridLayout.addWidget(self.Blue_spinBox, 8, 1, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.DestinoX_spinBox = QSpinBox(self.groupBox)
        self.DestinoX_spinBox.setObjectName(u"DestinoX_spinBox")
        self.DestinoX_spinBox.setMaximum(500)

        self.gridLayout.addWidget(self.DestinoX_spinBox, 1, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)

        self.OrigenY_spinBox = QSpinBox(self.groupBox)
        self.OrigenY_spinBox.setObjectName(u"OrigenY_spinBox")
        self.OrigenY_spinBox.setMaximum(500)

        self.gridLayout.addWidget(self.OrigenY_spinBox, 4, 1, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)

        self.DestinoY_label = QLabel(self.groupBox)
        self.DestinoY_label.setObjectName(u"DestinoY_label")

        self.gridLayout.addWidget(self.DestinoY_label, 2, 0, 1, 1)

        self.Green_spinBox = QSpinBox(self.groupBox)
        self.Green_spinBox.setObjectName(u"Green_spinBox")
        self.Green_spinBox.setMaximum(255)

        self.gridLayout.addWidget(self.Green_spinBox, 7, 1, 1, 1)

        self.DestinoY_spinBox = QSpinBox(self.groupBox)
        self.DestinoY_spinBox.setObjectName(u"DestinoY_spinBox")
        self.DestinoY_spinBox.setMaximum(500)

        self.gridLayout.addWidget(self.DestinoY_spinBox, 2, 1, 1, 1)

        self.Green_label = QLabel(self.groupBox)
        self.Green_label.setObjectName(u"Green_label")

        self.gridLayout.addWidget(self.Green_label, 7, 0, 1, 1)

        self.OrigenX_spinBox = QSpinBox(self.groupBox)
        self.OrigenX_spinBox.setObjectName(u"OrigenX_spinBox")
        self.OrigenX_spinBox.setMaximum(500)

        self.gridLayout.addWidget(self.OrigenX_spinBox, 3, 1, 1, 1)

        self.Id_spinBox = QSpinBox(self.groupBox)
        self.Id_spinBox.setObjectName(u"Id_spinBox")
        self.Id_spinBox.setMaximum(500)

        self.gridLayout.addWidget(self.Id_spinBox, 0, 1, 1, 1)

        self.mostrar_pushButton = QPushButton(self.groupBox)
        self.mostrar_pushButton.setObjectName(u"mostrar_pushButton")

        self.gridLayout.addWidget(self.mostrar_pushButton, 10, 0, 1, 1)

        self.final_pushButton = QPushButton(self.groupBox)
        self.final_pushButton.setObjectName(u"final_pushButton")

        self.gridLayout.addWidget(self.final_pushButton, 10, 1, 1, 1)

        self.lista_de_adyacencia_pushButton = QPushButton(self.groupBox)
        self.lista_de_adyacencia_pushButton.setObjectName(u"lista_de_adyacencia_pushButton")

        self.gridLayout.addWidget(self.lista_de_adyacencia_pushButton, 11, 0, 1, 2)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabla = QTableWidget(self.tab_2)
        self.tabla.setObjectName(u"tabla")
        self.tabla.setGeometry(QRect(10, 20, 881, 521))
        self.buscar_lineEdit = QLineEdit(self.tab_2)
        self.buscar_lineEdit.setObjectName(u"buscar_lineEdit")
        self.buscar_lineEdit.setGeometry(QRect(30, 570, 341, 21))
        self.buscar_pushButton = QPushButton(self.tab_2)
        self.buscar_pushButton.setObjectName(u"buscar_pushButton")
        self.buscar_pushButton.setGeometry(QRect(390, 570, 93, 28))
        self.mostrar_tabla_pushButton = QPushButton(self.tab_2)
        self.mostrar_tabla_pushButton.setObjectName(u"mostrar_tabla_pushButton")
        self.mostrar_tabla_pushButton.setGeometry(QRect(500, 570, 93, 28))
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.Dibujar_pushButton = QPushButton(self.tab_3)
        self.Dibujar_pushButton.setObjectName(u"Dibujar_pushButton")
        self.Dibujar_pushButton.setGeometry(QRect(20, 550, 241, 31))
        self.Limpiar_pushButton = QPushButton(self.tab_3)
        self.Limpiar_pushButton.setObjectName(u"Limpiar_pushButton")
        self.Limpiar_pushButton.setGeometry(QRect(20, 590, 241, 31))
        self.graphicsView = QGraphicsView(self.tab_3)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setGeometry(QRect(20, 20, 861, 481))
        self.Ver_puntos_pushButton = QPushButton(self.tab_3)
        self.Ver_puntos_pushButton.setObjectName(u"Ver_puntos_pushButton")
        self.Ver_puntos_pushButton.setGeometry(QRect(280, 590, 171, 31))
        self.puntos_mas_cercanos_pushButton = QPushButton(self.tab_3)
        self.puntos_mas_cercanos_pushButton.setObjectName(u"puntos_mas_cercanos_pushButton")
        self.puntos_mas_cercanos_pushButton.setGeometry(QRect(280, 550, 171, 31))
        self.kruskal_pushButton = QPushButton(self.tab_3)
        self.kruskal_pushButton.setObjectName(u"kruskal_pushButton")
        self.kruskal_pushButton.setGeometry(QRect(470, 550, 151, 31))
        self.label_4 = QLabel(self.tab_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(120, 520, 47, 13))
        self.label_5 = QLabel(self.tab_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(340, 520, 71, 16))
        self.label_6 = QLabel(self.tab_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(520, 520, 41, 16))
        self.dijkstra_pushButton = QPushButton(self.tab_3)
        self.dijkstra_pushButton.setObjectName(u"dijkstra_pushButton")
        self.dijkstra_pushButton.setGeometry(QRect(470, 590, 151, 31))
        self.OrigenX_spinBox_2 = QSpinBox(self.tab_3)
        self.OrigenX_spinBox_2.setObjectName(u"OrigenX_spinBox_2")
        self.OrigenX_spinBox_2.setGeometry(QRect(770, 520, 71, 22))
        self.OrigenX_spinBox_2.setMaximum(1000)
        self.DestinoX_spinBox_2 = QSpinBox(self.tab_3)
        self.DestinoX_spinBox_2.setObjectName(u"DestinoX_spinBox_2")
        self.DestinoX_spinBox_2.setGeometry(QRect(770, 550, 71, 22))
        self.DestinoX_spinBox_2.setMaximum(1000)
        self.OrigenY_spinBox_2 = QSpinBox(self.tab_3)
        self.OrigenY_spinBox_2.setObjectName(u"OrigenY_spinBox_2")
        self.OrigenY_spinBox_2.setGeometry(QRect(770, 580, 71, 22))
        self.OrigenY_spinBox_2.setMaximum(1000)
        self.DestinoY_spinBox_2 = QSpinBox(self.tab_3)
        self.DestinoY_spinBox_2.setObjectName(u"DestinoY_spinBox_2")
        self.DestinoY_spinBox_2.setGeometry(QRect(770, 610, 71, 22))
        self.DestinoY_spinBox_2.setMaximum(1000)
        self.label_7 = QLabel(self.tab_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(680, 520, 101, 16))
        self.label_8 = QLabel(self.tab_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(680, 550, 101, 16))
        self.label_9 = QLabel(self.tab_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(680, 580, 47, 13))
        self.label_10 = QLabel(self.tab_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(680, 610, 47, 13))
        self.tabWidget.addTab(self.tab_3, "")

        self.gridLayout_3.addWidget(self.tabWidget, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 929, 21))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        self.menuOrdenar = QMenu(self.menubar)
        self.menuOrdenar.setObjectName(u"menuOrdenar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuOrdenar.menuAction())
        self.menuArchivo.addAction(self.actionArbir)
        self.menuArchivo.addAction(self.actionGuardar)
        self.menuOrdenar.addAction(self.actionID)
        self.menuOrdenar.addAction(self.actionVelocidad)
        self.menuOrdenar.addAction(self.actionDistancia)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionArbir.setText(QCoreApplication.translate("MainWindow", u"Arbir", None))
#if QT_CONFIG(shortcut)
        self.actionArbir.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionGuardar.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
#if QT_CONFIG(shortcut)
        self.actionGuardar.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionID.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.actionVelocidad.setText(QCoreApplication.translate("MainWindow", u"Velocidad ", None))
        self.actionDistancia.setText(QCoreApplication.translate("MainWindow", u"Distancia ", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Particulas", None))
        self.Blue_label.setText(QCoreApplication.translate("MainWindow", u"Blue", None))
        self.Velocidad_label.setText(QCoreApplication.translate("MainWindow", u"Velocidad", None))
        self.inicio_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar Iinicio ", None))
        self.DestinoX_label.setText(QCoreApplication.translate("MainWindow", u"Destino X", None))
        self.Red_label.setText(QCoreApplication.translate("MainWindow", u"Red", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Id", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Origen X", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Origen Y", None))
        self.DestinoY_label.setText(QCoreApplication.translate("MainWindow", u"Destino Y", None))
        self.Green_label.setText(QCoreApplication.translate("MainWindow", u"Green", None))
        self.mostrar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.final_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar Final", None))
        self.lista_de_adyacencia_pushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar lista de adyacencia ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.buscar_lineEdit.setText("")
        self.buscar_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Id a buscar ", None))
        self.buscar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.mostrar_tabla_pushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tabla", None))
        self.Dibujar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Dibujar", None))
        self.Limpiar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Limpiar ", None))
        self.Ver_puntos_pushButton.setText(QCoreApplication.translate("MainWindow", u"Ver Puntos", None))
        self.puntos_mas_cercanos_pushButton.setText(QCoreApplication.translate("MainWindow", u"Ver Puntos Mas Cercanos ", None))
        self.kruskal_pushButton.setText(QCoreApplication.translate("MainWindow", u"Kruskal ", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Grafico", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Fuerza Bruta", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Grafos", None))
        self.dijkstra_pushButton.setText(QCoreApplication.translate("MainWindow", u"Dijkstra", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Origen X", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Destino X ", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Origen Y", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Destino Y ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Grafico", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
        self.menuOrdenar.setTitle(QCoreApplication.translate("MainWindow", u"Ordenar ", None))
    # retranslateUi

