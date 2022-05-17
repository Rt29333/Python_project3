
from Random import *
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import time
import threading
import pyttsx3


class Random_Slect(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Random_Slect, self).__init__()
        self.setupUi(self)

        # 给标签设置边框
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        # 设置阴影
        self.label.setFrameShadow(QtWidgets.QFrame.Raised)


        self.label.setText('会是谁呢？')

        self.pushButton.clicked.connect(self.onbutton)
        self.pushButton_2.clicked.connect(self.Click_Stop)


    def onbutton(self):
        self.thread = threading.Thread(target=self.start)
        self.thread.start()

    def start(self):
        while True:
            with open('dataname.txt', 'r', encoding='utf8') as fp:
                name_read = fp.read()
                name_list = name_read.split('\n')
                for name in name_list:
                    print(name)
                    self.label.setText(name)
                    pyttsx3.speak(name)
                    time.sleep(0.2)



    def Click_Stop(self):
        self.stop_check = True








if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    windows = Random_Slect()
    windows.show()
    sys.exit(app.exec_())