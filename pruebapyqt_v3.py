import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtGui, QtWidgets, uic
import cv2

class VentanaPrincipal(QMainWindow):

    def __init__(self, parent=None):
        super(VentanaPrincipal, self).__init__(parent)
        loadUi('ventanaprin.ui', self)
        self.botonqr.clicked.connect(self.abrirVentanaLector)

    def abrirVentanaLector(self):

        self.hide()
        otraventana=VentanaLector(self)
        otraventana.show()
        
class VentanaLector(QMainWindow):

    def __init__(self, parent=None):

        super(VentanaLector, self).__init__(parent)

        self.MainWindow=loadUi('camprueba2.ui', self)

        self.botonreturn.clicked.connect(self.abrirVentanaPrincipal)

        self.webcam = cv2.VideoCapture(0)

        self.timer = QtCore.QTimer(self.MainWindow);
 
        # Conectamos la señal timeout() que emite nuestro temporizador con la funcion show_frame().
        self.timer.timeout.connect(self.show_frame)
 
        # Tomamos una captura cada 1 mili-segundo.
        self.timer.start(50);


    def show_frame(self):

        val, frame  = self.webcam.read()

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
                    
            if dato == "Sociales":

                self.abrirVentanaSociales()
                        
            #    img = cv2.imread('colombia.jpg', cv2.IMREAD_COLOR)
            #    frame = img
                    
            elif dato == "adios":
                        
                img = cv2.imread('espana.jpg', cv2.IMREAD_COLOR)
                frame = img

        else:

            print("Codigo QR no detectado")
                
        image = QtGui.QImage(frame, frame.shape[1], frame.shape[0], frame.shape[1] * frame.shape[2], QtGui.QImage.Format_RGB888)
         
        pixmap = QtGui.QPixmap()
        pixmap.convertFromImage(image.rgbSwapped())
         
        self.MainWindow.lblWebcam.setPixmap(pixmap)


       
    def abrirVentanaPrincipal(self):

        self.timer.stop()
        self.webcam.release()
        self.parent().show()
        self.close()

    def abrirVentanaSociales(self):
        self.timer.stop()
        self.webcam.release()
        self.hide()
        otraventana=VentanaSociales(self)
        otraventana.show()
class VentanaLector1(QMainWindow):

    def __init__(self, parent=None):

        super(VentanaLector1, self).__init__(parent)

        self.MainWindow=loadUi('camprueba2.ui', self)

        self.botonreturn.clicked.connect(self.abrirVentanaPrincipal)

        self.webcam = cv2.VideoCapture(0)

        self.timer = QtCore.QTimer(self.MainWindow);
 
        # Conectamos la señal timeout() que emite nuestro temporizador con la funcion show_frame().
        self.timer.timeout.connect(self.show_frame)
 
        # Tomamos una captura cada 1 mili-segundo.
        self.timer.start(50);


    def show_frame(self):

        val, frame  = self.webcam.read()

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
                    
            if dato == "Sociales":

                self.abrirVentanaSociales()
                        
            #    img = cv2.imread('colombia.jpg', cv2.IMREAD_COLOR)
            #    frame = img
                    
            elif dato == "adios":
                        
                img = cv2.imread('espana.jpg', cv2.IMREAD_COLOR)
                frame = img

        else:

            print("Codigo QR no detectado")
                
        image = QtGui.QImage(frame, frame.shape[1], frame.shape[0], frame.shape[1] * frame.shape[2], QtGui.QImage.Format_RGB888)
         
        pixmap = QtGui.QPixmap()
        pixmap.convertFromImage(image.rgbSwapped())
         
        self.MainWindow.lblWebcam.setPixmap(pixmap)


       
    def abrirVentanaPrincipal(self):

        self.timer.stop()
        self.webcam.release()
        self.hide()
        otraventana=VentanaPrincipal(self)
        otraventana.show()

    def abrirVentanaSociales(self):
        self.timer.stop()
        self.webcam.release()
        self.hide()
        otraventana=VentanaSociales(self)
        otraventana.show()
class VentanaSociales(QMainWindow):


    def __init__(self, parent=None):

        super(VentanaSociales, self).__init__(parent)
        loadUi('visorimg_sociales.ui', self)
        self.botonprin.clicked.connect(self.abrirVentanaPrincipal)
        self.returnqr.clicked.connect(self.abrirVentanaLector)
        
#     def conversion(self):
       

    def abrirVentanaPrincipal(self):
        
        self.close()
        otraventana=VentanaPrincipal(self)
        otraventana.show()

    def abrirVentanaLector(self):

        otraventana=VentanaLector1(self)
        otraventana.show()
        self.hide()

        

app = QApplication(sys.argv)
main = VentanaPrincipal()
main.show()
sys.exit(app.exec_())