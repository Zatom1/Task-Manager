# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 19:32:17 2022

@author: Ziddane
"""

import pickle as pkl
import numpy as np
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDateTime, Qt
import time
import sys
from sys import exit
from PyQt5 import uic
import datetime

#format for below tasks - [name(str), desc(str), due date(epoch time int)]

#2d array w/ list of all current tasks
task_arr = np.array([["", "no description set", 0],["", "no description set", 0],["", "no description set", 0],["", "no description set", 0],["", "no description set", 0],["", "no description set", 0],["", "no description set", 0],["", "no description set", 0]])
#load task_arr from local storage in order to enable saving
        
task_arr = np.load("task_list.npy")

def new_alert(title):
    alert = QMessageBox()
    alert.setText(title + " Task Created")
    alert.exec()
    


class CustomDialog(QDialog):
    def __init__(self, task_num):
        super().__init__()
        self.task_num = task_num

        self.setWindowTitle("Task")
        uic.loadUi("task popout.ui", self)
        
        self.title = self.findChild(QLabel, "title")
        self.title.setText(task_arr[self.task_num][0])
        self.desc = self.findChild(QLabel, "description_box")
        self.desc.setText(task_arr[self.task_num][1])
        self.date = self.findChild(QLabel, "date")
        epoch_time = task_arr[self.task_num][2]
        print(epoch_time[0])
        string_epoch = ""
        for i in range(0, 10):
            string_epoch += epoch_time[i]
        date = datetime.datetime.fromtimestamp(int(string_epoch)+21600)  
        datetime_str = date.strftime( "%Y - %m - %d")  

        self.date.setText(str(datetime_str))
        
        self.button = self.findChild(QPushButton, "complete_button")
        self.button.clicked.connect(lambda: self.complete_task(self.task_num))
        
    def complete_task(self, task_num):
        task_arr[self.task_num][0] = ""

class UI(QDialog):
    
    def __init__(self):
        super(UI, self).__init__()
        self.setWindowTitle("Organizer")
        
        now = QDateTime.currentDateTime()

        unix_time = now.toSecsSinceEpoch()
        print(unix_time)
        
        uic.loadUi("Form.ui", self)
        self.due_date = self.findChild(QDateEdit, "dateEdit")
        due_date = self.due_date.dateTime()
        temp = due_date.toPyDateTime()
        due_unix_time = (temp - datetime.datetime(1970,1,1)).total_seconds()
        print(due_unix_time)
        
        self.task_button1 = self.findChild(QPushButton, "pushButton_3")
        self.task_button2 = self.findChild(QPushButton, "pushButton_4")
        self.task_button3 = self.findChild(QPushButton, "pushButton_5")
        self.task_button4 = self.findChild(QPushButton, "pushButton_6")
        self.task_button5 = self.findChild(QPushButton, "pushButton_7")
        self.task_button6 = self.findChild(QPushButton, "pushButton_8")
        self.task_button7 = self.findChild(QPushButton, "pushButton_9")
        self.task_button8 = self.findChild(QPushButton, "pushButton_10")
        
        """popup = task_popup()
        if popup.exec():
            print("yes")
        else:
            print("no")
        """
        
        
        self.task1 = self.findChild(QLabel, "todo_1")
        self.task2 = self.findChild(QLabel, "todo_2")
        self.task3 = self.findChild(QLabel, "todo_3")
        self.task4 = self.findChild(QLabel, "todo_4")
        self.task5 = self.findChild(QLabel, "todo_5")
        self.task6 = self.findChild(QLabel, "todo_6")
        self.task7 = self.findChild(QLabel, "todo_7")
        self.task8 = self.findChild(QLabel, "todo_8")
        
        self.task1.setText(task_arr[0][0])
        self.task2.setText(task_arr[1][0])
        self.task3.setText(task_arr[2][0])
        self.task4.setText(task_arr[3][0])
        self.task5.setText(task_arr[4][0])
        self.task6.setText(task_arr[5][0])
        self.task7.setText(task_arr[6][0])
        self.task8.setText(task_arr[7][0])

        self.name_box = self.findChild(QLineEdit, "lineEdit")
        self.desc_box = self.findChild(QPlainTextEdit, "plainTextEdit")

        self.confirm_button = self.findChild(QPushButton, "pushButton_2")
        self.confirm_button.clicked.connect(self.save_task)
        
        self.exit_button = self.findChild(QPushButton, "pushButton")
        self.exit_button.clicked.connect(self.exit_program)
        
        
        self.task_button1.clicked.connect(lambda: self.button_clicked(0))
        self.task_button2.clicked.connect(lambda: self.button_clicked(1))
        self.task_button3.clicked.connect(lambda: self.button_clicked(2))
        self.task_button4.clicked.connect(lambda: self.button_clicked(3))
        self.task_button5.clicked.connect(lambda: self.button_clicked(4))
        self.task_button6.clicked.connect(lambda: self.button_clicked(5))
        self.task_button7.clicked.connect(lambda: self.button_clicked(6))
        self.task_button8.clicked.connect(lambda: self.button_clicked(7))


        self.show()

    def button_clicked(self, num):
        print("click")

        dlg = CustomDialog(num)
        if dlg.exec():
            print("Success!")
        else:
            print("Cancel!")
            self.task1.setText(task_arr[0][0])
            self.task2.setText(task_arr[1][0])
            self.task3.setText(task_arr[2][0])
            self.task4.setText(task_arr[3][0])
            
            self.task5.setText(task_arr[4][0])
            self.task6.setText(task_arr[5][0])
            self.task7.setText(task_arr[6][0])
            self.task8.setText(task_arr[7][0])
            
    def save_task(self):
        index = 0
        name = self.name_box.text()
        desc = self.desc_box.toPlainText()
        due_date = self.due_date.dateTime()
        temp = due_date.toPyDateTime()
        due_unix_time = (temp - datetime.datetime(1970,1,1)).total_seconds()
        for i in range(0,7):
            if task_arr[i][0] == "":
                index = i
                break
        task_arr[index][0] = name
        task_arr[index][1] = desc
        task_arr[index][2] = due_unix_time

        print(index)
        print(name)
        print(desc)
        print(due_unix_time)
        
        self.task1.setText(task_arr[0][0])
        self.task2.setText(task_arr[1][0])
        self.task3.setText(task_arr[2][0])
        self.task4.setText(task_arr[3][0])
        
        self.task5.setText(task_arr[4][0])
        self.task6.setText(task_arr[5][0])
        self.task7.setText(task_arr[6][0])
        self.task8.setText(task_arr[7][0])
        
    
    def exit_program(self):
        name = self.name_box.text()
        np.save("task_list", task_arr)
        new_alert(name)
        
        #self.label.setText(f'hello {self.textedit.toPlainText}')
    
app = QApplication(sys.argv)
UIWindow = UI()
UIWindow.show()
app.exec_()
