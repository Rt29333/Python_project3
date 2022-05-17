# list_name = ['刘备', '关羽', '张飞', '张三', '李四', '杨戬', '诸葛亮']
# for name in list_name:
#     with open('dataname.txt', 'a+', encoding='utf8') as fp:
#         fp.write(name + ' ')

# # 打开指定目录下的文件
# with open('D:/python Projects/Python project3/dataname.txt', 'r', encoding='utf8') as fp:
#     mn = fp.read()
#     name = mn.split('\n')
#     print(name)

# 语音模块
# import pyttsx3
# listen = pyttsx3.init()
# listen.say("输出语音")
# listen.runAndWait()

#!/usr/bin/python3

# import _thread
# import time
#
# # 为线程定义一个函数
# def print_time(threadName, delay):
#    count = 0
#    while count < 5:
#       time.sleep(delay)
#       count += 1
#       print ("%s: %s" % (threadName, time.ctime(time.time()) ))
#
# # 创建两个线程
# try:
#    _thread.start_new_thread(print_time, ("Thread-1", 2, ) )
#    _thread.start_new_thread(print_time, ("Thread-2", 4, ) )
# except:
#    print ("Error: 无法启动线程")
#
# while 1:
#    pass

#
# from PySide2.QtWidgets import QApplication, QTextBrowser
# from PySide2.QtUiTools import QUiLoader
# from threading import Thread
#
# from PySide2.QtCore import Signal, QObject
#
#
# # 自定义信号源对象类型，一定要继承自 QObject
# class MySignals(QObject):
#    # 定义一种信号，两个参数 类型分别是： QTextBrowser 和 字符串
#    # 调用 emit方法 发信号时，传入参数 必须是这里指定的 参数类型
#    text_print = Signal(QTextBrowser, str)
#
#    # 还可以定义其他种类的信号
#    update_table = Signal(str)
#
#
# # 实例化
# global_ms = MySignals()
#
#
# class Stats:
#
#    def __init__(self):
#       self.ui = QUiLoader().load('main.ui')
#
#       # 自定义信号的处理函数
#       global_ms.text_print.connect(self.printToGui)
#
#    def printToGui(self, fb, text):
#       fb.append(str(text))
#       fb.ensureCursorVisible()
#
#    def task1(self):
#       def threadFunc():
#          # 通过Signal 的 emit 触发执行 主线程里面的处理函数
#          # emit参数和定义Signal的数量、类型必须一致
#          global_ms.text_print.emit(self.ui.infoBox1, '输出内容')
#
#       thread = Thread(target=threadFunc)
#       thread.start()
#
#    def task2(self):
#       def threadFunc():
#          global_ms.text_print.emit(self.ui.infoBox2, '输出内容')
#
#       thread = Thread(target=threadFunc)
#       thread.start()

from PyQt5.QtCore import QTimer
from Random import *
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import random
import time
import threading
import pyttsx3
import _thread

class Random_Slect(QtWidgets.QMainWindow, Ui_MainWindow):
   def __init__(self):
      super(Random_Slect, self).__init__()
      self.setupUi(self)
      self.num = 0
      self.num1 = 1

      self.lineEdit.setText('会是谁呢？')
      self.lineEdit.setReadOnly(True)
      self.pushButton.clicked.connect(self.start)

   def start(self):
      if self.radioButton.isChecked():
         print('顺序点名')
      elif self.radioButton_2.isChecked():
         print("随机点名")
         with open('dataname.txt', 'r', encoding='utf8') as fp:
             name_read = fp.read()
         name_list = name_read.split('\n')
         numbers = random.sample(range(0, len(name_list)), len(name_list))
         print(numbers)

if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    windows = Random_Slect()
    windows.show()

    sys.exit(app.exec_())