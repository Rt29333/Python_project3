from PyQt5.QtCore import QTimer
from Random import *
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import time
import threading
import pyttsx3
import _thread

# 用了一个数字算法


class Random_Slect(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Random_Slect, self).__init__()
        self.setupUi(self)
        self.num = 0
        self.num1 = 1

        self.lineEdit.setText('会是谁呢？')
        self.lineEdit.setReadOnly(True)

        self.pushButton.clicked.connect(self.start)
        self.pushButton_2.clicked.connect(self.stop)
        self.pushButton_2.setEnabled(False)



    def Click_Show(self):
        with open('dataname.txt', 'r', encoding='utf8') as fp:
            name_read = fp.read()
        name_list = name_read.split('\n')
        # print(name_list)
        for name in name_list:
            # print('开始111', self.num)
            # print('暂停111', self.num1)
            if self.num == self.num1 - 1:
                break
            # 实时刷新,随机显示
            # print(name)
            QtWidgets.QApplication.processEvents()
            self.lineEdit.setText(name)

    def start(self):
        self.num += 1
        # print('开始', self.num)
        self.pushButton.setEnabled(False)
        self.pushButton_2.setEnabled(True)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.Click_Show)
        self.timer.start()

    def stop(self):
        self.num1 += 1
        # print('暂停', self.num)
        self.pushButton_2.setEnabled(False)
        self.pushButton.setEnabled(True)
        self.timer.stop()
















if __name__ == '__main__':
    import _thread
    app = QtWidgets.QApplication(sys.argv)
    windows = Random_Slect()
    windows.show()

    sys.exit(app.exec_())