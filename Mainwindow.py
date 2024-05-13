import PySide2.QtCore
from PySide2.QtWidgets import QMainWindow,QFileDialog,QMessageBox,QTableWidgetItem,QGraphicsScene
from ui_mainwindow import Ui_MainWindow
from PySide2.QtCore import Slot #impprtamos todo esto para que se pueda implementar la interfaz
from PySide2.QtGui import QPen, QColor,QTransform
from Particulas import particulas
from Funciones import funciones 
from Algoritmos import puntos_mas_cercanos,kruskal
from random import randint
from pprint import pprint 

class Mainwindow(QMainWindow):
    #se crea una clase que se va a convertir en la ventana principal de la aplicacion 
    def __init__(self):
        #se define el constructor de la clase principal
        super(Mainwindow, self).__init__()
        self.ui = Ui_MainWindow() #aqui se vincula lo del mainwindow del qt
        self.funciones=funciones()
        self.ui.setupUi(self) 
        self.scene=QGraphicsScene()
        self.ui.graphicsView.setScene(self.scene)

        self.grafo = dict()
        self.ui.inicio_pushButton.clicked.connect(self.inicio)
        self.ui.final_pushButton.clicked.connect(self.final)
        self.ui.mostrar_pushButton.clicked.connect(self.click_mostrar)
        self.ui.actionArbir.triggered.connect(self.action_Abrir_Archivo)
        self.ui.actionGuardar.triggered.connect(self.action_Guardar_Archivo)
        self.ui.mostrar_tabla_pushButton.clicked.connect(self.mostrar_tabla)
        self.ui.buscar_pushButton.clicked.connect(self.buscar_id)
        self.ui.Dibujar_pushButton.clicked.connect(self.dibujar)
        self.ui.Limpiar_pushButton.clicked.connect(self.limpiar)
        self.ui.actionID.triggered.connect(self.action_sort_by_ID)
        self.ui.actionDistancia.triggered.connect(self.action_sort_by_Distancia)
        self.ui.actionVelocidad.triggered.connect(self.action_sort_by_Velocidad)
        self.ui.Ver_puntos_pushButton.clicked.connect(self.click_ver_puntos)
        self.ui.puntos_mas_cercanos_pushButton.clicked.connect(self.click_puntos_mas_cercanos)
        self.ui.lista_de_adyacencia_pushButton.clicked.connect(self.click_lista_de_adyacencia)
        self.ui.kruskal_pushButton.clicked.connect(self.click_kruskal)
        
#cada funcion que se agregue se debe colocar aqui para que pueda vincularse y se muestre correctamente

    @Slot()
    def click_kruskal(self):
        self.grafo.clear()
        for particula in self.funciones:
            origen = (particula.origenx,particula.origeny)
            destino = (particula.destinox, particula.destinoy)
            distancia = particula.distancia
            if origen in self.grafo:
                self.grafo[origen].append((destino, distancia))     
            else:
                self.grafo[origen] = [(destino, distancia)]
            if destino in self.grafo:
                self.grafo[destino].append((origen, distancia))
            else:
                self.grafo[destino] = [(origen, distancia)]
        #self.limpiar()
        print(self.grafo)
        #arbol_minimo_aristas = kruskal(self.grafo)
        #pen_arbol = QPen()
        #pen_arbol.setWidth(2)
        #pen_arbol.setColor(QColor(0, 0, 0))
        #self.click_ver_puntos()

        #for arista in arbol_minimo_aristas:
            #origen = arista[0]
            #destino = arista[1]
            # Dibujar la arista en la escena de QGraphicsView
            #self.scene.addLine(origen[0] + 3, origen[1] + 3, destino[0] + 3, destino[1] + 3, pen_arbol)
        #pprint(arbol_minimo_aristas)


    @Slot()
    def click_lista_de_adyacencia(self):
        self.grafo.clear()
        for particula in self.funciones:
            origen = (particula.origenx, particula.origeny)
            destino = (particula.destinox, particula.destinoy)
            distancia = particula.distancia
            if origen in self.grafo:
                self.grafo[origen].append((destino, distancia))     
            else:
                self.grafo[origen] = [(destino, distancia)]
            if destino in self.grafo:
                self.grafo[destino].append((origen, distancia))
            else:
                self.grafo[destino] = [(origen, distancia)]

        self.scene.clear()
        self.ui.plainTextEdit.clear()
        self.ui.plainTextEdit.insertPlainText(str(self.grafo))
        pprint(self.grafo)



    @Slot()
    def click_ver_puntos(self):#funcion para ver los puntos en la interfaz
        self.limpiar()
        pen= QPen()
        pen.setWidth(2)#se muestra el grosor de cada linea dibujada 

        for particula in self.funciones:
            red = particula.red
            green = particula.green
            blue = particula.blue

            x_origen = particula.origenx
            y_origen = particula.origeny
            x_destino = particula.destinox
            y_destino = particula.destinoy
            #esta funcion es para mostrar unicamente los puntos, lo cual toma cada valor de las partuculas y los 
            #rteanforma a dibujos ´pr ,medio de self.scene enlas elipses

            color = QColor(red, green, blue)
            pen.setColor(color)

            self.scene.addEllipse(x_origen,y_origen,6,6,pen)
            self.scene.addEllipse(x_destino,y_destino,6,6,pen)    

    @Slot()
    def click_puntos_mas_cercanos(self):
        self.limpiar()
        self.click_ver_puntos()
        pen = QPen()
        pen.setWidth(2)
        puntos = [] #inicializa una lista vacía llamada puntos para almacenar las coordenadas de los puntos que se van a dibujar
        for particula in self.funciones:#itera sobre los elementos de self, iterando en cada particula que hay en funciones 
            x_origen = particula.origenx
            y_origen = particula.origeny
            x_destino = particula.destinox#las coordenadas de origen y destino de cada particula se extraen y se agregan a la lista puntos.
            y_destino = particula.destinoy
            puntos.append((x_origen, y_origen))#se utiliza para agregar un elemento al final de una lista existente
            puntos.append((x_destino, y_destino))
        
        resultado = puntos_mas_cercanos(puntos) #devuelve los pumtos mas cercanos 
        for punto1, punto2 in resultado:#el pumto 1 y 2 se extraen u se asignan a x1 y x2
            x1 = punto1[0]
            y1 = punto1[1]
            x2 = punto2[0]
            y2 = punto2[1]
            red = randint(0,255)
            green = randint(0,255)
            blue = randint(0,255)
            
            color = QColor(red, green, blue)#se  establece un onjeto con sus componentes 
            pen.setColor(color)
            self.scene.addLine(x1, y1, x2, y2, pen)#se dibuja en la interfaz
            

#sirve para mostrar las particulas de manera ordenada 
    @Slot()
    def action_sort_by_Velocidad(self):
        self.funciones.sort_by_velocidad()
        self.mostrar_tabla()
    @Slot()#ordenacion por distancia
    def action_sort_by_Distancia(self):
        self.funciones.sort_by_distancia()
        self.mostrar_tabla()
    @Slot()#ordenacion por id
    def action_sort_by_ID(self):
        self.funciones.sort_by_id()
        self.mostrar_tabla()
    
    @Slot()
    def dibujar(self):
        self.limpiar()
        pen= QPen()#esta libreria es para dibujar 
        pen.setWidth(2)#establece el grosor de la linea que se dibujara 

        for particula in self.funciones:#este for itera sobre los objetos de sel.funciones t 
            red = particula.red#cada color toma el valor de lo que haya dentro de cada particula
            green = particula.green
            blue = particula.blue

            x_origen = particula.origenx
            y_origen = particula.origeny
            x_destino = particula.destinox#lo mismo que en el color este toma pero el lugar de cada particula
            y_destino = particula.destinoy

            color = QColor(red, green, blue)
            pen.setColor(color)
            #en esta parte se dinuja de acuierdo a lo asignado anteriormente 
            self.scene.addEllipse(x_origen,y_origen,6,6,pen)
            self.scene.addEllipse(x_destino,y_destino,6,6,pen)
            self.scene.addLine(x_origen+3 ,y_origen+3,x_destino+3,y_destino+3, pen)
    

    @Slot()
    def limpiar(self):
        self.scene.clear()


    @Slot()
    def mostrar_tabla(self):
        self.ui.tabla.setColumnCount(10)
        headers = ["ID","Origen X","Destino X","Origen Y","Destino Y","Distancia","Velocidad","Red","Green","Blue"]
        self.ui.tabla.setHorizontalHeaderLabels(headers)
        self.ui.tabla.setRowCount(len(self.funciones))

        row = 0

        for particula in self.funciones:
            id_widget = QTableWidgetItem(str(particula.id))
            origenx_widget = QTableWidgetItem(str(particula.origenx))
            destinox_widget = QTableWidgetItem(str(particula.destinox))
            origeny_widget = QTableWidgetItem(str(particula.origeny))
            destinoy_widget = QTableWidgetItem(str(particula.destinoy))
            distancia_widget = QTableWidgetItem(str(particula.distancia))
            velocidad_widget = QTableWidgetItem(str(particula.velocidad))
            red_widget = QTableWidgetItem(str(particula.red))
            green_widget = QTableWidgetItem(str(particula.green))
            blue_widget = QTableWidgetItem(str(particula.blue))

            self.ui.tabla.setItem(row, 0,id_widget)
            self.ui.tabla.setItem(row, 1,origenx_widget)
            self.ui.tabla.setItem(row, 2,destinox_widget)
            self.ui.tabla.setItem(row, 3, origeny_widget)
            self.ui.tabla.setItem(row, 4, destinoy_widget)
            self.ui.tabla.setItem(row, 5,distancia_widget)
            self.ui.tabla.setItem(row, 6,velocidad_widget)
            self.ui.tabla.setItem(row, 7,red_widget)
            self.ui.tabla.setItem(row, 8,green_widget)
            self.ui.tabla.setItem(row, 9,blue_widget)

            row += 1

    @Slot()
    def buscar_id(self):
        id = self.ui.buscar_lineEdit.text()

        encontrado = False
        for particula in self.funciones:
            if id == particula.id:
                self.ui.tabla.clear()
                headers = ["ID","Origen X","Destino X","Origen Y","Destino Y","Distancia","Velocidad","Red","Green","Blue"]
                self.ui.tabla.setHorizontalHeaderLabels(headers)
                self.ui.tabla.setRowCount(1)

                id_widget = QTableWidgetItem(str(particula.id))
                origenx_widget = QTableWidgetItem(str(particula.origenx))
                destinox_widget = QTableWidgetItem(str(particula.destinox))
                origeny_widget = QTableWidgetItem(str(particula.origeny))
                destinoy_widget = QTableWidgetItem(str(particula.destinoy))
                distancia_widget = QTableWidgetItem(str(particula.distancia))
                velocidad_widget = QTableWidgetItem(str(particula.velocidad))
                red_widget = QTableWidgetItem(str(particula.red))
                green_widget = QTableWidgetItem(str(particula.green))
                blue_widget = QTableWidgetItem(str(particula.blue))
                
                self.ui.tabla.setItem(0, 0, id_widget)
                self.ui.tabla.setItem(0, 1, origenx_widget)
                self.ui.tabla.setItem(0, 2, destinox_widget)
                self.ui.tabla.setItem(0, 3, origeny_widget)
                self.ui.tabla.setItem(0, 4, destinoy_widget)
                self.ui.tabla.setItem(0, 5, distancia_widget)
                self.ui.tabla.setItem(0, 6, velocidad_widget)
                self.ui.tabla.setItem(0, 7, red_widget)
                self.ui.tabla.setItem(0, 8, green_widget)
                self.ui.tabla.setItem(0, 9, blue_widget)

                encontrado = True
                return  
        if not encontrado:
            QMessageBox.warning(
                self,
                "Atencion",
                f'La particula con el ID {id} no se encontro'
            )



    @Slot()
    def action_Abrir_Archivo(self):
        #print ("abrir archivo")
        ubicacion = QFileDialog.getOpenFileName(
            self,
            'Abrir Archivo',
            '.',
            'JSON (*.json)'
        )[0]
        self.funciones.abrir(ubicacion)

    @Slot()
    def action_Guardar_Archivo(self):
        #print ("guardar archivo")
        ubicacion = QFileDialog.getSaveFileName(
            self,
            'Guardar Archivo',
            '.',
            'JSON (*.json)'
        )[0]
        print(ubicacion)
        if self.funciones.guardar(ubicacion):
            QMessageBox.information(
                self,
                "Exito",
                "Se pudo crear el archivo" + ubicacion
            )
        else:
            QMessageBox.information(
                self,
                "Error",
                "No se pudo crear el archivo" +ubicacion
            )

    @Slot()
    def inicio(self):#se define un metodo llamado añadir que se mandan llamar
        id=self.ui.Id_spinBox.value()
        DestinoX = self.ui.DestinoX_spinBox.value()#son los datos que se muestran tambien en el designer
        DestinoY = self.ui.DestinoY_spinBox.value()
        OrigenY= self.ui.OrigenY_spinBox.value()
        OrigenX= self.ui.OrigenX_spinBox.value()
        Velocidad = self.ui.Velocidad_spinBox.value()
        Green = self.ui.Green_spinBox.value()
        Red = self.ui.Red_spinBox.value()
        Blue = self.ui.Blue_spinBox.value()
        p = particulas(id, OrigenX, DestinoX,OrigenY, DestinoY, Velocidad, Green,Red,Blue  )
        self.funciones.agregar_inicio(p)#esto me manda el metodo de la clase funciones 
        

    @Slot()
    def final(self):#se define un metodo llamado añadir que se mandan llamar
        id=self.ui.Id_spinBox.value()
        DestinoX = self.ui.DestinoX_spinBox.value()#son los datos que se muestran tambien en el designer
        DestinoY = self.ui.DestinoY_spinBox.value()
        OrigenY= self.ui.OrigenY_spinBox.value()
        OrigenX= self.ui.OrigenX_spinBox.value()
        Velocidad = self.ui.Velocidad_spinBox.value()
        Green = self.ui.Green_spinBox.value()
        Red = self.ui.Red_spinBox.value()
        Blue = self.ui.Blue_spinBox.value()
        p = particulas(id,OrigenX,DestinoX,OrigenY,DestinoY,Velocidad,Green,Red,Blue)
        self.funciones.agregar_final(p)

    @Slot()
    def click_mostrar(self):
        self.ui.plainTextEdit.clear()#elimina las cadenas en el plain text edit
        self.ui.plainTextEdit.insertPlainText(str(self.funciones))

    def wheelEvent(self, event):#este es para hacer zoom
        if event.delta() > 0:
            self.ui.graphicsView.scale(1.2,1.2)
        else:
            self.ui.graphicsView.scale(0.8, 0.8)