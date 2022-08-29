# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 19:40:07 2022

@author: Ziddane
"""


from PyQt5.QtWidgets import *

import sys
from PyQt5 import uic

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        
        uic.loadUi("Form.ui", self)
        
        self.label_task_name = self.findChild(QLabel, "label")
        self.name_box = self.findChild(QPlainTextEdit, "plainTextEdit")
        self.condirm_button = self.findChild(QPushButton, "pushButton")

        self.confirm_button.clicked.connect(self.clicker)

        self.show()
        
    def clicker(self):
        print("heyo")
        #self.label.setText(f'hello {self.textedit.toPlainText}')
        
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()

"""
Form, Window = uic.loadUiType("Form.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)



window.show()


app.exec()
"""
