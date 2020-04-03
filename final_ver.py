# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import os
import matplotlib.pyplot as plt
import collections

# simple base class for process works on FCFS
class CProcess:
    def __init__(self, name="", time=0, priority=None, order=0):
        self.Name = name
        self.Time = time
        self.Priority = priority
        self.Order = order

#TODO extend classes in here by inhertinace

msg = "ENTER A VALID INPUT"
error_str2 = "</span></p></body></html>"
error_str1 = "<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#ff0000;\">"

list_of_proc = []

def bubble_sort_of_order(l):
    for iteration in range(len(l)):
        for index in range(1, len(l)):
            this = l[index]
            prev = l[index - 1]

            if prev.Order <= this.Order:
                continue

            l[index] = prev
            l[index - 1] = this

def bubble_sort_of_Time(l):
    for iteration in range(len(l)):
        for index in range(1, len(l)):
            this = l[index]
            prev = l[index - 1]

            if prev.Time <= this.Time:
                continue

            l[index] = prev
            l[index - 1] = this

def bubble_sort_of_Priority(l):
    for iteration in range(len(l)):
        for index in range(1, len(l)):
            this = l[index]
            prev = l[index - 1]

            if prev.Priority <= this.Priority:
                continue

            l[index] = prev
            l[index - 1] = this

def bubble_sort_of(l):
    for iteration in range(len(l)):
        for index in range(1, len(l)):
            this = l[index]
            prev = l[index - 1]

            if prev <= this:
                continue

            l[index] = prev
            l[index - 1] = this


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1132, 624)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.process_name = QtWidgets.QLineEdit(self.centralwidget)
        self.process_name.setGeometry(QtCore.QRect(40, 150, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.process_name.setFont(font)
        self.process_name.setText("")
        self.process_name.setObjectName("process_name")
        self.process_time = QtWidgets.QLineEdit(self.centralwidget)
        self.process_time.setGeometry(QtCore.QRect(300, 150, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.process_time.setFont(font)
        self.process_time.setText("")
        self.process_time.setObjectName("process_time")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 100, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(310, 110, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.type = QtWidgets.QComboBox(self.centralwidget)
        self.type.setGeometry(QtCore.QRect(40, 240, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.type.setFont(font)
        self.type.setObjectName("type")
        self.type.addItem("")
        self.type.addItem("")
        self.draw_button = QtWidgets.QPushButton(self.centralwidget)
        self.draw_button.setGeometry(QtCore.QRect(310, 280, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.draw_button.setFont(font)
        self.draw_button.setObjectName("draw_button")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 190, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.process_priority = QtWidgets.QLineEdit(self.centralwidget)
        self.process_priority.setGeometry(QtCore.QRect(570, 150, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.process_priority.setFont(font)
        self.process_priority.setText("")
        self.process_priority.setObjectName("process_priority")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(680, 210, 256, 291))
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(570, 110, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.process_order = QtWidgets.QLineEdit(self.centralwidget)
        self.process_order.setGeometry(QtCore.QRect(810, 150, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.process_order.setFont(font)
        self.process_order.setText("")
        self.process_order.setObjectName("process_order")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(810, 110, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.algo = QtWidgets.QComboBox(self.centralwidget)
        self.algo.setGeometry(QtCore.QRect(40, 340, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.algo.setFont(font)
        self.algo.setObjectName("algo")
        self.algo.addItem("")
        self.algo.addItem("")
        self.algo.addItem("")
        self.algo.addItem("")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(40, 290, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.add_button = QtWidgets.QPushButton(self.centralwidget)
        self.add_button.setGeometry(QtCore.QRect(390, 60, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.add_button.setFont(font)
        self.add_button.setObjectName("add_button")
        self.process_remove = QtWidgets.QComboBox(self.centralwidget)
        self.process_remove.setGeometry(QtCore.QRect(320, 470, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.process_remove.setFont(font)
        self.process_remove.setObjectName("process_remove")
        self.remove_button = QtWidgets.QPushButton(self.centralwidget)
        self.remove_button.setGeometry(QtCore.QRect(320, 410, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.remove_button.setFont(font)
        self.remove_button.setObjectName("remove_button")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(120, 10, 751, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")

        self.time_quantum = QtWidgets.QLineEdit(self.centralwidget)
        self.time_quantum.setGeometry(QtCore.QRect(40, 470, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.time_quantum.setFont(font)
        self.time_quantum.setText("")
        self.time_quantum.setObjectName("time_quantum")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(40, 410, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")

        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(40, 540, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.avaerage_display = QtWidgets.QLabel(self.centralwidget)
        self.avaerage_display.setGeometry(QtCore.QRect(250, 540, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.avaerage_display.setFont(font)
        self.avaerage_display.setText("")
        self.avaerage_display.setObjectName("avaerage_display")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.label_7.hide()

        self.process_remove.hide()
        self.remove_button.hide()

        self.count = 1
        self.time_q = None

        #TODO add remove method optional
        self.draw_button.clicked.connect(self.validate)
        #TODO go to validate combination first then draw
        self.add_button.clicked.connect(self.add)
        self.remove_button.clicked.connect(self.remove)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Process Name"))
        self.label_2.setText(_translate("MainWindow", "Time"))
        self.type.setItemText(0, _translate("MainWindow", "Non Preemptive"))
        self.type.setItemText(1, _translate("MainWindow", "Preemptive"))
        self.draw_button.setText(_translate("MainWindow", "Draw"))
        self.label_3.setText(_translate("MainWindow", "Type"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "Process List"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.label_4.setText(_translate("MainWindow", "Priority"))
        self.label_5.setText(_translate("MainWindow", "Arrival"))
        self.algo.setItemText(0, _translate("MainWindow", "FCFS"))
        self.algo.setItemText(1, _translate("MainWindow", "SJF"))
        self.algo.setItemText(2, _translate("MainWindow", "Priority"))
        self.algo.setItemText(3, _translate("MainWindow", "RR"))
        self.label_6.setText(_translate("MainWindow", "Algo"))
        self.add_button.setText(_translate("MainWindow", "Add process"))
        self.remove_button.setText(_translate("MainWindow", "Remove Procces"))
        self.label_7.setText(_translate("MainWindow","<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#ff0000;\">ENTER A VALID INPUT</span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "Time quantum:"))
        self.label_9.setText(_translate("MainWindow", "Average Time:"))
    def remove(self):
        if len(list_of_proc) == 0:
            return
        re = self.process_remove.currentIndex()
        self.process_remove.removeItem(re)
        item = self.listWidget.item(re+1)
        self.listWidget.removeItemWidget(item)
        self.count -= 1
        list_of_proc.pop(re)
        item.setText("")
    def add(self):
        p_name = self.process_name.text()
        if p_name == "":
            msg = "Not a valid Name"
            self.label_7.setText(error_str1+msg+error_str2)
            self.label_7.show()
            return

        for p in list_of_proc:
            if p_name == p.Name:
                msg = "repeated Name"
                self.label_7.setText(error_str1 + msg + error_str2)
                self.label_7.show()
                return

        self.process_name.clear()
        try:
            p_time = int(self.process_time.text())
            if p_time <= 0:
                msg = "not a valid time"
                self.label_7.setText(error_str1 + msg + error_str2)
                self.label_7.show()
                return
            #TODO if negative

            self.process_time.clear()
        except:
            msg = "not a valid time"
            self.label_7.setText(error_str1 + msg + error_str2)
            self.label_7.show()
            return


        try:
            p_priority = int(self.process_priority.text())
            if p_priority <= 0:
                msg = "not a valid priority"
                self.label_7.setText(error_str1 + msg + error_str2)
                self.label_7.show()
                return

        except:
            p_priority = None

        self.process_priority.clear()
        try:
            p_order = int(self.process_order.text())
        except:
            p_order = 0

        self.process_order.clear()

        # TODO validate input (not repeated nor invalid type) show error message
        pro = CProcess(p_name,p_time,p_priority,p_order)
        list_of_proc.append(pro)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = self.listWidget.item(self.count)
        item.setText("NAME: " + p_name + "\tTIME: " + str(p_time) + "\tPriotity: " + str(p_priority) +"\tArrive " + str(p_order)  )
        self.count += 1
        self.process_remove.addItem(p_name)
        self.label_7.hide()


    def draw(self,periods,pro):
        print(periods)
        print(pro)
        self.avaerage_display.setText("15")

        i = 0
        while i <= len(periods) - 2:
            try:
                if pro[i] == pro[i + 1]:
                    periods[i] = (periods[i][0], periods[i + 1][1] + periods[i][1])
                    periods.pop(i + 1)
                    pro.pop(i + 1)
                    # i = (len(pro) - 1 + i) % len(pro)
                else:
                    #i = (i + 1) % len(pro)
                    i += 1
            except:
                break
        print(pro)
        print(periods)
        sum_wa = 0
        found = []
        for i in range(len(pro)):
            if not pro[i] in found:
                sum_wa += periods[i][0]
                final = periods[i][0] + periods[i][1]
                for j in range(i+1,len(pro)):
                    if pro[i] == pro[j]:
                        sum_wa += periods[j][0] - final
                        final = periods[j][0] + periods[j][1]
                found.append(pro[i])

        jk = str(sum_wa/len(list_of_proc))
        self.avaerage_display.setText(jk)


        i=0
        s = []
        for per in periods:
            s.append(per[0])
            s.append(per[0]+per[1])
        # Importing the matplotlb.pyplot
        #print(s)
        # Declaring a figure "gnt"
        fig, gnt = plt.subplots()

        # Setting Y-axis limits
        gnt.set_ylim(0, 20)

        # Setting X-axis limits
        gnt.set_xlim(0, periods[len(periods)-1][0])



        # Setting labels for x-axis and y-axis
        gnt.set_xlabel('time')
        gnt.set_ylabel('gantt')
        gnt.set_xticks(s)
        # Setting ticks on y-axis
        gnt.set_yticks([10])
        # Labelling tickes of y-axis
        gnt.set_yticklabels(['p'])

        # Setting graph attribute
        gnt.grid(True)

        # Declaring a bar in schedule
        #gnt.broken_barh([(40, 50)], (30, 9), facecolors=('tab:orange'))

        # Declaring multiple bars in at same level and same width
        #gnt.broken_barh([(110, 10), (150, 10)], (10, 9),facecolors='tab:blue')

        #gnt.broken_barh([(10, 50), (100, 20), (130, 10)], (5, 10),facecolors=('tab:red'))
        gnt.broken_barh(periods, (5, 10), facecolors=('tab:grey'))

        for i in range(len(pro)):
            beg = periods[i][0]
            end = periods[i][1]/2
            plt.text(beg+end, 10, pro[i],fontsize=10)

        plt.show()
        #plt.savefig("gantt1.png")



    def validate(self):
        if len(list_of_proc) == 0:
            msg = "add process first"
            self.label_7.setText(error_str1 + msg + error_str2)
            self.label_7.show()
            return
        p_type = self.type.currentText()
        p_algo = self.algo.currentText()
        if p_algo == "FCFS":
            if p_type == "Preemptive":
                msg = "FCFS is not Preemptive"
                self.label_7.setText(error_str1 + msg + error_str2)
                self.label_7.show()
                return
            else:
                self.label_7.hide()
                self.fcfs_m()
        if p_algo == "SJF":
            self.label_7.hide()
            self.sjf_m(p_type)

        if p_algo == "RR":
            if p_type == "Non Preemptive":
                msg = "RR is Preemptive only"
                self.label_7.setText(error_str1 + msg + error_str2)
                self.label_7.show()
                return
            if self.time_quantum.text() == "":
                msg = "time quantum is missing"
                self.label_7.setText(error_str1 + msg + error_str2)
                self.label_7.show()
                return
            try:
                self.time_q = int(self.time_quantum.text())
                if self.time_q <= 0:
                    self.time_q/0
            except:
                msg = "not a valid time quantum"
                self.label_7.setText(error_str1 + msg + error_str2)
                self.label_7.show()
                return

            self.label_7.hide()
            self.rr_m()

        if p_algo == "Priority":
            self.label_7.hide()
            self.priority_m(p_type)
            return

        self.label_7.hide()

    def fcfs_m(self):
        begin = 0
        periods = []
        pro = []
        #print(list_of_proc)
        bubble_sort_of_order(list_of_proc)
        begin = list_of_proc[0].Order
        for i in range(0,len(list_of_proc)):
            if begin < list_of_proc[i].Order:
                begin = list_of_proc[i].Order
            pro.append(list_of_proc[i].Name)
            t = list_of_proc[i].Time
            periods.append( (begin,t))
            print((begin, t))
            begin += t
        periods.append((begin, 0))
        self.draw(periods,pro)

    def sjf_m(self,p_type):
        if p_type == "Non Preemptive":
            bubble_sort_of_order(list_of_proc)
            begin = list_of_proc[0].Order
            periods = []
            pro = []
            ss = []
            i = 0
            while ((i < len(list_of_proc)) or (len(ss) != 0)):
                try:
                    if begin < list_of_proc[i].Order and len(ss) == 0:
                        begin = list_of_proc[i].Order
                except:
                    pass
                while i < len(list_of_proc):
                    if list_of_proc[i].Order <= begin:
                        ss.append(list_of_proc[i])
                    else:
                        break

                    i += 1
                bubble_sort_of_Time(ss)
                pro.append(ss[0].Name)
                t = ss[0].Time
                periods.append((begin, t))
                print((begin, t))
                begin += t
                ss.pop(0)

            periods.append((begin, 0))
            self.draw(periods, pro)
        else:
            bubble_sort_of_order(list_of_proc)
            begin = list_of_proc[0].Order
            periods = []
            pro = []
            ss = []
            s = []
            i = 0
            for i in range(len(list_of_proc)):
                s.append(list_of_proc[i].Order)
            b = set(s)
            s = list(b)
            bubble_sort_of(s)
            s.append(1000)
            i = 0
            for j in range(len(s)-1):
                while i < len(list_of_proc):
                    if s[j] == list_of_proc[i].Order:
                        ss.append(list_of_proc[i])
                    else:
                        break

                    i += 1
                while begin < s[j+1] and len(ss) != 0:
                    bubble_sort_of_Time(ss)
                    pro.append(ss[0].Name)
                    t = ss[0].Time
                    if begin + t <= s[j + 1]:
                        periods.append((begin, t))
                        print((begin, t))
                        begin += t
                        ss.pop(0)
                        #if (s[j+1] != 1000):
                         #   begin = s[j + 1]

                        if len(ss) == 0:
                            break
                    else:
                        rest = abs(s[j+1]-begin)
                        periods.append((begin, rest))
                        print((begin, rest))
                        rest2 = t- rest
                        ss[0] = CProcess(ss[0].Name,rest2,ss[0].Priority,ss[0].Order)
                        if s[j+1] == 1000:
                            break
                        begin = s[j+1]
                if begin < s[j+1] and s[j+1] != 1000:
                    begin = s[j + 1]

            periods.append((begin, 0))
            self.draw(periods, pro)

    def rr_m(self):
        bubble_sort_of_order(list_of_proc)
        begin = list_of_proc[0].Order
        periods = []
        pro = []
        ss = []
        rem = []
        for i in range(len(list_of_proc)):
            n = list_of_proc[i].Name
            tt = list_of_proc[i].Time
            pp = list_of_proc[i].Priority
            oo = list_of_proc[i].Order
            rem.append(CProcess(n,tt,pp,oo))

        begin = rem[0].Order
        flag = False
        while len(rem) > 0:

            if flag == True:
                for v in rem:
                    if v.Order <= begin:
                        break
                    else:
                        begin = v.Order
                        break

            i = 0
            while i < len(rem):
                if rem[i].Order > begin:
                    #i = (i+1) % len(rem)
                    i += 1
                    flag = True
                    continue
                if(rem[i].Time < self.time_q):
                    periods.append((begin , rem[i].Time))
                    begin += rem[i].Time
                    pro.append(rem[i].Name)
                    rem.pop(i)
                    if len(rem) == 0:
                        break
                    #i = (len(rem)-1+i) % len(rem)
                    flag = False
                else:
                    periods.append((begin, self.time_q))
                    begin += self.time_q
                    pro.append(rem[i].Name)
                    flag = False
                    rem[i].Time -= self.time_q
                    if rem[i].Time == 0:
                        rem.pop(i)
                        if len(rem) == 0:
                            break
                        #i = (len(rem) - 1 + i) % len(rem)

                #i = (i + 1) % len(rem)
                i += 1
        #print(len(pro))
        #print(len(periods))
        #for j in range(len(periods)):
         #   print(periods[j] , pro[j])
        periods.append((begin, 0))
        self.draw(periods,pro)

    def priority_m(self,p_type):
        for proc1 in list_of_proc:
            if proc1.Priority == None:

                msg = proc1.Name +"the priority is none"
                self.label_7.setText(error_str1 + msg + error_str2)
                self.label_7.show()
                return
        if p_type == "Non Preemptive":
            bubble_sort_of_order(list_of_proc)
            begin = list_of_proc[0].Order
            periods = []
            pro = []
            ss = []
            i = 0
            while ((i < len(list_of_proc)) or (len(ss) != 0)):
                try:
                    if begin < list_of_proc[i].Order and len(ss) == 0:
                        begin = list_of_proc[i].Order
                except:
                    pass
                while i < len(list_of_proc):
                    if list_of_proc[i].Order <= begin:
                        ss.append(list_of_proc[i])
                    else:
                        break

                    i += 1
                bubble_sort_of_Priority(ss)
                pro.append(ss[0].Name)
                t = ss[0].Time
                periods.append((begin, t))
                print((begin, t))
                begin += t
                ss.pop(0)

            periods.append((begin, 0))
            self.draw(periods, pro)
        else:
            bubble_sort_of_order(list_of_proc)
            begin = list_of_proc[0].Order
            periods = []
            pro = []
            ss = []
            s = []
            i = 0
            for i in range(len(list_of_proc)):
                s.append(list_of_proc[i].Order)
            b = set(s)
            s = list(b)
            s.append(1000)
            bubble_sort_of(s)
            i = 0
            for j in range(len(s)-1):
                while i < len(list_of_proc):
                    if s[j] == list_of_proc[i].Order:
                        ss.append(list_of_proc[i])
                    else:
                        break

                    i += 1
                while begin < s[j+1] and len(ss) != 0:
                    bubble_sort_of_Priority(ss)
                    pro.append(ss[0].Name)
                    t = ss[0].Time
                    if begin + t <= s[j + 1]:
                        periods.append((begin, t))
                        print((begin, t))
                        begin += t
                        ss.pop(0)
                        if len(ss) == 0:
                            break
                    else:
                        rest = abs(s[j+1]-begin)
                        periods.append((begin, rest))
                        print((begin, rest))
                        rest2 = t- rest
                        ss[0] = CProcess(ss[0].Name,rest2,ss[0].Priority,ss[0].Order)
                        if s[j+1] == 1000:
                            break
                        begin = s[j+1]
                if begin < s[j+1] and s[j+1] != 1000:
                    begin = s[j + 1]

            periods.append((begin, 0))
            self.draw(periods, pro)
def exception_hook(exctype, value, traceback):
    print(exctype, value, traceback)
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys._excepthook = sys.excepthook
    sys.excepthook = exception_hook
    sys.exit(app.exec_())
