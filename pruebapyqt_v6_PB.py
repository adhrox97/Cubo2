import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtGui, QtWidgets, uic
import cv2

lista=''
ventanta=0

class VentanaPrincipal(QMainWindow):

    def __init__(self, parent=None):
        super(VentanaPrincipal, self).__init__(parent)
        loadUi('ventanaprin2pruebaPB.ui', self)
        self.b_asignaturas.clicked.connect(self.abrirVentanaMaterias)

    def abrirVentanaMaterias(self):

        self.close()
        otraventana=VentanaMaterias(self)
        otraventana.show()
        
class VentanaMaterias(QMainWindow):

    def __init__(self, parent=None):

        super(VentanaMaterias, self).__init__(parent)

        self.MainWindow=loadUi('ventanaAsignaturasPB.ui', self)

        self.botonreturn.clicked.connect(self.abrirVentanaPrincipal)

        self.b_matematica.clicked.connect(self.abrirVentanaMatematica)

        self.b_ciencia.clicked.connect(self.abrirVentanaCiencia)

        self.b_lenguaje.clicked.connect(self.abrirVentanaLenguaje)

        self.b_artistica.clicked.connect(self.abrirVentanaArtistica)


    # def Respuestas(self):

    #     global lista
    #     lista='materias/Respuestas/Respuestas.txt'
    #     self.abrirVentanaAsignatura()

    def abrirVentanaPrincipal(self):

        self.close()
        otraventana=VentanaPrincipal(self)
        otraventana.show()

    def abrirVentanaMatematica(self):

        self.close()
        otraventana=VentanaMatematica(self)
        otraventana.show()

    def abrirVentanaCiencia(self):

        self.close()
        otraventana=VentanaCiencia(self)
        otraventana.show()

    def abrirVentanaLenguaje(self):

        self.close()
        otraventana=VentanaLenguaje(self)
        otraventana.show()

    def abrirVentanaArtistica(self):

        self.close()
        otraventana=VentanaArtistica(self)
        otraventana.show()

    # def abrirVentanaAsignatura(self):

    #     self.close()
    #     otraventana=VentanaAsignatura(self)
    #     otraventana.show()

class VentanaMatematica(QMainWindow):

    def __init__(self, parent=None):

        super(VentanaMatematica, self).__init__(parent)

        self.MainWindow=loadUi('matematicaT.ui', self)

        self.b_matematicas1.clicked.connect(self.Matematicas1)

        self.b_matematicas2.clicked.connect(self.Matematicas2)

        self.botonreturn.clicked.connect(self.abrirVentanaMaterias)
                    
                    
    def Matematicas1(self):

        global lista
        global ventana
        ventana=VentanaMatematica(self)
        lista='materias/Matematicas1/Matematicas1.txt'        
        self.abrirVentanaAsignatura()

    def Matematicas2(self):
        
        global lista
        global ventana
        ventana=VentanaMatematica(self)
        lista='materias/Matematicas2/Matematicas2.txt'
        self.abrirVentanaAsignatura()

    def Respuestas(self):

        global lista
        global ventana
        ventana=VentanaMatematica(self)
        lista='materias/Respuestas/Respuestas.txt'
        self.abrirVentanaAsignatura()

    def abrirVentanaPrincipal(self):

        self.close()
        otraventana=VentanaPrincipal(self)
        otraventana.show()

    def abrirVentanaMaterias(self):

        self.close()
        otraventana=VentanaMaterias(self)
        otraventana.show()

    def abrirVentanaAsignatura(self):

        self.close()
        otraventana=VentanaAsignatura(self)
        otraventana.show()

class VentanaCiencia(QMainWindow):

    def __init__(self, parent=None):

        super(VentanaCiencia, self).__init__(parent)

        self.MainWindow=loadUi('cienciaT.ui', self)

        self.b_ciencias1.clicked.connect(self.Ciencias1)

        self.b_ciencias2.clicked.connect(self.Ciencias2)

        self.botonreturn.clicked.connect(self.abrirVentanaMaterias)
                    
                    
    def Ciencias1(self):

        global lista
        global ventana
        ventana=VentanaCiencia(self)
        lista='materias/Ciencias1/Ciencias1.txt'
        self.abrirVentanaAsignatura()

    def Ciencias2(self):

        global lista
        global ventana
        ventana=VentanaCiencia(self)
        lista='materias/Ciencias2/Ciencias2.txt'
        self.abrirVentanaAsignatura()

    def Respuestas(self):

        global lista
        global ventana
        ventana=VentanaCiencia(self)
        lista='materias/Respuestas/Respuestas.txt'
        self.abrirVentanaAsignatura()

    def abrirVentanaPrincipal(self):

        self.close()
        otraventana=VentanaPrincipal(self)
        otraventana.show()

    def abrirVentanaMaterias(self):

        self.close()
        otraventana=VentanaMaterias(self)
        otraventana.show()

    def abrirVentanaAsignatura(self):

        self.close()
        otraventana=VentanaAsignatura(self)
        otraventana.show()

class VentanaLenguaje(QMainWindow):

    def __init__(self, parent=None):

        super(VentanaLenguaje, self).__init__(parent)

        self.MainWindow=loadUi('lenguajeT.ui', self)

        self.b_lenguaje1.clicked.connect(self.Lenguaje1)

        self.b_lenguaje2.clicked.connect(self.Lenguaje2)

        self.botonreturn.clicked.connect(self.abrirVentanaMaterias)
                    
                    
    def Lenguaje1(self):

        global lista
        global ventana
        ventana=VentanaLenguaje(self)
        lista='materias/Lenguaje1/Lenguaje1.txt'        
        self.abrirVentanaAsignatura()

    def Lenguaje2(self):

        global lista
        global ventana
        ventana=VentanaLenguaje(self)
        lista='materias/Lenguaje2/Lenguaje2.txt'
        self.abrirVentanaAsignatura()

    def Respuestas(self):

        global lista
        global ventana
        ventana=VentanaLenguaje(self)
        lista='materias/Respuestas/Respuestas.txt'
        self.abrirVentanaAsignatura()

    def abrirVentanaPrincipal(self):

        self.close()
        otraventana=VentanaPrincipal(self)
        otraventana.show()

    def abrirVentanaMaterias(self):

        self.close()
        otraventana=VentanaMaterias(self)
        otraventana.show()

    def abrirVentanaAsignatura(self):

        self.close()
        otraventana=VentanaAsignatura(self)
        otraventana.show()

class VentanaArtistica(QMainWindow):

    def __init__(self, parent=None):

        super(VentanaArtistica, self).__init__(parent)

        self.MainWindow=loadUi('artisticaT.ui', self)

        self.b_artistica1.clicked.connect(self.Artistica1)

        self.b_artistica2.clicked.connect(self.Artistica2)

        self.botonreturn.clicked.connect(self.abrirVentanaMaterias)
                    
                    
    def Artistica1(self):

        global lista
        global ventana
        ventana=VentanaArtistica(self)
        lista='materias/Artistica1/Artistica1.txt'
        self.abrirVentanaAsignatura()

    def Artistica2(self):

        global lista
        global ventana
        ventana=VentanaArtistica(self)
        lista='materias/Artistica2/Artistica2.txt'        
        self.abrirVentanaAsignatura()

    def Respuestas(self):

        global lista
        global ventana
        ventana=VentanaArtistica(self)
        lista='materias/Respuestas/Respuestas.txt'
        self.abrirVentanaAsignatura()

    def abrirVentanaPrincipal(self):

        self.close()
        otraventana=VentanaPrincipal(self)
        otraventana.show()

    def abrirVentanaMaterias(self):

        self.close()
        otraventana=VentanaMaterias(self)
        otraventana.show()

    def abrirVentanaAsignatura(self):

        self.close()
        otraventana=VentanaAsignatura(self)
        otraventana.show()

class VentanaAsignatura(QMainWindow):


    def __init__(self, parent=None):

        super(VentanaAsignatura, self).__init__(parent)
        self.MainWindow=loadUi('AsignaturaPB.ui', self)
        self.timer = QtCore.QTimer(self.MainWindow);
        self.timer.timeout.connect(self.navimg)
        self.timer.start(50);
        self.botonprin.clicked.connect(self.abrirVentanaPrincipal)
        self.returnqr.clicked.connect(self.abrirVentanaMaterias)
        self.topic_r.clicked.connect(self.abrirVentanaTopics)
        self.i=0
        self.bsiguiente.clicked.connect(self.sum)
        self.banterior.clicked.connect(self.res)
        hf=open(lista,'r')
        self.lines=hf.readlines()
        hf.close()

    def sum(self):

        if self.i < len(self.lines)-1:

            self.i=self.i+1

        else:

            self.i=self.i

    def res(self):

        if self.i > 0:

            self.i=self.i-1

        else:

            self.i=self.i

    def navimg(self):


        frame=cv2.imread(self.lines[self.i][:-1], cv2.IMREAD_COLOR)


        image = QtGui.QImage(frame, frame.shape[1], frame.shape[0], frame.shape[1] * frame.shape[2], QtGui.QImage.Format_RGB888)
        pixmap = QtGui.QPixmap()
        pixmap.convertFromImage(image.rgbSwapped())
        self.MainWindow.lblAsignatura.setPixmap(pixmap)

    def abrirVentanaPrincipal(self):

        self.timer.stop()
        self.close()
        otraventana=VentanaPrincipal(self)
        otraventana.show()

    def abrirVentanaMaterias(self):

        self.timer.stop()
        self.close()
        otraventana=VentanaMaterias(self)
        otraventana.show()

    def abrirVentanaTopics(self):

        global ventana
        self.timer.stop()
        self.close()
        ventana.show()

app = QApplication(sys.argv)
main = VentanaPrincipal()
main.show()
sys.exit(app.exec_())