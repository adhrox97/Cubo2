import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtGui, QtWidgets, uic
import cv2

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

                self.abrirVentanaCiencias1()

            elif dato == "Ciencias2":

                self.abrirVentanaCiencias2()
                    
            elif dato == "Matematicas1":
                        
                self.abrirVentanaMatematicas1()

            elif dato == "Matematicas2":
                        
                self.abrirVentanaMatematicas2()

            elif dato == "Lenguaje1":
                        
                self.abrirVentanaLenguaje1()

            elif dato == "Lenguaje2":
                        
                self.abrirVentanaLenguaje2()

            elif dato == "Artistica1":
                        
                self.abrirVentanaArtistica1()

            elif dato == "Artistica2":
                        
                self.abrirVentanaArtistica2()

            elif dato == "Respuestas":
                        
                self.abrirVentanaRespuestas()

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

    def abrirVentanaCiencias1(self):

        self.timer.stop()
        self.webcam.release()
        self.close()
        otraventana=VentanaCiencias1(self)
        otraventana.show()

    def abrirVentanaCiencias2(self):

        self.timer.stop()
        self.webcam.release()
        self.close()
        otraventana=VentanaCiencias2(self)
        otraventana.show()

    def abrirVentanaMatematicas1(self):

        self.timer.stop()
        self.webcam.release()
        self.close()
        otraventana=VentanaMatematicas1(self)
        otraventana.show()

    def abrirVentanaMatematicas2(self):

        self.timer.stop()
        self.webcam.release()
        self.close()
        otraventana=VentanaMatematicas2(self)
        otraventana.show()

    def abrirVentanaLenguaje1(self):

        self.timer.stop()
        self.webcam.release()
        self.close()
        otraventana=VentanaLenguaje1(self)
        otraventana.show()

    def abrirVentanaLenguaje2(self):

        self.timer.stop()
        self.webcam.release()
        self.close()
        otraventana=VentanaLenguaje2(self)
        otraventana.show()

    def abrirVentanaArtistica1(self):

        self.timer.stop()
        self.webcam.release()
        self.close()
        otraventana=VentanaArtistica1(self)
        otraventana.show()

    def abrirVentanaArtistica2(self):

        self.timer.stop()
        self.webcam.release()
        self.close()
        otraventana=VentanaArtistica2(self)
        otraventana.show()

    def abrirVentanaRespuestas(self):

        self.timer.stop()
        self.webcam.release()
        self.close()
        otraventana=VentanaRespuestas(self)
        otraventana.show()

class VentanaCiencias1(QMainWindow):


    def __init__(self, parent=None):

        super(VentanaCiencias1, self).__init__(parent)
        self.MainWindow=loadUi('Ciencias1.ui', self)
        self.timer = QtCore.QTimer(self.MainWindow);
        self.timer.timeout.connect(self.navimg)
        self.timer.start(50);
        self.botonprin.clicked.connect(self.abrirVentanaPrincipal)
        self.returnqr.clicked.connect(self.abrirVentanaLector)
        self.i=0
        self.bsiguiente.clicked.connect(self.sum)
        self.banterior.clicked.connect(self.res)
        lista='materias/Ciencias1/Ciencias1.txt'
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
        self.MainWindow.lblCiencias1.setPixmap(pixmap)

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

class VentanaCiencias2(QMainWindow):


    def __init__(self, parent=None):

        super(VentanaCiencias2, self).__init__(parent)
        self.MainWindow=loadUi('Ciencias2.ui', self)
        self.timer = QtCore.QTimer(self.MainWindow);
        self.timer.timeout.connect(self.navimg)
        self.timer.start(50);
        self.botonprin.clicked.connect(self.abrirVentanaPrincipal)
        self.returnqr.clicked.connect(self.abrirVentanaLector)
        self.i=0
        self.bsiguiente.clicked.connect(self.sum)
        self.banterior.clicked.connect(self.res)
        lista='materias/Ciencias2/Ciencias2.txt'
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
        self.MainWindow.lblCiencias2.setPixmap(pixmap)

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

class VentanaMatematicas1(QMainWindow):


    def __init__(self, parent=None):

        super(VentanaMatematicas1, self).__init__(parent)
        self.MainWindow=loadUi('Matematicas1.ui', self)
        self.timer = QtCore.QTimer(self.MainWindow);
        self.timer.timeout.connect(self.navimg)
        self.timer.start(50);
        self.botonprin.clicked.connect(self.abrirVentanaPrincipal)
        self.returnqr.clicked.connect(self.abrirVentanaLector)
        self.i=0
        self.bsiguiente.clicked.connect(self.sum)
        self.banterior.clicked.connect(self.res)
        lista='materias/Matematicas1/Matematicas1.txt'
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
        self.MainWindow.lblMatematicas1.setPixmap(pixmap)

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

class VentanaMatematicas2(QMainWindow):


    def __init__(self, parent=None):

        super(VentanaMatematicas2, self).__init__(parent)
        self.MainWindow=loadUi('Matematicas2.ui', self)
        self.timer = QtCore.QTimer(self.MainWindow);
        self.timer.timeout.connect(self.navimg)
        self.timer.start(50);
        self.botonprin.clicked.connect(self.abrirVentanaPrincipal)
        self.returnqr.clicked.connect(self.abrirVentanaLector)
        self.i=0
        self.bsiguiente.clicked.connect(self.sum)
        self.banterior.clicked.connect(self.res)
        lista='materias/Matematicas2/Matematicas2.txt'
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
        self.MainWindow.lblMatematicas2.setPixmap(pixmap)

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

class VentanaLenguaje1(QMainWindow):


    def __init__(self, parent=None):

        super(VentanaLenguaje1, self).__init__(parent)
        self.MainWindow=loadUi('Lenguaje1.ui', self)
        self.timer = QtCore.QTimer(self.MainWindow);
        self.timer.timeout.connect(self.navimg)
        self.timer.start(50);
        self.botonprin.clicked.connect(self.abrirVentanaPrincipal)
        self.returnqr.clicked.connect(self.abrirVentanaLector)
        self.i=0
        self.bsiguiente.clicked.connect(self.sum)
        self.banterior.clicked.connect(self.res)
        lista='materias/Lenguaje1/Lenguaje1.txt'
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
        self.MainWindow.lblLenguaje1.setPixmap(pixmap)

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

class VentanaLenguaje2(QMainWindow):


    def __init__(self, parent=None):

        super(VentanaLenguaje2, self).__init__(parent)
        self.MainWindow=loadUi('Lenguaje2.ui', self)
        self.timer = QtCore.QTimer(self.MainWindow);
        self.timer.timeout.connect(self.navimg)
        self.timer.start(50);
        self.botonprin.clicked.connect(self.abrirVentanaPrincipal)
        self.returnqr.clicked.connect(self.abrirVentanaLector)
        self.i=0
        self.bsiguiente.clicked.connect(self.sum)
        self.banterior.clicked.connect(self.res)
        lista='materias/Lenguaje2/Lenguaje2.txt'
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
        self.MainWindow.lblLenguaje2.setPixmap(pixmap)

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

class VentanaArtistica1(QMainWindow):


    def __init__(self, parent=None):

        super(VentanaArtistica1, self).__init__(parent)
        self.MainWindow=loadUi('Artistica1.ui', self)
        self.timer = QtCore.QTimer(self.MainWindow);
        self.timer.timeout.connect(self.navimg)
        self.timer.start(50);
        self.botonprin.clicked.connect(self.abrirVentanaPrincipal)
        self.returnqr.clicked.connect(self.abrirVentanaLector)
        self.i=0
        self.bsiguiente.clicked.connect(self.sum)
        self.banterior.clicked.connect(self.res)
        lista='materias/Artistica1/Artistica1.txt'
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
        self.MainWindow.lblArtistica1.setPixmap(pixmap)

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

class VentanaArtistica2(QMainWindow):


    def __init__(self, parent=None):

        super(VentanaArtistica2, self).__init__(parent)
        self.MainWindow=loadUi('Artistica2.ui', self)
        self.timer = QtCore.QTimer(self.MainWindow);
        self.timer.timeout.connect(self.navimg)
        self.timer.start(50);
        self.botonprin.clicked.connect(self.abrirVentanaPrincipal)
        self.returnqr.clicked.connect(self.abrirVentanaLector)
        self.i=0
        self.bsiguiente.clicked.connect(self.sum)
        self.banterior.clicked.connect(self.res)
        lista='materias/Artistica2/Artistica2.txt'
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
        self.MainWindow.lblArtistica2.setPixmap(pixmap)

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

class VentanaRespuestas(QMainWindow):


    def __init__(self, parent=None):

        super(VentanaRespuestas, self).__init__(parent)
        self.MainWindow=loadUi('Respuestas.ui', self)
        self.timer = QtCore.QTimer(self.MainWindow);
        self.timer.timeout.connect(self.navimg)
        self.timer.start(50);
        self.botonprin.clicked.connect(self.abrirVentanaPrincipal)
        self.returnqr.clicked.connect(self.abrirVentanaLector)
        self.i=0
        self.bsiguiente.clicked.connect(self.sum)
        self.banterior.clicked.connect(self.res)
        lista='materias/Respuestas/Respuestas.txt'
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
        self.MainWindow.lblRespuestas.setPixmap(pixmap)

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