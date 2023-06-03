from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
import cv2.aruco as aruco
import numpy as np
from PyQt5.QtWidgets import QFileDialog
from detect import HomoBgDtector


detector = HomoBgDtector()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # Adding Background
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 801, 601))
        self.label.setAutoFillBackground(False)
        self.label.setText("")
        self.label.setPixmap(
            QtGui.QPixmap("photo-1617118602031-1edde7582212.jpg")
            )
        self.label.setObjectName("label")
        # Add pushbutton for Live Capture
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.clicked.connect(self.livecapture)
        self.pushButton.setGeometry(QtCore.QRect(410, 120, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Mistral")
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("background-color: #e5e5e5")
        self.pushButton.setObjectName("pushButton")
        # Add pushbutton for Browsing Image
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.clicked.connect(self.browse)
        self.pushButton_2.setGeometry(QtCore.QRect(190, 120, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Mistral")
        font.setPointSize(12)
        font.setItalic(False)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: #e5e5e5\n")
        self.pushButton_2.setObjectName("pushButton_2")
        # Giving Title
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(240, 30, 291, 51))
        font = QtGui.QFont()
        font.setFamily("Papyrus")
        font.setPointSize(26)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow",
                                             "MainWindow"))
        self.pushButton.setText(_translate("MainWindow",
                                           "Live Capturing"))
        self.pushButton_2.setText(_translate("MainWindow",
                                             "Browse for Pictures"))
        self.label_2.setText(_translate("MainWindow", "MeasureCraft"))
    
        
    
        
        
        

        
        
