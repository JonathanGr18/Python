# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Particulas.ui'
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
        MainWindow.resize(918, 814)
        MainWindow.setAnimated(True)
        self.actionAbrir = QAction(MainWindow)
        self.actionAbrir.setObjectName(u"actionAbrir")
        self.actionGuardar = QAction(MainWindow)
        self.actionGuardar.setObjectName(u"actionGuardar")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(40, 30, 791, 731))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gbxVuelo = QGroupBox(self.tab)
        self.gbxVuelo.setObjectName(u"gbxVuelo")
        self.gbxVuelo.setGeometry(QRect(0, 10, 271, 281))
        self.spxVelocidad = QSpinBox(self.gbxVuelo)
        self.spxVelocidad.setObjectName(u"spxVelocidad")
        self.spxVelocidad.setGeometry(QRect(110, 210, 81, 20))
        self.spxVelocidad.setMaximum(250)
        self.spxVelocidad.setSingleStep(25)
        self.btnAgregarInicio = QPushButton(self.gbxVuelo)
        self.btnAgregarInicio.setObjectName(u"btnAgregarInicio")
        self.btnAgregarInicio.setGeometry(QRect(30, 240, 93, 28))
        self.lblId = QLabel(self.gbxVuelo)
        self.lblId.setObjectName(u"lblId")
        self.lblId.setGeometry(QRect(50, 20, 41, 16))
        self.txtId = QLineEdit(self.gbxVuelo)
        self.txtId.setObjectName(u"txtId")
        self.txtId.setGeometry(QRect(90, 20, 120, 20))
        self.lblVelocidad = QLabel(self.gbxVuelo)
        self.lblVelocidad.setObjectName(u"lblVelocidad")
        self.lblVelocidad.setGeometry(QRect(50, 210, 47, 12))
        self.groupBox = QGroupBox(self.gbxVuelo)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(12, 51, 111, 91))
        self.formLayout_2 = QFormLayout(self.groupBox)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.lblOrigenX = QLabel(self.groupBox)
        self.lblOrigenX.setObjectName(u"lblOrigenX")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.lblOrigenX)

        self.spxOrigenX = QSpinBox(self.groupBox)
        self.spxOrigenX.setObjectName(u"spxOrigenX")
        self.spxOrigenX.setMaximum(500)
        self.spxOrigenX.setSingleStep(25)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.spxOrigenX)

        self.lblOrigenY = QLabel(self.groupBox)
        self.lblOrigenY.setObjectName(u"lblOrigenY")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.lblOrigenY)

        self.spxOrigenY = QSpinBox(self.groupBox)
        self.spxOrigenY.setObjectName(u"spxOrigenY")
        self.spxOrigenY.setMaximum(500)
        self.spxOrigenY.setSingleStep(25)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.spxOrigenY)

        self.groupBox_3 = QGroupBox(self.gbxVuelo)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(10, 140, 251, 56))
        self.gridLayout_6 = QGridLayout(self.groupBox_3)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.spxRed = QSpinBox(self.groupBox_3)
        self.spxRed.setObjectName(u"spxRed")
        self.spxRed.setMaximum(255)
        self.spxRed.setSingleStep(25)

        self.gridLayout_6.addWidget(self.spxRed, 0, 1, 1, 1)

        self.lblGreen = QLabel(self.groupBox_3)
        self.lblGreen.setObjectName(u"lblGreen")

        self.gridLayout_6.addWidget(self.lblGreen, 0, 2, 1, 1)

        self.lblBue = QLabel(self.groupBox_3)
        self.lblBue.setObjectName(u"lblBue")

        self.gridLayout_6.addWidget(self.lblBue, 0, 4, 1, 1)

        self.spxBlue = QSpinBox(self.groupBox_3)
        self.spxBlue.setObjectName(u"spxBlue")
        self.spxBlue.setMaximum(255)
        self.spxBlue.setSingleStep(25)

        self.gridLayout_6.addWidget(self.spxBlue, 0, 5, 1, 1)

        self.spxGreen = QSpinBox(self.groupBox_3)
        self.spxGreen.setObjectName(u"spxGreen")
        self.spxGreen.setMaximum(255)
        self.spxGreen.setSingleStep(25)

        self.gridLayout_6.addWidget(self.spxGreen, 0, 3, 1, 1)

        self.lblRed = QLabel(self.groupBox_3)
        self.lblRed.setObjectName(u"lblRed")

        self.gridLayout_6.addWidget(self.lblRed, 0, 0, 1, 1)

        self.groupBox_2 = QGroupBox(self.gbxVuelo)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(150, 50, 111, 91))
        self.formLayout = QFormLayout(self.groupBox_2)
        self.formLayout.setObjectName(u"formLayout")
        self.lblDestinoY = QLabel(self.groupBox_2)
        self.lblDestinoY.setObjectName(u"lblDestinoY")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.lblDestinoY)

        self.lblDestinoX = QLabel(self.groupBox_2)
        self.lblDestinoX.setObjectName(u"lblDestinoX")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.lblDestinoX)

        self.spxDestinoY = QSpinBox(self.groupBox_2)
        self.spxDestinoY.setObjectName(u"spxDestinoY")
        self.spxDestinoY.setMaximum(500)
        self.spxDestinoY.setSingleStep(25)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.spxDestinoY)

        self.spxDestinoX = QSpinBox(self.groupBox_2)
        self.spxDestinoX.setObjectName(u"spxDestinoX")
        self.spxDestinoX.setMaximum(500)
        self.spxDestinoX.setSingleStep(25)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.spxDestinoX)

        self.btnAgregarFinal = QPushButton(self.gbxVuelo)
        self.btnAgregarFinal.setObjectName(u"btnAgregarFinal")
        self.btnAgregarFinal.setGeometry(QRect(150, 240, 93, 28))
        self.groupBox_4 = QGroupBox(self.tab)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(0, 290, 271, 411))
        self.gridLayout_7 = QGridLayout(self.groupBox_4)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.ptxMostrar = QPlainTextEdit(self.groupBox_4)
        self.ptxMostrar.setObjectName(u"ptxMostrar")

        self.gridLayout_7.addWidget(self.ptxMostrar, 0, 0, 1, 3)

        self.btnMostrar = QPushButton(self.groupBox_4)
        self.btnMostrar.setObjectName(u"btnMostrar")

        self.gridLayout_7.addWidget(self.btnMostrar, 1, 0, 1, 3)

        self.btnOrdVelPlain = QPushButton(self.groupBox_4)
        self.btnOrdVelPlain.setObjectName(u"btnOrdVelPlain")

        self.gridLayout_7.addWidget(self.btnOrdVelPlain, 2, 0, 1, 3)

        self.btnOrdDistPlain = QPushButton(self.groupBox_4)
        self.btnOrdDistPlain.setObjectName(u"btnOrdDistPlain")

        self.gridLayout_7.addWidget(self.btnOrdDistPlain, 3, 0, 1, 3)

        self.btnOrdIDPlain = QPushButton(self.groupBox_4)
        self.btnOrdIDPlain.setObjectName(u"btnOrdIDPlain")

        self.gridLayout_7.addWidget(self.btnOrdIDPlain, 4, 0, 1, 3)

        self.gpvGraficaGrafos = QGraphicsView(self.tab)
        self.gpvGraficaGrafos.setObjectName(u"gpvGraficaGrafos")
        self.gpvGraficaGrafos.setGeometry(QRect(280, 110, 491, 401))
        self.btnGrafo = QPushButton(self.tab)
        self.btnGrafo.setObjectName(u"btnGrafo")
        self.btnGrafo.setGeometry(QRect(280, 520, 93, 28))
        self.btnKruskal = QPushButton(self.tab)
        self.btnKruskal.setObjectName(u"btnKruskal")
        self.btnKruskal.setGeometry(QRect(410, 520, 93, 28))
        self.btnDijkstra = QPushButton(self.tab)
        self.btnDijkstra.setObjectName(u"btnDijkstra")
        self.btnDijkstra.setGeometry(QRect(540, 520, 93, 28))
        self.btnPrim = QPushButton(self.tab)
        self.btnPrim.setObjectName(u"btnPrim")
        self.btnPrim.setGeometry(QRect(670, 520, 93, 28))
        self.txtOrigenX = QLineEdit(self.tab)
        self.txtOrigenX.setObjectName(u"txtOrigenX")
        self.txtOrigenX.setGeometry(QRect(460, 560, 113, 22))
        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(320, 560, 130, 16))
        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(320, 590, 130, 16))
        self.txtOrigenY = QLineEdit(self.tab)
        self.txtOrigenY.setObjectName(u"txtOrigenY")
        self.txtOrigenY.setGeometry(QRect(460, 590, 113, 22))
        self.btnLimpiar = QPushButton(self.tab)
        self.btnLimpiar.setObjectName(u"btnLimpiar")
        self.btnLimpiar.setGeometry(QRect(670, 560, 93, 28))
        self.label_3 = QLabel(self.tab)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(320, 646, 130, 20))
        self.label_4 = QLabel(self.tab)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(320, 620, 130, 16))
        self.txtDesitnoY = QLineEdit(self.tab)
        self.txtDesitnoY.setObjectName(u"txtDesitnoY")
        self.txtDesitnoY.setGeometry(QRect(460, 650, 113, 22))
        self.txtDestinoX = QLineEdit(self.tab)
        self.txtDestinoX.setObjectName(u"txtDestinoX")
        self.txtDestinoX.setGeometry(QRect(460, 620, 113, 22))
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_3 = QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.txtBuscarTabla = QLineEdit(self.tab_2)
        self.txtBuscarTabla.setObjectName(u"txtBuscarTabla")
        self.txtBuscarTabla.setDragEnabled(True)

        self.gridLayout_3.addWidget(self.txtBuscarTabla, 1, 0, 1, 1)

        self.btnMostrarTabla = QPushButton(self.tab_2)
        self.btnMostrarTabla.setObjectName(u"btnMostrarTabla")

        self.gridLayout_3.addWidget(self.btnMostrarTabla, 1, 3, 1, 1)

        self.btnBuscarTabla = QPushButton(self.tab_2)
        self.btnBuscarTabla.setObjectName(u"btnBuscarTabla")

        self.gridLayout_3.addWidget(self.btnBuscarTabla, 1, 2, 1, 1)

        self.tbwTabla = QTableWidget(self.tab_2)
        self.tbwTabla.setObjectName(u"tbwTabla")

        self.gridLayout_3.addWidget(self.tbwTabla, 0, 0, 1, 5)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_4 = QGridLayout(self.tab_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.btnLimpiarGrafica = QPushButton(self.tab_3)
        self.btnLimpiarGrafica.setObjectName(u"btnLimpiarGrafica")

        self.gridLayout_4.addWidget(self.btnLimpiarGrafica, 1, 3, 1, 1)

        self.btnMostrarGrafica = QPushButton(self.tab_3)
        self.btnMostrarGrafica.setObjectName(u"btnMostrarGrafica")

        self.gridLayout_4.addWidget(self.btnMostrarGrafica, 1, 0, 1, 1)

        self.btnMostrarPuntos = QPushButton(self.tab_3)
        self.btnMostrarPuntos.setObjectName(u"btnMostrarPuntos")

        self.gridLayout_4.addWidget(self.btnMostrarPuntos, 1, 1, 1, 1)

        self.gpvGrafica = QGraphicsView(self.tab_3)
        self.gpvGrafica.setObjectName(u"gpvGrafica")

        self.gridLayout_4.addWidget(self.gpvGrafica, 0, 0, 1, 4)

        self.btnPuntosSercanos = QPushButton(self.tab_3)
        self.btnPuntosSercanos.setObjectName(u"btnPuntosSercanos")

        self.gridLayout_4.addWidget(self.btnPuntosSercanos, 1, 2, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 918, 26))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menuArchivo.addAction(self.actionAbrir)
        self.menuArchivo.addAction(self.actionGuardar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Actividad #Grafos", None))
        self.actionAbrir.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
#if QT_CONFIG(shortcut)
        self.actionAbrir.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionGuardar.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
#if QT_CONFIG(shortcut)
        self.actionGuardar.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.gbxVuelo.setTitle(QCoreApplication.translate("MainWindow", u"Particulas", None))
        self.btnAgregarInicio.setText(QCoreApplication.translate("MainWindow", u"Agregar Inicio", None))
        self.lblId.setText(QCoreApplication.translate("MainWindow", u"ID:", None))
        self.lblVelocidad.setText(QCoreApplication.translate("MainWindow", u"Velocidad:", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Origen:", None))
        self.lblOrigenX.setText(QCoreApplication.translate("MainWindow", u"X:", None))
        self.lblOrigenY.setText(QCoreApplication.translate("MainWindow", u"Y:", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Color", None))
        self.lblGreen.setText(QCoreApplication.translate("MainWindow", u"Green:", None))
        self.lblBue.setText(QCoreApplication.translate("MainWindow", u"Blue:", None))
        self.lblRed.setText(QCoreApplication.translate("MainWindow", u"Red:", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Destino:", None))
        self.lblDestinoY.setText(QCoreApplication.translate("MainWindow", u"Y:", None))
        self.lblDestinoX.setText(QCoreApplication.translate("MainWindow", u"X:", None))
        self.btnAgregarFinal.setText(QCoreApplication.translate("MainWindow", u"Agregar Final", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Salida:", None))
        self.btnMostrar.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.btnOrdVelPlain.setText(QCoreApplication.translate("MainWindow", u"Ordenar Velocidad", None))
        self.btnOrdDistPlain.setText(QCoreApplication.translate("MainWindow", u"Ordenar Distancia", None))
        self.btnOrdIDPlain.setText(QCoreApplication.translate("MainWindow", u"Ordenar ID", None))
        self.btnGrafo.setText(QCoreApplication.translate("MainWindow", u"Grafo", None))
        self.btnKruskal.setText(QCoreApplication.translate("MainWindow", u"Kruskal", None))
        self.btnDijkstra.setText(QCoreApplication.translate("MainWindow", u"Dijkstra", None))
        self.btnPrim.setText(QCoreApplication.translate("MainWindow", u"Prim", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Origen X (Llave):", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Origen Y (Llave):", None))
        self.btnLimpiar.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Destino Y (Llave):", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Destino X (Llave):", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.txtBuscarTabla.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ID de Particula", None))
        self.btnMostrarTabla.setText(QCoreApplication.translate("MainWindow", u"Mostrar Particulas ", None))
        self.btnBuscarTabla.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Mostrar/Buscar", None))
        self.btnLimpiarGrafica.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.btnMostrarGrafica.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.btnMostrarPuntos.setText(QCoreApplication.translate("MainWindow", u"Mostrar Solo Puntos", None))
        self.btnPuntosSercanos.setText(QCoreApplication.translate("MainWindow", u"Puntos Sercanos", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Dibujar Particulas", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
    # retranslateUi

