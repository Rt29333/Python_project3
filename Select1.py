from PyQt5.QtCore import QTimer
from Random import *
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import random
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

        self.pushButton_4.clicked.connect(self.Click_reselect)
        self.pushButton_4.setEnabled(False)

        self.pushButton.clicked.connect(self.start)
        self.pushButton.setEnabled(False)

        self.pushButton_2.clicked.connect(self.stop)
        # 默认禁用暂停按键
        self.pushButton_2.setEnabled(False)

        self.pushButton_3.clicked.connect(self.Click_Insert)

        self.textBrowser.setAlignment(QtCore.Qt.AlignCenter)

        self.pushButton_5.clicked.connect(self.Click_Clear)

        # 默认选择 随机点名
        self.radioButton_2.setChecked(True)


    def Click_Clear(self):
        self.textBrowser.clear()

    def Click_reselect(self):
        self.lineEdit.clear()
        self.lineEdit.setText('会是谁呢？')
        self.pushButton.setEnabled(False)
        self.pushButton_3.setEnabled(True)
        self.pushButton_4.setEnabled(False)

    def Click_Insert(self):
        try:
            self.Insert_path, type = QtWidgets.QFileDialog.getOpenFileName(None, '打开文件',
                                                                           'D:/python Projects/Python project3',
                                                                           'Type files(*.txt)')
            # print(self.Insert_path)
            if self.Insert_path != "":
                self.pushButton.setEnabled(True)
                self.pushButton_3.setEnabled(False)

        except Exception as e:
            # print(e)
            QtWidgets.QMessageBox.warning(self.widget, '提示', '未导出学生信息名单')

    def Click_Show(self):
        try:
            with open(self.Insert_path, 'r', encoding='utf8') as fp:
                name_read = fp.read()
            name_list = name_read.split('\n')
            # print(name_list)
            if self.radioButton.isChecked():
                for name in name_list:
                    # print('开始111', self.num)
                    # print('暂停111', self.num1)
                    if self.num == self.num1 - 1:
                        # print("恭喜{}中奖".format(name))
                        self.textBrowser.append("恭喜 \"{}\" 中奖啦".format(name))
                        break
                    # 实时刷新,随机显示
                    # print(name)
                    QtWidgets.QApplication.processEvents()
                    self.lineEdit.setText(name)
            elif self.radioButton_2.isChecked():
                numbers = random.sample(range(0, len(name_list)), len(name_list))
                # print(numbers)
                # print("随机点名")
                for num in numbers:
                    name = name_list[num]
                    # print(name)
                    if self.num == self.num1 - 1:
                        # print("恭喜{}中奖".format(name))
                        self.textBrowser.append("恭喜 \"{}\" 中奖啦".format(name))
                        break
                    QtWidgets.QApplication.processEvents()
                    self.lineEdit.setText(name)
        except Exception as e:
            # print(e)
            QtWidgets.QMessageBox.warning(self.widget, '提示', '未导出学生信息名单')

    def start(self):
        # if self.radioButton.isChecked():
        #     print('顺序点名')
        # elif self.radioButton_2.isChecked():
        #     print("随机点名")
        try:
            self.num += 1
            # print('开始', self.num)
            self.pushButton.setEnabled(False)
            self.pushButton_2.setEnabled(True)
            self.pushButton_3.setEnabled(False)
            self.pushButton_4.setEnabled(False)
            self.timer = QTimer(self)
            self.timer.timeout.connect(self.Click_Show)
            self.timer.start()
        except Exception as e:
            # print(e)
            QtWidgets.QMessageBox.warning(self.widget, '提示', '未导出学生信息名单')

    def stop(self):
        self.pushButton_4.setEnabled(True)
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