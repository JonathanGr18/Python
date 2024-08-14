import sys, time
from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem, QApplication, QGraphicsScene
from PySide2.QtGui import QPen, QColor, QTransform
from PySide2.QtCore import Slot

from Particulas import Ui_MainWindow
from laboratorio import Laboratorio
from ClaseParticula import Particula
from algoritmos import distancia_euclidiana
from algoritmos import puntos_mas_cercanos
from pprint import pprint

class MainWindow(QMainWindow):
    def __init__(self):#Reservar memoria para mostrar ventana
        super(MainWindow, self).__init__()#Llamar a construtor de QMainWindow
        self.laboratorio=Laboratorio()
        self.puntos=[]
        self.grafolista=dict()
        #PRIM
        self.listaVisitados=[]
        self.grafoResultante={}
        self.listaOrdenada=[]

        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        #Pagina 1
        self.ui.btnAgregarFinal.clicked.connect(self.clic_agregarFinal)
        self.ui.btnAgregarInicio.clicked.connect(self.clic_agregarInicio)
        self.ui.btnMostrar.clicked.connect(self.clic_mostrar)
        self.ui.btnOrdIDPlain.clicked.connect(self.clic_ordenarID)
        self.ui.btnOrdDistPlain.clicked.connect(self.clic_ordenarDist)
        self.ui.btnOrdVelPlain.clicked.connect(self.clic_ordenarVel)
        self.ui.btnLimpiar.clicked.connect(self.clic_limpiar)
        #Grafos
        self.ui.btnKruskal.clicked.connect(self.clic_kruskal)
        self.ui.btnDijkstra.clicked.connect(self.clic_dijkstra)
        self.ui.btnPrim.clicked.connect(self.clic_prim)
        self.ui.btnGrafo.clicked.connect(self.clic_grafo)
        self.grafo=QGraphicsScene()
        self.ui.gpvGraficaGrafos.setScene(self.grafo)
        #Pagina 2
        self.ui.btnMostrarTabla.clicked.connect(self.clic_mostrarTabla)
        self.ui.btnBuscarTabla.clicked.connect(self.clic_buscarIdTabla)
        #Pagina 3
        self.ui.btnMostrarGrafica.clicked.connect(self.clic_mostrarGrafica)
        self.ui.btnLimpiarGrafica.clicked.connect(self.clic_limpiarGrafica)
        self.ui.btnMostrarPuntos.clicked.connect(self.clic_dibujarPuntos)
        self.ui.btnPuntosSercanos.clicked.connect(self.clic_puntosSercanos)
        self.scene=QGraphicsScene() #Scene es un objeto de tipo QGraphicsView
        self.ui.gpvGrafica.setScene(self.scene)
        #Opciones menu
        self.ui.actionAbrir.triggered.connect(self.action_Abrir)
        self.ui.actionGuardar.triggered.connect(self.action_Guardar)

        self.ui.txtOrigenX.setText("0")
        self.ui.txtOrigenY.setText("100")
        self.ui.txtDestinoX.setText("400")
        self.ui.txtDesitnoY.setText("200")
    
    @Slot()
    def clic_limpiar(self):
        self.listaVisitados.clear()
        self.grafoResultante.clear()
        self.listaOrdenada.clear()
        self.ui.ptxMostrar.clear()
        self.grafo.clear()
    
    @Slot()
    def clic_kruskal(self):
        pass

    @Slot()
    def clic_dijkstra(self):
        self.clic_grafo()
        x=int(self.ui.txtOrigenX.text())
        y=int(self.ui.txtOrigenY.text())
        origen=(x,y) #Obtener llave 

        # Inicialización de las estructuras de datos
        distancia = {nodo: float('inf') for nodo in self.grafolista}  # Distancia inicial infinita para todos los nodos
        distancia[origen] = 0  # Distancia cero para el nodo de inicio
        print(distancia)
        visitados = set()  # Conjunto de nodos visitados
        print(self.grafolista)
        while len(visitados) < len(self.grafolista):
            # Encuentra el nodo con la distancia mínima que no ha sido visitado
            min_distancia = float('inf')
            min_nodo = None
            for nodo in self.grafolista:
                print("NODO:",nodo)
                if nodo not in visitados and distancia[nodo] < min_distancia:
                    min_distancia = distancia[nodo]
                    print("MIN_DIST:",min_distancia)
                    min_nodo = nodo
                    print("MIN_NODO:",min_nodo)
                    print("DISTANCIA[NODO]:",distancia[nodo])

            # Marcar el nodo mínimo como visitado
            visitados.add(min_nodo)
            print("VISITADOS:",visitados)
            # Actualizar las distancias de los nodos vecinos no visitados
            for neighbor,distancia in self.grafolista[min_nodo]:
                print("NEIGHBOR:",neighbor)
                print("SELF.GRAFOLISTA[min-nodo]:",self.grafolista[min_nodo])
                distancia[neighbor] = min(distancia[neighbor], distancia[min_nodo] + self.grafolista[min_nodo][neighbor])
                print("DISTANCIA[EIGHBOR]:",distancia[neighbor])

        print(distancia)
    
    @Slot()
    def clic_prim(self):
        self.clic_grafo()#Cargar lista grafo
        x=int(self.ui.txtOrigenX.text())
        y=int(self.ui.txtOrigenY.text())
        origenp=(x,y) #Obtener llave 
        #Agregar a lista de visitados
        self.listaVisitados.append(origenp)
        #Agregar Adyacentes a lista ordenada
        for destino, distancia in self.grafolista[origenp]:
            self.listaOrdenada.append((origenp,destino, distancia))
        #Ordenar lista por la distancia
        pos=0;act=0; Aux=[]
        for i in range(len(self.listaOrdenada)):
            Aux=self.listaOrdenada[i]
            act=self.listaOrdenada[i][2]
            pos=i
            while pos>0 and self.listaOrdenada[pos-1][2]>act:
                self.listaOrdenada[pos]=self.listaOrdenada[pos-1]
                pos=pos-1
            self.listaOrdenada[pos]=Aux

        while self.listaOrdenada:#Hacer mientras no este vacia
            vertice=self.listaOrdenada.pop(0)#Eliminar el vertice
            x=vertice[1]
            #Si el destino no esta en la lista de visitados
            if x not in self.listaVisitados:
                #Agregar a lista de visitados en nodo destino
                self.listaVisitados.append(x)
                #Agregar a lista ordenada los adyacentes del nodo destino
                #'x' no han sido visitados
                for key, lista in self.grafolista[x]:
                    if key not in self.listaVisitados:
                        self.listaOrdenada.append((x,key,lista))
                #Ordenar lista 
                self.listaOrdenada=[(c,a,b) for a,b,c in self.listaOrdenada]
                self.listaOrdenada.sort()
                self.listaOrdenada=[(a,b,c) for c,a,b in self.listaOrdenada]
                #Agregar vertice al grafo resultante
                origen=vertice[0]#valor del nodo origen
                destino=vertice[1]#Nodo destino
                peso=vertice[2]#Peso de la arista entre los dos nodos
                #Agregar estos valores al grafo
                if origen in self.grafoResultante:
                    if destino in self.grafoResultante:
                        lista=self.grafoResultante[origen]
                        self.grafoResultante[origen]=lista+[(destino, peso)]
                        lista=self.grafoResultante[destino]
                        lista.append((origen,peso))
                        self.grafoResultante[destino]=lista
                    else:
                        self.grafoResultante[destino]=[(origen,peso)]
                        lista=self.grafoResultante[origen]
                        lista.append((destino,peso))
                        self.grafoResultante[origen]=lista
                elif destino in self.grafoResultante:
                    self.grafoResultante[origen]=[(destino, peso)]
                    lista=self.grafoResultante[destino]
                    lista.append((origen,peso))
                    self.grafoResultante[destino]=lista
                else:
                    self.grafoResultante[destino]=[(origen,peso)]
                    self.grafoResultante[origen]=[(destino,peso)]

        self.grafo.clear()
        for key, lista in self.grafoResultante.items():
            for i,y in lista:
                print(i,y)
                self.grafo.addEllipse(i[0], i[1], 6, 6)#Cordenadas(2), Tamaños(2)
                self.grafo.addLine(key[0]+3, key[1]+3, i[0]+3, i[1]+3)#+3 es el margen
                         

        self.ui.ptxMostrar.clear()
        i=0
        for key, lista in self.grafoResultante.items():
            i+=1
            self.ui.ptxMostrar.insertPlainText("\nConexion #"+str(i)+":\n")
            self.ui.ptxMostrar.insertPlainText(str(key)+":")
            self.ui.ptxMostrar.insertPlainText(str(lista))

    @Slot()
    def clic_grafo(self):
        self.grafolista.clear()
        self.ui.ptxMostrar.clear()
        pen=QPen()#Definir Lapiz
        pen.setWidth(2)#Anchura del lapiz

        for particulas in self.laboratorio: 
            #Mostrar en grafica
            color=QColor(particulas.fred,particulas.fgreen,particulas.fblue)#Definir color
            pen.setColor(color)#Color de objetos
            self.grafo.addEllipse(particulas.forigenX, particulas.forigenY, 6, 6,pen)#Cordenadas(2), Tamaños(2)
            self.grafo.addEllipse(particulas.fdestinoX,particulas.fdestinoY, 6, 6,pen)
            self.grafo.addLine(particulas.forigenX+3, particulas.forigenY+3, particulas.fdestinoX+3, particulas.fdestinoY+3,pen)#+3 es el margen


            key=(particulas.forigenX, particulas.forigenY)#key origen
            key2=(particulas.fdestinoX, particulas.fdestinoY)#Key destino

            value=(key2),int(particulas.fdistancia)#Value destinos [(cord,cord),distancia]
            value2=(key),int(particulas.fdistancia)#Value Origen [(cord,cord),distancia]
            #Lista de adyacensia
            if key in self.grafolista:#Origen key
                self.grafolista[key].append(value)
            else:
                self.grafolista[key]=[value]

            if key2 in self.grafolista:#Destino key
                self.grafolista[key2].append(value2)
            else:
                self.grafolista[key2]=[value2]

        #Mostrar en PLainText
        i=0
        for key, value in self.grafolista.items():
            i+=1
            self.ui.ptxMostrar.insertPlainText("\nLLAVE #"+str(i)+":\n")
            self.ui.ptxMostrar.insertPlainText(str(key)+":")
            self.ui.ptxMostrar.insertPlainText(str(value))

    
    @Slot()
    def clic_dibujarPuntos(self):
        self.clic_limpiarGrafica()
        pen=QPen()
        pen.setWidth(5)
        for particula in self.laboratorio:
            xo=particula.forigenX
            yo=particula.forigenY
            xd=particula.fdestinoX
            yd=particula.fdestinoY
            punto=(particula.forigenX,particula.forigenY)
            punto2=(particula.fdestinoX,particula.fdestinoY)
            self.puntos.append(punto)
            self.puntos.append(punto2)
            color = QColor(particula.fred, particula.fgreen, particula.fblue)
            pen.setColor(color)
            self.scene.addEllipse(particula.forigenX, particula.forigenY, 6, 6, pen)
            self.scene.addEllipse(particula.fdestinoX, particula.fdestinoY, 6, 6,pen)
    
    @Slot()
    def clic_puntosSercanos(self):
        self.clic_dibujarPuntos()
        resultado = puntos_mas_cercanos(self.puntos)
        
        for punto1, punto2 in resultado:
            x1=punto1[0]
            y1=punto1[1]
            x2=punto2[0]
            y2=punto2[1]
            self.scene.addLine(x1+3, y1+3, x2+3, y2+3)
    
    @Slot()
    def clic_ordenarID(self):#Ascendente
        self.laboratorio.ordID()
        self.clic_mostrar()

    @Slot()
    def clic_ordenarDist(self):#Descedente
        self.laboratorio.ordDist()
        self.clic_mostrar()

    @Slot()
    def clic_ordenarVel(self):#Ascendente
        self.laboratorio.ordVel()
        self.clic_mostrar()

    @Slot()
    def clic_mostrarGrafica(self):
        pen=QPen()#Definir Lapiz
        pen.setWidth(2)#Anchura del lapiz

        for particulas in self.laboratorio: 
            color=QColor(particulas.fred,particulas.fgreen,particulas.fblue)#Definir color
            pen.setColor(color)#Color de objetos

            x_origen=particulas.forigenX #Obtener dato
            y_origen=particulas.forigenY
            x_destino=particulas.fdestinoX
            y_destino=particulas.fdestinoY

            self.scene.addEllipse(x_origen, y_origen, 6, 6,pen)#Cordenadas(2), Tamaños(2)
            self.scene.addEllipse(x_destino,y_destino, 6, 6,pen)
            self.scene.addLine(x_origen+3, y_origen+3, x_destino+3, y_destino+3,pen)#+3 es el margen
    
    def wheelEvent(self, event):
        if event.delta()>0:
            self.ui.gpvGrafica.scale(1.2, 1.2)#Aumento de 20%
        else:
            self.ui.gpvGrafica.scale(0.8, 0.8)#Decremento de 20%

    @Slot()
    def clic_limpiarGrafica(self):
        self.scene.clear()

    @Slot()#Verificacion si hay un click o cambio
    def clic_agregarFinal(self):
        id=self.ui.txtId.text()
        origenX=self.ui.spxOrigenX.value()
        origenY=self.ui.spxOrigenY.value()
        destinoX=self.ui.spxDestinoX.value() #sacar la informacion del widget, text() lo regresa en forma de string
        destinoY=self.ui.spxDestinoY.value()
        velocidad=self.ui.spxVelocidad.value()
        red=self.ui.spxRed.value()#Regresa en forma de entero
        green=self.ui.spxGreen.value()
        blue=self.ui.spxBlue.value()#Los rangos de spinBox se pueden limitar en el Designer
        #Limpiar despues de agregar
        self.ui.txtId.clear()
        self.ui.spxOrigenX.clear()
        self.ui.spxOrigenY.clear()
        self.ui.spxDestinoX.clear()     
        self.ui.spxDestinoY.clear()
        self.ui.spxVelocidad.clear()
        self.ui.spxRed.clear()
        self.ui.spxGreen.clear()
        self.ui.spxBlue.clear()

        particulas= Particula(id,origenX,origenY,destinoX,destinoY,velocidad,red,green,blue)
        self.laboratorio.agregarFinal(particulas)
    @Slot()    
    def clic_agregarInicio(self):
        id=self.ui.txtId.text()
        origenX=self.ui.spxOrigenX.value()
        origenY=self.ui.spxOrigenY.value()
        destinoX=self.ui.spxDestinoX.value() #sacar la informacion del widget, text() lo regresa en forma de string
        destinoY=self.ui.spxDestinoY.value()
        velocidad=self.ui.spxVelocidad.value()
        red=self.ui.spxRed.value()#Regresa en forma de entero
        green=self.ui.spxGreen.value()
        blue=self.ui.spxBlue.value()
        #Limpiar despues de agregar
        self.ui.txtId.clear()
        self.ui.spxOrigenX.clear()
        self.ui.spxOrigenY.clear()
        self.ui.spxDestinoX.clear()     
        self.ui.spxDestinoY.clear()
        self.ui.spxVelocidad.clear()
        self.ui.spxRed.clear()
        self.ui.spxGreen.clear()
        self.ui.spxBlue.clear()

        particulas= Particula(id,origenX,origenY,destinoX,destinoY,velocidad,red,green,blue)
        self.laboratorio.agregarInicio(particulas)

    @Slot()
    def clic_mostrar(self):
        self.ui.ptxMostrar.clear()
        self.ui.ptxMostrar.insertPlainText("=======PARTICULAS=======\n"+str(self.laboratorio))
    
    @Slot()
    def clic_mostrarTabla(self):
        self.ui.tbwTabla.setColumnCount(10)#Cantidad de columnas
        headers=["ID","Origen[X]","Origen[Y]","Destino[X]","Destino[Y]","Velocidad","Red","Green","Blue","Distancia"]#Nombre de columnas
        self.ui.tbwTabla.setHorizontalHeaderLabels(headers)#Mostrar Nombre

        self.ui.tbwTabla.setRowCount(len(self.laboratorio))#crear filas en tabla

        row=0
        for particulas in self.laboratorio:
            id_widget=QTableWidgetItem(particulas.fid)
            origenx_widget=QTableWidgetItem(str(particulas.forigenX))
            origeny_widget=QTableWidgetItem(str(particulas.forigenY))
            destinox_widget=QTableWidgetItem(str(particulas.fdestinoX))
            destinoy_widget=QTableWidgetItem(str(particulas.fdestinoY))
            velocidad_widget=QTableWidgetItem(str(particulas.fvelocidad))
            red_widget=QTableWidgetItem(str(particulas.fred))
            green_widget=QTableWidgetItem(str(particulas.fgreen))
            blue_widget=QTableWidgetItem(str(particulas.fblue))
            distancia_widget=QTableWidgetItem(str(particulas.fdistancia))

            self.ui.tbwTabla.setItem(row,0,id_widget)
            self.ui.tbwTabla.setItem(row,1,origenx_widget)
            self.ui.tbwTabla.setItem(row,2,origeny_widget)
            self.ui.tbwTabla.setItem(row,3,destinox_widget)
            self.ui.tbwTabla.setItem(row,4,destinoy_widget)
            self.ui.tbwTabla.setItem(row,5,velocidad_widget)
            self.ui.tbwTabla.setItem(row,6,red_widget)
            self.ui.tbwTabla.setItem(row,7,green_widget)
            self.ui.tbwTabla.setItem(row,8,blue_widget)
            self.ui.tbwTabla.setItem(row,9,distancia_widget)
            row+=1

    @Slot()
    def clic_buscarIdTabla(self):
        id=self.ui.txtBuscarTabla.text()

        encontrado=False
        for particulas in self.laboratorio:
            if id==particulas.fid:
                self.ui.tbwTabla.clear()
                self.ui.tbwTabla.setColumnCount(10)#Cantidad de columnas
                headers=["ID","Origen[X]","Origen[Y]","Destino[X]","Destino[Y]","Velocidad","Red","Green","Blue","Distancia"]#Nombre de columnas
                self.ui.tbwTabla.setHorizontalHeaderLabels(headers)#Mostrar Nombre
                self.ui.tbwTabla.setRowCount(1)
                

                id_widget=QTableWidgetItem(particulas.fid)
                origenx_widget=QTableWidgetItem(str(particulas.forigenX))
                origeny_widget=QTableWidgetItem(str(particulas.forigenY))
                destinox_widget=QTableWidgetItem(str(particulas.fdestinoX))
                destinoy_widget=QTableWidgetItem(str(particulas.fdestinoY))
                velocidad_widget=QTableWidgetItem(str(particulas.fvelocidad))
                red_widget=QTableWidgetItem(str(particulas.fred))
                green_widget=QTableWidgetItem(str(particulas.fgreen))
                blue_widget=QTableWidgetItem(str(particulas.fblue))
                distancia_widget=QTableWidgetItem(str(particulas.fdistancia))

                self.ui.tbwTabla.setItem(0,0,id_widget)
                self.ui.tbwTabla.setItem(0,1,origenx_widget)
                self.ui.tbwTabla.setItem(0,2,origeny_widget)
                self.ui.tbwTabla.setItem(0,3,destinox_widget)
                self.ui.tbwTabla.setItem(0,4,destinoy_widget)
                self.ui.tbwTabla.setItem(0,5,velocidad_widget)
                self.ui.tbwTabla.setItem(0,6,red_widget)
                self.ui.tbwTabla.setItem(0,7,green_widget)
                self.ui.tbwTabla.setItem(0,8,blue_widget)
                self.ui.tbwTabla.setItem(0,9,distancia_widget)
                encontrado=True
                return
        if not encontrado:
            QMessageBox.warning(self, "Atencion", f'La Particula con el identificador "(ID)" no fue encontrado')

    @Slot()
    def action_Abrir(self):
       #print("Guardar Archivo")
        ubicacion=QFileDialog.getOpenFileName(
            self,
            'Abrir Archivo',
            '.',
            'JSON(*.json)'
        )[0]
        if self.laboratorio.abrirArchivo(ubicacion):
            QMessageBox.information(
                self,
                "Exito",
                "Se pudo abrir el archivo " + ubicacion
            )
        else:
            QMessageBox.information(
                self, 
                "Error", 
                "No se pudo abrir el archivo "+ ubicacion
            )
    @Slot()
    def action_Guardar(self):
        ubicacion=QFileDialog.getSaveFileName(
            self,
            'Guardar Archivo',
            '.',
            'JSON(*.json)'
        )[0]
        print(ubicacion)
        if self.laboratorio.guardarArchivo(ubicacion):
            QMessageBox.information(
                self,
                "Exito",
                "Se pudo crear el archivo " + ubicacion
            )
        else:
            QMessageBox.information(
                self, 
                "Error", 
                "No se pudo crear el archivo "+ ubicacion
            )

if __name__=='__main__':
    #Aplicacion de QT
    app=QApplication()
    #Se crea una ventana con la palabra hola
    window=MainWindow()
    #Se hace visible la ventana
    window.show() 
    #Qt loop
    sys.exit(app.exec_())