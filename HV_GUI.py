# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HV_GUI.ui'
#
# Created: Thu Jul  7 15:14:09 2016
#      by: PyQt4 UI code generator 4.6.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(939, 731)
        self.MainWindow_2 = QtGui.QWidget(MainWindow)
        self.MainWindow_2.setObjectName("MainWindow_2")
        self.main_title = QtGui.QLabel(self.MainWindow_2)
        self.main_title.setGeometry(QtCore.QRect(200, 60, 511, 31))
        self.main_title.setObjectName("main_title")
        self.P_0 = QtGui.QCheckBox(self.MainWindow_2)
        self.P_0.setGeometry(QtCore.QRect(110, 190, 93, 22))
        self.P_0.setObjectName("P_0")
        self.P_2 = QtGui.QCheckBox(self.MainWindow_2)
        self.P_2.setGeometry(QtCore.QRect(110, 250, 93, 22))
        self.P_2.setObjectName("P_2")
        self.P_3 = QtGui.QCheckBox(self.MainWindow_2)
        self.P_3.setGeometry(QtCore.QRect(110, 280, 93, 22))
        self.P_3.setObjectName("P_3")
        self.P_4 = QtGui.QCheckBox(self.MainWindow_2)
        self.P_4.setGeometry(QtCore.QRect(110, 310, 93, 22))
        self.P_4.setObjectName("P_4")
        self.P_5 = QtGui.QCheckBox(self.MainWindow_2)
        self.P_5.setGeometry(QtCore.QRect(110, 340, 93, 22))
        self.P_5.setObjectName("P_5")
        self.P_6 = QtGui.QCheckBox(self.MainWindow_2)
        self.P_6.setGeometry(QtCore.QRect(110, 370, 93, 22))
        self.P_6.setObjectName("P_6")
        self.P_7 = QtGui.QCheckBox(self.MainWindow_2)
        self.P_7.setGeometry(QtCore.QRect(110, 400, 93, 22))
        self.P_7.setObjectName("P_7")
        self.P_8 = QtGui.QCheckBox(self.MainWindow_2)
        self.P_8.setGeometry(QtCore.QRect(110, 430, 93, 22))
        self.P_8.setObjectName("P_8")
        self.V0_t = QtGui.QLabel(self.MainWindow_2)
        self.V0_t.setGeometry(QtCore.QRect(370, 160, 71, 21))
        self.V0_t.setObjectName("V0_t")
        self.I0_t = QtGui.QLabel(self.MainWindow_2)
        self.I0_t.setGeometry(QtCore.QRect(470, 160, 71, 21))
        self.I0_t.setObjectName("I0_t")
        self.VMon_t = QtGui.QLabel(self.MainWindow_2)
        self.VMon_t.setGeometry(QtCore.QRect(200, 160, 71, 21))
        self.VMon_t.setObjectName("VMon_t")
        self.IMon_t = QtGui.QLabel(self.MainWindow_2)
        self.IMon_t.setGeometry(QtCore.QRect(280, 160, 71, 21))
        self.IMon_t.setObjectName("IMon_t")
        self.RUP_t = QtGui.QLabel(self.MainWindow_2)
        self.RUP_t.setGeometry(QtCore.QRect(560, 160, 81, 21))
        self.RUP_t.setObjectName("RUP_t")
        self.RDN_t = QtGui.QLabel(self.MainWindow_2)
        self.RDN_t.setGeometry(QtCore.QRect(650, 160, 101, 21))
        self.RDN_t.setObjectName("RDN_t")
        self.trip_t = QtGui.QLabel(self.MainWindow_2)
        self.trip_t.setGeometry(QtCore.QRect(770, 160, 71, 21))
        self.trip_t.setObjectName("trip_t")
        self.CH_t = QtGui.QLabel(self.MainWindow_2)
        self.CH_t.setGeometry(QtCore.QRect(10, 160, 81, 21))
        self.CH_t.setObjectName("CH_t")
        self.P_t = QtGui.QLabel(self.MainWindow_2)
        self.P_t.setGeometry(QtCore.QRect(110, 160, 71, 21))
        self.P_t.setObjectName("P_t")
        self.V0_0 = QtGui.QLineEdit(self.MainWindow_2)
        self.V0_0.setGeometry(QtCore.QRect(370, 190, 71, 26))
        self.V0_0.setObjectName("V0_0")
        self.V0_2 = QtGui.QLineEdit(self.MainWindow_2)
        self.V0_2.setGeometry(QtCore.QRect(370, 250, 71, 26))
        self.V0_2.setObjectName("V0_2")
        self.V0_3 = QtGui.QLineEdit(self.MainWindow_2)
        self.V0_3.setGeometry(QtCore.QRect(370, 280, 71, 26))
        self.V0_3.setObjectName("V0_3")
        self.V0_4 = QtGui.QLineEdit(self.MainWindow_2)
        self.V0_4.setGeometry(QtCore.QRect(370, 310, 71, 26))
        self.V0_4.setObjectName("V0_4")
        self.V0_5 = QtGui.QLineEdit(self.MainWindow_2)
        self.V0_5.setGeometry(QtCore.QRect(370, 340, 71, 26))
        self.V0_5.setObjectName("V0_5")
        self.V0_6 = QtGui.QLineEdit(self.MainWindow_2)
        self.V0_6.setGeometry(QtCore.QRect(370, 370, 71, 26))
        self.V0_6.setObjectName("V0_6")
        self.V0_7 = QtGui.QLineEdit(self.MainWindow_2)
        self.V0_7.setGeometry(QtCore.QRect(370, 400, 71, 26))
        self.V0_7.setObjectName("V0_7")
        self.V0_8 = QtGui.QLineEdit(self.MainWindow_2)
        self.V0_8.setGeometry(QtCore.QRect(370, 430, 71, 26))
        self.V0_8.setObjectName("V0_8")
        self.I0_5 = QtGui.QLineEdit(self.MainWindow_2)
        self.I0_5.setGeometry(QtCore.QRect(470, 340, 71, 26))
        self.I0_5.setObjectName("I0_5")
        self.I0_8 = QtGui.QLineEdit(self.MainWindow_2)
        self.I0_8.setGeometry(QtCore.QRect(470, 430, 71, 26))
        self.I0_8.setObjectName("I0_8")
        self.I0_4 = QtGui.QLineEdit(self.MainWindow_2)
        self.I0_4.setGeometry(QtCore.QRect(470, 310, 71, 26))
        self.I0_4.setObjectName("I0_4")
        self.I0_0 = QtGui.QLineEdit(self.MainWindow_2)
        self.I0_0.setGeometry(QtCore.QRect(470, 190, 71, 26))
        self.I0_0.setObjectName("I0_0")
        self.I0_2 = QtGui.QLineEdit(self.MainWindow_2)
        self.I0_2.setGeometry(QtCore.QRect(470, 250, 71, 26))
        self.I0_2.setObjectName("I0_2")
        self.I0_6 = QtGui.QLineEdit(self.MainWindow_2)
        self.I0_6.setGeometry(QtCore.QRect(470, 370, 71, 26))
        self.I0_6.setObjectName("I0_6")
        self.I0_7 = QtGui.QLineEdit(self.MainWindow_2)
        self.I0_7.setGeometry(QtCore.QRect(470, 400, 71, 26))
        self.I0_7.setObjectName("I0_7")
        self.I0_3 = QtGui.QLineEdit(self.MainWindow_2)
        self.I0_3.setGeometry(QtCore.QRect(470, 280, 71, 26))
        self.I0_3.setObjectName("I0_3")
        self.RUP_5 = QtGui.QLineEdit(self.MainWindow_2)
        self.RUP_5.setGeometry(QtCore.QRect(570, 340, 71, 26))
        self.RUP_5.setObjectName("RUP_5")
        self.RUP_8 = QtGui.QLineEdit(self.MainWindow_2)
        self.RUP_8.setGeometry(QtCore.QRect(570, 430, 71, 26))
        self.RUP_8.setObjectName("RUP_8")
        self.RUP_4 = QtGui.QLineEdit(self.MainWindow_2)
        self.RUP_4.setGeometry(QtCore.QRect(570, 310, 71, 26))
        self.RUP_4.setObjectName("RUP_4")
        self.RUP_0 = QtGui.QLineEdit(self.MainWindow_2)
        self.RUP_0.setGeometry(QtCore.QRect(570, 190, 71, 26))
        self.RUP_0.setObjectName("RUP_0")
        self.RUP_2 = QtGui.QLineEdit(self.MainWindow_2)
        self.RUP_2.setGeometry(QtCore.QRect(570, 250, 71, 26))
        self.RUP_2.setObjectName("RUP_2")
        self.RUP_6 = QtGui.QLineEdit(self.MainWindow_2)
        self.RUP_6.setGeometry(QtCore.QRect(570, 370, 71, 26))
        self.RUP_6.setObjectName("RUP_6")
        self.RUP_7 = QtGui.QLineEdit(self.MainWindow_2)
        self.RUP_7.setGeometry(QtCore.QRect(570, 400, 71, 26))
        self.RUP_7.setObjectName("RUP_7")
        self.RUP_3 = QtGui.QLineEdit(self.MainWindow_2)
        self.RUP_3.setGeometry(QtCore.QRect(570, 280, 71, 26))
        self.RUP_3.setObjectName("RUP_3")
        self.RDN_5 = QtGui.QLineEdit(self.MainWindow_2)
        self.RDN_5.setGeometry(QtCore.QRect(670, 340, 71, 26))
        self.RDN_5.setObjectName("RDN_5")
        self.RDN_8 = QtGui.QLineEdit(self.MainWindow_2)
        self.RDN_8.setGeometry(QtCore.QRect(670, 430, 71, 26))
        self.RDN_8.setObjectName("RDN_8")
        self.RDN_4 = QtGui.QLineEdit(self.MainWindow_2)
        self.RDN_4.setGeometry(QtCore.QRect(670, 310, 71, 26))
        self.RDN_4.setObjectName("RDN_4")
        self.RDN_0 = QtGui.QLineEdit(self.MainWindow_2)
        self.RDN_0.setGeometry(QtCore.QRect(670, 190, 71, 26))
        self.RDN_0.setObjectName("RDN_0")
        self.RDN_2 = QtGui.QLineEdit(self.MainWindow_2)
        self.RDN_2.setGeometry(QtCore.QRect(670, 250, 71, 26))
        self.RDN_2.setObjectName("RDN_2")
        self.RDN_6 = QtGui.QLineEdit(self.MainWindow_2)
        self.RDN_6.setGeometry(QtCore.QRect(670, 370, 71, 26))
        self.RDN_6.setObjectName("RDN_6")
        self.RDN_7 = QtGui.QLineEdit(self.MainWindow_2)
        self.RDN_7.setGeometry(QtCore.QRect(670, 400, 71, 26))
        self.RDN_7.setObjectName("RDN_7")
        self.RDN_3 = QtGui.QLineEdit(self.MainWindow_2)
        self.RDN_3.setGeometry(QtCore.QRect(670, 280, 71, 26))
        self.RDN_3.setObjectName("RDN_3")
        self.trip_5 = QtGui.QLineEdit(self.MainWindow_2)
        self.trip_5.setGeometry(QtCore.QRect(770, 340, 71, 26))
        self.trip_5.setObjectName("trip_5")
        self.trip_8 = QtGui.QLineEdit(self.MainWindow_2)
        self.trip_8.setGeometry(QtCore.QRect(770, 430, 71, 26))
        self.trip_8.setObjectName("trip_8")
        self.trip_4 = QtGui.QLineEdit(self.MainWindow_2)
        self.trip_4.setGeometry(QtCore.QRect(770, 310, 71, 26))
        self.trip_4.setObjectName("trip_4")
        self.trip_0 = QtGui.QLineEdit(self.MainWindow_2)
        self.trip_0.setGeometry(QtCore.QRect(770, 190, 71, 26))
        self.trip_0.setObjectName("trip_0")
        self.trip_2 = QtGui.QLineEdit(self.MainWindow_2)
        self.trip_2.setGeometry(QtCore.QRect(770, 250, 71, 26))
        self.trip_2.setObjectName("trip_2")
        self.trip_6 = QtGui.QLineEdit(self.MainWindow_2)
        self.trip_6.setGeometry(QtCore.QRect(770, 370, 71, 26))
        self.trip_6.setObjectName("trip_6")
        self.trip_7 = QtGui.QLineEdit(self.MainWindow_2)
        self.trip_7.setGeometry(QtCore.QRect(770, 400, 71, 26))
        self.trip_7.setObjectName("trip_7")
        self.trip_3 = QtGui.QLineEdit(self.MainWindow_2)
        self.trip_3.setGeometry(QtCore.QRect(770, 280, 71, 26))
        self.trip_3.setObjectName("trip_3")
        self.kill_button = QtGui.QPushButton(self.MainWindow_2)
        self.kill_button.setGeometry(QtCore.QRect(520, 470, 92, 41))
        self.kill_button.setObjectName("kill_button")
        self.gm2_logo = QtGui.QLabel(self.MainWindow_2)
        self.gm2_logo.setGeometry(QtCore.QRect(750, 10, 130, 120))
        self.gm2_logo.setPixmap(QtGui.QPixmap("/home/g2uol/Desktop/HV_GUI/gm2logo2.png"))
        self.gm2_logo.setScaledContents(True)
        self.gm2_logo.setObjectName("gm2_logo")
        self.UOL_logo = QtGui.QLabel(self.MainWindow_2)
        self.UOL_logo.setGeometry(QtCore.QRect(40, 20, 120, 120))
        self.UOL_logo.setPixmap(QtGui.QPixmap("/home/g2uol/Desktop/HV_GUI/UNIVERSITY_OF_LIVERPOOL_COAT_OF_ARMS.png"))
        self.UOL_logo.setScaledContents(True)
        self.UOL_logo.setObjectName("UOL_logo")
        self.VMon_0 = QtGui.QLabel(self.MainWindow_2)
        self.VMon_0.setGeometry(QtCore.QRect(201, 190, 71, 20))
        self.VMon_0.setObjectName("VMon_0")
        self.VMon_2 = QtGui.QLabel(self.MainWindow_2)
        self.VMon_2.setGeometry(QtCore.QRect(201, 250, 71, 20))
        self.VMon_2.setObjectName("VMon_2")
        self.VMon_3 = QtGui.QLabel(self.MainWindow_2)
        self.VMon_3.setGeometry(QtCore.QRect(201, 280, 71, 20))
        self.VMon_3.setObjectName("VMon_3")
        self.VMon_4 = QtGui.QLabel(self.MainWindow_2)
        self.VMon_4.setGeometry(QtCore.QRect(201, 310, 71, 20))
        self.VMon_4.setObjectName("VMon_4")
        self.VMon_5 = QtGui.QLabel(self.MainWindow_2)
        self.VMon_5.setGeometry(QtCore.QRect(201, 340, 71, 20))
        self.VMon_5.setObjectName("VMon_5")
        self.VMon_7 = QtGui.QLabel(self.MainWindow_2)
        self.VMon_7.setGeometry(QtCore.QRect(201, 400, 71, 20))
        self.VMon_7.setObjectName("VMon_7")
        self.VMon_6 = QtGui.QLabel(self.MainWindow_2)
        self.VMon_6.setGeometry(QtCore.QRect(201, 370, 71, 20))
        self.VMon_6.setObjectName("VMon_6")
        self.VMon_8 = QtGui.QLabel(self.MainWindow_2)
        self.VMon_8.setGeometry(QtCore.QRect(201, 430, 71, 20))
        self.VMon_8.setObjectName("VMon_8")
        self.IMon_2 = QtGui.QLabel(self.MainWindow_2)
        self.IMon_2.setGeometry(QtCore.QRect(281, 250, 71, 20))
        self.IMon_2.setObjectName("IMon_2")
        self.IMon_3 = QtGui.QLabel(self.MainWindow_2)
        self.IMon_3.setGeometry(QtCore.QRect(281, 280, 71, 20))
        self.IMon_3.setObjectName("IMon_3")
        self.IMon_6 = QtGui.QLabel(self.MainWindow_2)
        self.IMon_6.setGeometry(QtCore.QRect(281, 370, 71, 20))
        self.IMon_6.setObjectName("IMon_6")
        self.IMon_5 = QtGui.QLabel(self.MainWindow_2)
        self.IMon_5.setGeometry(QtCore.QRect(281, 340, 71, 20))
        self.IMon_5.setObjectName("IMon_5")
        self.IMon_7 = QtGui.QLabel(self.MainWindow_2)
        self.IMon_7.setGeometry(QtCore.QRect(281, 400, 71, 20))
        self.IMon_7.setObjectName("IMon_7")
        self.IMon_4 = QtGui.QLabel(self.MainWindow_2)
        self.IMon_4.setGeometry(QtCore.QRect(281, 310, 71, 20))
        self.IMon_4.setObjectName("IMon_4")
        self.IMon_0 = QtGui.QLabel(self.MainWindow_2)
        self.IMon_0.setGeometry(QtCore.QRect(281, 190, 71, 20))
        self.IMon_0.setObjectName("IMon_0")
        self.IMon_8 = QtGui.QLabel(self.MainWindow_2)
        self.IMon_8.setGeometry(QtCore.QRect(281, 430, 71, 20))
        self.IMon_8.setObjectName("IMon_8")
        self.set_button = QtGui.QPushButton(self.MainWindow_2)
        self.set_button.setGeometry(QtCore.QRect(280, 470, 92, 41))
        self.set_button.setObjectName("set_button")
        self.send_button = QtGui.QPushButton(self.MainWindow_2)
        self.send_button.setEnabled(False)
        self.send_button.setGeometry(QtCore.QRect(400, 470, 92, 41))
        self.send_button.setObjectName("send_button")
        self.CH_2 = QtGui.QLabel(self.MainWindow_2)
        self.CH_2.setGeometry(QtCore.QRect(20, 250, 62, 16))
        self.CH_2.setObjectName("CH_2")
        self.CH_3 = QtGui.QLabel(self.MainWindow_2)
        self.CH_3.setGeometry(QtCore.QRect(20, 280, 62, 16))
        self.CH_3.setObjectName("CH_3")
        self.CH_6 = QtGui.QLabel(self.MainWindow_2)
        self.CH_6.setGeometry(QtCore.QRect(20, 370, 62, 16))
        self.CH_6.setObjectName("CH_6")
        self.CH_5 = QtGui.QLabel(self.MainWindow_2)
        self.CH_5.setGeometry(QtCore.QRect(20, 340, 62, 16))
        self.CH_5.setObjectName("CH_5")
        self.CH_7 = QtGui.QLabel(self.MainWindow_2)
        self.CH_7.setGeometry(QtCore.QRect(20, 400, 62, 16))
        self.CH_7.setObjectName("CH_7")
        self.CH_4 = QtGui.QLabel(self.MainWindow_2)
        self.CH_4.setGeometry(QtCore.QRect(20, 310, 62, 16))
        self.CH_4.setObjectName("CH_4")
        self.CH_0 = QtGui.QLabel(self.MainWindow_2)
        self.CH_0.setGeometry(QtCore.QRect(20, 190, 62, 16))
        self.CH_0.setObjectName("CH_0")
        self.CH_8 = QtGui.QLabel(self.MainWindow_2)
        self.CH_8.setGeometry(QtCore.QRect(20, 430, 62, 16))
        self.CH_8.setObjectName("CH_8")
        self.connect_button = QtGui.QPushButton(self.MainWindow_2)
        self.connect_button.setGeometry(QtCore.QRect(40, 470, 92, 41))
        self.connect_button.setObjectName("connect_button")
        self.listWidget = QtGui.QTextBrowser(self.MainWindow_2)
        self.listWidget.setEnabled(True)
        self.listWidget.setGeometry(QtCore.QRect(40, 530, 861, 181))
        self.listWidget.setObjectName("listWidget")
        self.S_6 = QtGui.QLabel(self.MainWindow_2)
        self.S_6.setGeometry(QtCore.QRect(850, 370, 71, 20))
        self.S_6.setObjectName("S_6")
        self.S_8 = QtGui.QLabel(self.MainWindow_2)
        self.S_8.setGeometry(QtCore.QRect(850, 430, 71, 20))
        self.S_8.setObjectName("S_8")
        self.S_5 = QtGui.QLabel(self.MainWindow_2)
        self.S_5.setGeometry(QtCore.QRect(850, 340, 71, 20))
        self.S_5.setObjectName("S_5")
        self.S_t = QtGui.QLabel(self.MainWindow_2)
        self.S_t.setGeometry(QtCore.QRect(849, 160, 71, 21))
        self.S_t.setObjectName("S_t")
        self.S_4 = QtGui.QLabel(self.MainWindow_2)
        self.S_4.setGeometry(QtCore.QRect(850, 310, 71, 20))
        self.S_4.setObjectName("S_4")
        self.S_2 = QtGui.QLabel(self.MainWindow_2)
        self.S_2.setGeometry(QtCore.QRect(850, 250, 71, 20))
        self.S_2.setObjectName("S_2")
        self.S_7 = QtGui.QLabel(self.MainWindow_2)
        self.S_7.setGeometry(QtCore.QRect(850, 400, 71, 20))
        self.S_7.setObjectName("S_7")
        self.S_0 = QtGui.QLabel(self.MainWindow_2)
        self.S_0.setGeometry(QtCore.QRect(850, 190, 71, 20))
        self.S_0.setObjectName("S_0")
        self.S_3 = QtGui.QLabel(self.MainWindow_2)
        self.S_3.setGeometry(QtCore.QRect(850, 280, 71, 20))
        self.S_3.setObjectName("S_3")
        self.disconnect_button = QtGui.QPushButton(self.MainWindow_2)
        self.disconnect_button.setGeometry(QtCore.QRect(160, 470, 92, 41))
        self.disconnect_button.setObjectName("disconnect_button")
        self.exit_button = QtGui.QPushButton(self.MainWindow_2)
        self.exit_button.setGeometry(QtCore.QRect(640, 470, 92, 41))
        self.exit_button.setObjectName("exit_button")
        self.RUP_1 = QtGui.QLineEdit(self.MainWindow_2)
        self.RUP_1.setEnabled(False)
        self.RUP_1.setGeometry(QtCore.QRect(570, 220, 71, 26))
        self.RUP_1.setObjectName("RUP_1")
        self.VMon_1 = QtGui.QLabel(self.MainWindow_2)
        self.VMon_1.setEnabled(False)
        self.VMon_1.setGeometry(QtCore.QRect(201, 220, 71, 20))
        self.VMon_1.setObjectName("VMon_1")
        self.RDN_1 = QtGui.QLineEdit(self.MainWindow_2)
        self.RDN_1.setEnabled(False)
        self.RDN_1.setGeometry(QtCore.QRect(670, 220, 71, 26))
        self.RDN_1.setObjectName("RDN_1")
        self.I0_1 = QtGui.QLineEdit(self.MainWindow_2)
        self.I0_1.setEnabled(False)
        self.I0_1.setGeometry(QtCore.QRect(470, 220, 71, 26))
        self.I0_1.setObjectName("I0_1")
        self.IMon_1 = QtGui.QLabel(self.MainWindow_2)
        self.IMon_1.setEnabled(False)
        self.IMon_1.setGeometry(QtCore.QRect(281, 220, 71, 20))
        self.IMon_1.setObjectName("IMon_1")
        self.S_1 = QtGui.QLabel(self.MainWindow_2)
        self.S_1.setEnabled(False)
        self.S_1.setGeometry(QtCore.QRect(850, 220, 71, 20))
        self.S_1.setObjectName("S_1")
        self.trip_1 = QtGui.QLineEdit(self.MainWindow_2)
        self.trip_1.setEnabled(False)
        self.trip_1.setGeometry(QtCore.QRect(770, 220, 71, 26))
        self.trip_1.setObjectName("trip_1")
        self.P_1 = QtGui.QCheckBox(self.MainWindow_2)
        self.P_1.setEnabled(False)
        self.P_1.setGeometry(QtCore.QRect(110, 220, 93, 22))
        self.P_1.setObjectName("P_1")
        self.V0_1 = QtGui.QLineEdit(self.MainWindow_2)
        self.V0_1.setEnabled(False)
        self.V0_1.setGeometry(QtCore.QRect(370, 220, 71, 26))
        self.V0_1.setObjectName("V0_1")
        self.CH_1 = QtGui.QLabel(self.MainWindow_2)
        self.CH_1.setEnabled(False)
        self.CH_1.setGeometry(QtCore.QRect(20, 220, 62, 16))
        self.CH_1.setObjectName("CH_1")
        self.time = QtGui.QLabel(self.MainWindow_2)
        self.time.setGeometry(QtCore.QRect(540, 110, 71, 20))
        self.time.setObjectName("time")
        self.time_label = QtGui.QLabel(self.MainWindow_2)
        self.time_label.setGeometry(QtCore.QRect(470, 110, 71, 21))
        self.time_label.setObjectName("time_label")
        self.date_label = QtGui.QLabel(self.MainWindow_2)
        self.date_label.setGeometry(QtCore.QRect(290, 110, 71, 21))
        self.date_label.setObjectName("date_label")
        self.date = QtGui.QLabel(self.MainWindow_2)
        self.date.setGeometry(QtCore.QRect(360, 110, 91, 20))
        self.date.setObjectName("date")
        self.line = QtGui.QFrame(self.MainWindow_2)
        self.line.setGeometry(QtCore.QRect(460, 100, 20, 31))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.plotly_button = QtGui.QPushButton(self.MainWindow_2)
        self.plotly_button.setGeometry(QtCore.QRect(760, 470, 92, 41))
        self.plotly_button.setObjectName("plotly_button")
        self.expand_button = QtGui.QToolButton(self.MainWindow_2)
        self.expand_button.setGeometry(QtCore.QRect(880, 480, 26, 25))
        self.expand_button.setObjectName("expand_button")
        MainWindow.setCentralWidget(self.MainWindow_2)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.P_0, self.P_2)
        MainWindow.setTabOrder(self.P_2, self.P_3)
        MainWindow.setTabOrder(self.P_3, self.P_4)
        MainWindow.setTabOrder(self.P_4, self.P_5)
        MainWindow.setTabOrder(self.P_5, self.P_6)
        MainWindow.setTabOrder(self.P_6, self.P_7)
        MainWindow.setTabOrder(self.P_7, self.P_8)
        MainWindow.setTabOrder(self.P_8, self.V0_0)
        MainWindow.setTabOrder(self.V0_0, self.V0_2)
        MainWindow.setTabOrder(self.V0_2, self.V0_3)
        MainWindow.setTabOrder(self.V0_3, self.V0_4)
        MainWindow.setTabOrder(self.V0_4, self.V0_5)
        MainWindow.setTabOrder(self.V0_5, self.V0_6)
        MainWindow.setTabOrder(self.V0_6, self.V0_7)
        MainWindow.setTabOrder(self.V0_7, self.V0_8)
        MainWindow.setTabOrder(self.V0_8, self.I0_0)
        MainWindow.setTabOrder(self.I0_0, self.I0_2)
        MainWindow.setTabOrder(self.I0_2, self.I0_3)
        MainWindow.setTabOrder(self.I0_3, self.I0_4)
        MainWindow.setTabOrder(self.I0_4, self.I0_5)
        MainWindow.setTabOrder(self.I0_5, self.I0_6)
        MainWindow.setTabOrder(self.I0_6, self.I0_7)
        MainWindow.setTabOrder(self.I0_7, self.I0_8)
        MainWindow.setTabOrder(self.I0_8, self.RUP_0)
        MainWindow.setTabOrder(self.RUP_0, self.RUP_2)
        MainWindow.setTabOrder(self.RUP_2, self.RUP_3)
        MainWindow.setTabOrder(self.RUP_3, self.RUP_4)
        MainWindow.setTabOrder(self.RUP_4, self.RUP_5)
        MainWindow.setTabOrder(self.RUP_5, self.RUP_6)
        MainWindow.setTabOrder(self.RUP_6, self.RUP_7)
        MainWindow.setTabOrder(self.RUP_7, self.RUP_8)
        MainWindow.setTabOrder(self.RUP_8, self.RDN_0)
        MainWindow.setTabOrder(self.RDN_0, self.RDN_2)
        MainWindow.setTabOrder(self.RDN_2, self.RDN_3)
        MainWindow.setTabOrder(self.RDN_3, self.RDN_4)
        MainWindow.setTabOrder(self.RDN_4, self.RDN_5)
        MainWindow.setTabOrder(self.RDN_5, self.RDN_6)
        MainWindow.setTabOrder(self.RDN_6, self.RDN_7)
        MainWindow.setTabOrder(self.RDN_7, self.RDN_8)
        MainWindow.setTabOrder(self.RDN_8, self.trip_0)
        MainWindow.setTabOrder(self.trip_0, self.trip_2)
        MainWindow.setTabOrder(self.trip_2, self.trip_3)
        MainWindow.setTabOrder(self.trip_3, self.trip_4)
        MainWindow.setTabOrder(self.trip_4, self.trip_5)
        MainWindow.setTabOrder(self.trip_5, self.trip_6)
        MainWindow.setTabOrder(self.trip_6, self.trip_7)
        MainWindow.setTabOrder(self.trip_7, self.trip_8)
        MainWindow.setTabOrder(self.trip_8, self.set_button)
        MainWindow.setTabOrder(self.set_button, self.send_button)
        MainWindow.setTabOrder(self.send_button, self.kill_button)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.main_title.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\">CAEN SY127 High Voltage System</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.P_0.setText(QtGui.QApplication.translate("MainWindow", "On/Off", None, QtGui.QApplication.UnicodeUTF8))
        self.P_2.setText(QtGui.QApplication.translate("MainWindow", "On/Off", None, QtGui.QApplication.UnicodeUTF8))
        self.P_3.setText(QtGui.QApplication.translate("MainWindow", "On/Off", None, QtGui.QApplication.UnicodeUTF8))
        self.P_4.setText(QtGui.QApplication.translate("MainWindow", "On/Off", None, QtGui.QApplication.UnicodeUTF8))
        self.P_5.setText(QtGui.QApplication.translate("MainWindow", "On/Off", None, QtGui.QApplication.UnicodeUTF8))
        self.P_6.setText(QtGui.QApplication.translate("MainWindow", "On/Off", None, QtGui.QApplication.UnicodeUTF8))
        self.P_7.setText(QtGui.QApplication.translate("MainWindow", "On/Off", None, QtGui.QApplication.UnicodeUTF8))
        self.P_8.setText(QtGui.QApplication.translate("MainWindow", "On/Off", None, QtGui.QApplication.UnicodeUTF8))
        self.V0_t.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">V0</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.I0_t.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">I0</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.VMon_t.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">VMon</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.IMon_t.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">IMon</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.RUP_t.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Ramp Up</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.RDN_t.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Ramp Down</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.trip_t.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Trip</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.CH_t.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Channel </span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.P_t.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Power</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.kill_button.setToolTip(QtGui.QApplication.translate("MainWindow", "Kill ", None, QtGui.QApplication.UnicodeUTF8))
        self.kill_button.setText(QtGui.QApplication.translate("MainWindow", "Kill", None, QtGui.QApplication.UnicodeUTF8))
        self.VMon_0.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.VMon_2.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.VMon_3.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.VMon_4.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.VMon_5.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.VMon_7.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.VMon_6.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.VMon_8.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.IMon_2.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.IMon_3.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.IMon_6.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.IMon_5.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.IMon_7.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.IMon_4.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.IMon_0.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.IMon_8.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.set_button.setText(QtGui.QApplication.translate("MainWindow", "Set", None, QtGui.QApplication.UnicodeUTF8))
        self.send_button.setText(QtGui.QApplication.translate("MainWindow", "Send", None, QtGui.QApplication.UnicodeUTF8))
        self.CH_2.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.CH_3.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.CH_6.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">6</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.CH_5.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">5</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.CH_7.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">7</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.CH_4.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">4</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.CH_0.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.CH_8.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">8</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.connect_button.setText(QtGui.QApplication.translate("MainWindow", "Connect", None, QtGui.QApplication.UnicodeUTF8))
        self.S_6.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">NULL</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.S_8.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">NULL</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.S_5.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">NULL</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.S_t.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Status</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.S_4.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">NULL</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.S_2.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">NULL</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.S_7.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">NULL</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.S_0.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">NULL</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.S_3.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">NULL</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.disconnect_button.setText(QtGui.QApplication.translate("MainWindow", "Disconnect", None, QtGui.QApplication.UnicodeUTF8))
        self.exit_button.setToolTip(QtGui.QApplication.translate("MainWindow", "Kill ", None, QtGui.QApplication.UnicodeUTF8))
        self.exit_button.setText(QtGui.QApplication.translate("MainWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.VMon_1.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.IMon_1.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.S_1.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">NULL</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.P_1.setText(QtGui.QApplication.translate("MainWindow", "On/Off", None, QtGui.QApplication.UnicodeUTF8))
        self.CH_1.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.time.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">00:00:00</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.time_label.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Time</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.date_label.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Date</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.date.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">00/00/0000</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.plotly_button.setToolTip(QtGui.QApplication.translate("MainWindow", "Kill ", None, QtGui.QApplication.UnicodeUTF8))
        self.plotly_button.setText(QtGui.QApplication.translate("MainWindow", "Plotly", None, QtGui.QApplication.UnicodeUTF8))
        self.expand_button.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))

