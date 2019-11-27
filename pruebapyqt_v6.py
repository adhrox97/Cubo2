import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtGui, QtWidgets, uic
import cv2

lista=''

class VentanaPrincipal(QMainWindow):

    def __init__(self, parent=None):
        super(VentanaPrincipal, self).__init__(parent)
        loadUi('ventanaprin2prueba.ui', self)
        self.botonqr.clicked.connect(self.abrirVentanaLector)

    def abrirVentanaLector(self):

        self.close()
        otraventana=VentanaLector(self)
        otraventana.show()
        
class VentanaLector(QMainWindow):

    def __init__(self, parent=None):

        super(VentanaLector, self).__init__(parent)

        self.MainWindow=loadUi('camprueba2prueba.ui', self)

        self.botonreturn.clicked.connect(self.abrirVentanaPrincipal)

        self.webcam = cv2.VideoCapture(0)

        self.timer = QtCore.QTimer(self.MainWindow);
 
        # Conectamos la señal timeout() que emite nuestro temporizador con la funcion show_frame().
        self.timer.timeout.connect(self.show_frame)
 
        # Tomamos una captura cada 50 mili-segundos.
        self.timer.start(50);


    def show_frame(self):

        val, frame  = self.webcam.read()

        global lista

        def display(im, bbox):
            n = len(bbox)
            for j in range(n):
                cv2.line(im, tuple(bbox[j][0]), tuple(bbox[ (j+2) % n][0]), (0,0,255), 3)
                

        qrDecoder = cv2.QRCodeDetector()
                
        # Detect and decode the qrcode
        data,bbox,rectifiedImage = qrDecoder.detectAndDecode(frame)

        if len(data)>0:

            dato=data
            print("Dato decodificado: {}".format(data))
            display(frame, bbox)
                    
            if dato == "Ciencias1":

                lista='materias/Ciencias1/Ciencias1.txt'
                self.abrirVentanaAsignatura()

            elif dato == "Ciencias2":

                lista='materias/Ciencias2/Ciencias2.txt'
                self.abrirVentanaAsignatura()
                    
            elif dato == "Matematicas1":

                lista='materias/Matematicas1/Matematicas1.txt'        
                self.abrirVentanaAsignatura()

            elif dato == "Matematicas2":
                
                lista='materias/Matematicas2/Matematicas2.txt'
                self.abrirVentanaAsignatura()

            elif dato == "Lenguaje1":

                lista='materias/Lenguaje1/Lenguaje1.txt'        
                self.abrirVentanaAsignatura()

            elif dato == "Lenguaje2":
                
                lista='materias/Lenguaje2/Lenguaje2.txt'
                self.abrirVentanaAsignatura()

            elif dato == "Artistica1":
                
                lista='materias/Artistica1/Artistica1.txt'
                self.abrirVentanaAsignatura()

            elif dato == "Artistica2":

                lista='materias/Artistica2/Artistica2.txt'        
                self.abrirVentanaAsignatura()

            elif dato == "Respuestas":
                
                lista='materias/Respuestas/Respuestas.txt'
                self.abrirVentanaAsignatura()

        else:

            print("Codigo QR no detectado")
                
        image = QtGui.QImage(frame, frame.shape[1], frame.shape[0], frame.shape[1] * frame.shape[2], QtGui.QImage.Format_RGB888)
         
        pixmap = QtGui.QPixmap()
        pixmap.convertFromImage(image.rgbSwapped())
        self.MainWindow.lblWebcam.setPixmap(pixmap)

    def abrirVentanaPrincipal(self):

        self.timer.stop()
        self.webcam.release()
        self.close()
        otraventana=VentanaPrincipal(self)
        otraventana.show()

    def abrirVentanaAsignatura(self):

        self.timer.stop()
        self.webcam.release()
        self.close()
        otraventana=VentanaAsignatura(self)
        otraventana.show()

class VentanaAsignatura(QMainWindow):


    def __init__(self, parent=None):

        super(VentanaAsignatura, self).__init__(parent)
        self.MainWindow=loadUi('Asignatura.ui', self)
        self.timer = QtCore.QTimer(self.MainWindow);
        self.timer.timeout.connect(self.navimg)
        self.timer.start(50);
        self.botonprin.clicked.connect(self.abrirVentanaPrincipal)
        self.returnqr.clicked.connect(self.abrirVentanaLector)
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

    def abrirVentanaLector(self):

        self.timer.stop()
        self.close()
        otraventana=VentanaLector(self)
        otraventana.show()

app = QApplication(sys.argv)
main = VentanaPrincipal()
main.show()
sys.exit(app.exec_())