import sys
import io
import folium # pip install folium
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView # pip install PyQtWebEngine
from PyQt5 import QtCore, QtGui, QtWidgets
from gauge import AnalogGaugeWidget
from PyQt5.QtCore import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from qtwidgets import *
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer

# import Opencv module
import cv2
import random
from datetime import datetime
import requests
# from ArduinoSensor_data import get_live_data, save_data_to_file, print_data
from read_data_from_file import read_data_from_file, print_file_data

# import ArduinoSensor_data
                # ArduinoSensor_data.main()     # This will run the main function in ArduinoSensor_data.py
                # ArduinoSensor_data.request_data() # This will run the request_data function in ArduinoSensor_data.py
# custom 
import weather
import getlocation
  
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1117, 636)
        # MainWindow.showFullScreen()  # This makes the window full-screen

        MainWindow.setStyleSheet("background-color: rgb(30, 31, 40);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1111, 651))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/bg/Untitled (1).png"))
        self.label.setScaledContents(True)
        
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(306, 60, 521, 61))
        self.frame.setStyleSheet("QFrame{\n"
                "background:None;\n"
                "}\n"
                "\n"
                "QPushButton{\n"
                "    \n"
                "    background-color: rgb(43,87,151,70);\n"
                "    border:None;\n"
                "    color:#fff;\n"
                "    font: 10pt;\n"
                "\n"
                "}\n"
                "QPushButton:Hover{\n"
                "\n"
                "    \n"
                "    background-color: rgba(43,87,151,120);\n"
                "\n"
                "\n"
                "}\n"
                "\n"
                "QPushButton:Pressed{\n"
                "    \n"
                "    \n"
                "background-color: rgba(43,87,120,100);\n"
                "\n"
                "}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_dash = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_dash.sizePolicy().hasHeightForWidth())
        self.btn_dash.setSizePolicy(sizePolicy)
        
        self.btn_dash.setObjectName("btn_dash")
        self.horizontalLayout.addWidget(self.btn_dash)
        self.btn_ac = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_ac.sizePolicy().hasHeightForWidth())
        self.btn_ac.setSizePolicy(sizePolicy)
        
        self.btn_ac.setObjectName("btn_ac")
        self.horizontalLayout.addWidget(self.btn_ac)
        self.btn_music = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_music.sizePolicy().hasHeightForWidth())
        self.btn_music.setSizePolicy(sizePolicy)
        
        self.btn_music.setObjectName("btn_music")
        self.horizontalLayout.addWidget(self.btn_music)
        self.btn_map = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_map.sizePolicy().hasHeightForWidth())
        self.btn_map.setSizePolicy(sizePolicy)
        self.btn_map.setObjectName("btn_map")
        self.horizontalLayout.addWidget(self.btn_map)
        
        self.frame_dashboard = QtWidgets.QFrame(self.centralwidget)
        self.frame_dashboard.setEnabled(True)
        self.frame_dashboard.setGeometry(QtCore.QRect(70, 120, 971, 411))
        self.frame_dashboard.setStyleSheet("QFrame{\n"
                "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(34, 46, 61), stop:1 rgba(34, 34, 47));\n"
                "\n"
                "border-radius:200px;\n"
                "\n"
                "}")
        self.frame_dashboard.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_dashboard.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_dashboard.setObjectName("frame_dashboard")
        
        self.speed = AnalogGaugeWidget(self.frame_dashboard)
        self.speed.setGeometry(QtCore.QRect(30, 50, 311, 281))
        self.speed.setStyleSheet("background-color: rgb(85, 85, 127);\n"
                "border-radius: 0px;")
        self.speed.setObjectName("speed")
        self.rpm = AnalogGaugeWidget(self.frame_dashboard)
        self.rpm.setGeometry(QtCore.QRect(630, 50, 311, 281))
        self.rpm.setStyleSheet("background-color: rgb(85, 85, 127);\n"
                "border-radius: 0px;")
        self.rpm.setObjectName("rpm")
        self.frame_2 = QtWidgets.QFrame(self.frame_dashboard)
        self.frame_2.setGeometry(QtCore.QRect(350, 30, 263, 38))
        self.frame_2.setStyleSheet("QFrame{\n"
                "background-color: rgba(85, 85, 127,80);\n"
                "border-radius:15px;\n"
                "}\n"
                "\n"
                "QLabel{\n"
                "background:None;\n"
                "}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setContentsMargins(0, 3, 0, 3)
        self.horizontalLayout_2.setSpacing(20)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_10 = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setMaximumSize(QtCore.QSize(40, 35))
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap(":/icon/steering.png"))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_2.addWidget(self.label_10)
        self.label_13 = QtWidgets.QLabel(self.frame_2)
        self.label_13.setMaximumSize(QtCore.QSize(40, 35))
        self.label_13.setText("")
        self.label_13.setPixmap(QtGui.QPixmap(":/icon/702814.png"))
        self.label_13.setScaledContents(True)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_2.addWidget(self.label_13)
        self.label_11 = QtWidgets.QLabel(self.frame_2)
        self.label_11.setMaximumSize(QtCore.QSize(40, 35))
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap(":/icon/748151.png"))
        self.label_11.setScaledContents(True)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_2.addWidget(self.label_11)
        self.label_12 = QtWidgets.QLabel(self.frame_2)
        self.label_12.setMaximumSize(QtCore.QSize(40, 35))
        self.label_12.setText("")
        self.label_12.setPixmap(QtGui.QPixmap(":/icon/1442194.png"))
        self.label_12.setScaledContents(True)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_2.addWidget(self.label_12)
        self.frame_3 = QtWidgets.QFrame(self.frame_dashboard)
        self.frame_3.setGeometry(QtCore.QRect(370, 360, 221, 41))
        self.frame_3.setStyleSheet("background-color: rgba(85, 85, 127,80);\n"
                "border-radius:15px;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.date = QtWidgets.QLabel(self.frame_3)
        self.date.setGeometry(QtCore.QRect(30, 0, 171, 41))
        self.date.setStyleSheet("color:#fff;\n"
                "font: 12pt \"Roboto\";\n"
                "background:None;")
        self.date.setAlignment(QtCore.Qt.AlignCenter)
        self.date.setObjectName("date")
        self.car_state = QtWidgets.QFrame(self.frame_dashboard)
        self.car_state.setGeometry(QtCore.QRect(350, 80, 271, 251))
        self.car_state.setStyleSheet("background:None;\n"
                "color:#ee1111;")
        self.car_state.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.car_state.setFrameShadow(QtWidgets.QFrame.Raised)
        self.car_state.setObjectName("car_state")
        
        self.label_3 = QtWidgets.QLabel(self.car_state)
        self.label_3.setGeometry(QtCore.QRect(50, 10, 181, 231))
        self.label_3.setStyleSheet("background:None")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/icon/car.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_backLeftDoor = QtWidgets.QLabel(self.car_state)
        self.label_backLeftDoor.setGeometry(QtCore.QRect(200, 150, 41, 16))
        self.label_backLeftDoor.setObjectName("label_backLeftDoor")
        self.label_frontRightDoor = QtWidgets.QLabel(self.car_state)
        self.label_frontRightDoor.setGeometry(QtCore.QRect(200, 110, 31, 16))
        self.label_frontRightDoor.setStyleSheet("color:green;")
        self.label_frontRightDoor.setObjectName("label_frontRightDoor")
        self.label_frontLeftDoor = QtWidgets.QLabel(self.car_state)
        self.label_frontLeftDoor.setGeometry(QtCore.QRect(40, 110, 41, 16))
        self.label_frontLeftDoor.setObjectName("label_frontLeftDoor")
        self.label_frontBonnet = QtWidgets.QLabel(self.car_state)
        self.label_frontBonnet.setGeometry(QtCore.QRect(120, 50, 41, 16))
        self.label_frontBonnet.setObjectName("label_frontBonnet")
        self.label_backBonnet = QtWidgets.QLabel(self.car_state)
        self.label_backBonnet.setGeometry(QtCore.QRect(120, 190, 55, 16))
        self.label_backBonnet.setStyleSheet("")
        self.label_backBonnet.setObjectName("label_backBonnet")
        self.label_backRightDoor = QtWidgets.QLabel(self.car_state)
        self.label_backRightDoor.setGeometry(QtCore.QRect(40, 150, 41, 16))
        self.label_backRightDoor.setObjectName("label_backRightDoor")
        self.frame_4 = QtWidgets.QFrame(self.frame_dashboard)
        self.frame_4.setGeometry(QtCore.QRect(730, 340, 141, 42))
        self.frame_4.setStyleSheet("background-color: rgb(0, 85, 127,130);\n"
                "border-radius:15px;")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_Fuel = QtWidgets.QLabel(self.frame_4)
        self.label_Fuel.setStyleSheet("color:#fff;\n"
                "font: 12pt \"MS UI Gothic\";\n"
                "background:None;")
        self.label_Fuel.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Fuel.setObjectName("label_Fuel")
        self.horizontalLayout_3.addWidget(self.label_Fuel)
        self.Fuel_Progress_bar = QtWidgets.QProgressBar(self.frame_4) # Fuel Progress bar
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Fuel_Progress_bar.sizePolicy().hasHeightForWidth())
        self.Fuel_Progress_bar.setSizePolicy(sizePolicy)
        self.Fuel_Progress_bar.setMinimumSize(QtCore.QSize(75, 0))
        self.Fuel_Progress_bar.setStyleSheet("QProgressBar{\n"
                "    background-color : rgb(0, 0, 0);\n"
                "    \n"
                "    color: rgb(0, 0, 0);\n"
                "    border-style: none;\n"
                "    border-radius: 5px;\n"
                "    text-align: center;\n"
                "}\n"
                "\n"
                "QProgressBar::chunk{\n"
                "    border-radius: 5px;\n"
                "    \n"
                "    background-color: rgb(0, 255, 127,200);\n"
                "}")
        self.Fuel_Progress_bar.setProperty("value",0)
        self.Fuel_Progress_bar.setTextVisible(False)
        self.Fuel_Progress_bar.setOrientation(QtCore.Qt.Horizontal)
        self.Fuel_Progress_bar.setInvertedAppearance(False)
        self.Fuel_Progress_bar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.Fuel_Progress_bar.setFormat("")
        self.Fuel_Progress_bar.setObjectName("Fuel_Progress_bar")
        self.horizontalLayout_3.addWidget(self.Fuel_Progress_bar)
        self.frame_5 = QtWidgets.QFrame(self.frame_dashboard)
        self.frame_5.setGeometry(QtCore.QRect(100, 340, 141, 42))
        self.frame_5.setStyleSheet("background-color: rgb(152, 57, 38,100);\n"
                "border-radius:15px;")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_Doorlocked = QtWidgets.QLabel(self.frame_5)
        self.label_Doorlocked.setStyleSheet("color:#fff;\n"
                "font: 10pt \"MS UI Gothic\";\n"
                "background:None;")
        self.label_Doorlocked.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Doorlocked.setObjectName("label_Doorlocked")
        self.horizontalLayout_4.addWidget(self.label_Doorlocked)
        self.label_Bottom_title = QtWidgets.QLabel(self.centralwidget)
        self.label_Bottom_title.setGeometry(QtCore.QRect(460, 579, 181, 31))
        self.label_Bottom_title.setStyleSheet("background:None;\n"
                "color:#fff;")
        self.label_Bottom_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Bottom_title.setObjectName("label_Bottom_title")
        
        #  Ac frame 
        self.frame_AC = QtWidgets.QFrame(self.centralwidget)
        self.frame_AC.setGeometry(QtCore.QRect(70, 120, 971, 411))
        self.frame_AC.setStyleSheet("QFrame{\n"
                "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(34, 46, 61), stop:1 rgba(34, 34, 47));\n"
                "\n"
                "border-radius:200px;\n"
                "\n"
                "}")
        self.frame_AC.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_AC.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_AC.setObjectName("frame_AC")
        
        # Circular Progress bar for AC
        self.circularProgressCPU = QtWidgets.QFrame(self.frame_AC)
        self.circularProgressCPU.setGeometry(QtCore.QRect(720, 80, 220, 220))
        self.circularProgressCPU.setStyleSheet("QFrame{\n"
                "    border-radius: 110px;    \n"
                "    background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.68 rgba(85, 170, 255, 255), stop:0.612 rgba(255, 255, 255, 0));\n"
                "}")
        self.circularProgressCPU.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.circularProgressCPU.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circularProgressCPU.setObjectName("circularProgressCPU")
        self.circularOutdoor = QtWidgets.QFrame(self.circularProgressCPU)
        self.circularOutdoor.setGeometry(QtCore.QRect(15, 15, 190, 190))
        self.circularOutdoor.setBaseSize(QtCore.QSize(0, 0))
        self.circularOutdoor.setStyleSheet("QFrame{\n"
                "    border-radius: 95px;    \n"
                "    background-color: rgb(58, 58, 102);\n"
                "}")
        self.circularOutdoor.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.circularOutdoor.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circularOutdoor.setObjectName("circularOutdoor")
        self.label_weather_percentage = QtWidgets.QLabel(self.circularOutdoor)
        self.label_weather_percentage.setGeometry(QtCore.QRect(40, 50, 132, 100))
        font = QtGui.QFont()
        font.setFamily("Roboto Thin")
        font.setPointSize(30)
        self.label_weather_percentage.setFont(font)
        self.label_weather_percentage.setStyleSheet("color: rgb(115, 185, 255); padding: 0px; background-color: none;")
        self.label_weather_percentage.setAlignment(QtCore.Qt.AlignCenter)
        self.label_weather_percentage.setIndent(-1)
        self.label_weather_percentage.setObjectName("label_weather_percentage")
        self.label_outdoor_temp = QtWidgets.QLabel(self.circularOutdoor)
        self.label_outdoor_temp.setGeometry(QtCore.QRect(40, 30, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(10)
        self.label_outdoor_temp.setFont(font)
        self.label_outdoor_temp.setStyleSheet("QLabel\n"
                "{\n"
                "background:None;\n"
                "color:rgb(255,255,255,100);\n"
                "}")
        self.label_outdoor_temp.setAlignment(QtCore.Qt.AlignCenter)
        self.label_outdoor_temp.setObjectName("label_outdoor_temp")
        
        
        self.weather = QtWidgets.QFrame(self.frame_AC)
        self.weather.setGeometry(QtCore.QRect(330, 10, 341, 351))
        self.weather.setStyleSheet("QFrame{\n"
                "border-radius:5px;\n"
                "background-color: rgb(14, 22, 39);\n"
                "}")
        self.weather.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.weather.setFrameShadow(QtWidgets.QFrame.Raised)
        self.weather.setObjectName("weather")
        self.label_weather_forecast = QtWidgets.QLabel(self.weather)
        self.label_weather_forecast.setGeometry(QtCore.QRect(50, 10, 261, 20))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        self.label_weather_forecast.setFont(font)
        self.label_weather_forecast.setStyleSheet("QLabel\n"
                "{\n"
                "background:None;\n"
                "color:rgb(227,162,26);\n"
                "}")
        self.label_weather_forecast.setAlignment(QtCore.Qt.AlignCenter)
        self.label_weather_forecast.setObjectName("label_weather_forecast")
        self.label_2 = QtWidgets.QLabel(self.weather)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 101, 81))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/icons/p.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_weather_cond = QtWidgets.QLabel(self.weather)
        self.label_weather_cond.setGeometry(QtCore.QRect(210, 60, 121, 81))
        self.label_weather_cond.setStyleSheet("color:#fff")
        self.label_weather_cond.setObjectName("label_weather_cond")
        self.frame_6 = QtWidgets.QFrame(self.weather)
        self.frame_6.setGeometry(QtCore.QRect(30, 250, 281, 81))
        self.frame_6.setStyleSheet("color:#fff;")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_6)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(30)
        self.gridLayout.setVerticalSpacing(11)
        self.gridLayout.setObjectName("gridLayout")
        self.label_24 = QtWidgets.QLabel(self.frame_6)
        self.label_24.setText("")
        self.label_24.setPixmap(QtGui.QPixmap(":/bg/289759.png"))
        self.label_24.setScaledContents(True)
        self.label_24.setObjectName("label_24")
        self.gridLayout.addWidget(self.label_24, 0, 2, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.frame_6)
        self.label_23.setText("")
        self.label_23.setPixmap(QtGui.QPixmap(":/icons/95252.png"))
        self.label_23.setScaledContents(True)
        self.label_23.setObjectName("label_23")
        self.gridLayout.addWidget(self.label_23, 0, 1, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy)
        self.label_22.setStyleSheet("")
        self.label_22.setText("")
        self.label_22.setPixmap(QtGui.QPixmap(":/icons/567255.png"))
        self.label_22.setScaledContents(True)
        self.label_22.setObjectName("label_22")
        self.gridLayout.addWidget(self.label_22, 0, 0, 1, 1)
        self.label_Ac_Mode1 = QtWidgets.QLabel(self.frame_6)
        self.label_Ac_Mode1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Ac_Mode1.setObjectName("label_Ac_Mode1")
        self.gridLayout.addWidget(self.label_Ac_Mode1, 1, 0, 1, 1)
        self.label_Ac_Mode2 = QtWidgets.QLabel(self.frame_6)
        self.label_Ac_Mode2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Ac_Mode2.setObjectName("label_Ac_Mode2")
        self.gridLayout.addWidget(self.label_Ac_Mode2, 1, 1, 1, 1)
        self.label_Ac_Mode3 = QtWidgets.QLabel(self.frame_6)
        self.label_Ac_Mode3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Ac_Mode3.setObjectName("label_Ac_Mode3")
        self.gridLayout.addWidget(self.label_Ac_Mode3, 1, 2, 1, 1)
        self.label_weather_percentage_4 = QtWidgets.QLabel(self.weather)
        self.label_weather_percentage_4.setGeometry(QtCore.QRect(110, 80, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto Thin")
        font.setPointSize(13)
        self.label_weather_percentage_4.setFont(font)
        self.label_weather_percentage_4.setStyleSheet("color: rgb(115, 185, 255,70); \n"
                "padding: 0px;\n"
                " background-color: none;")
        self.label_weather_percentage_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_weather_percentage_4.setIndent(-1)
        self.label_weather_percentage_4.setObjectName("label_weather_percentage_4")
        self.line = QtWidgets.QFrame(self.weather)
        self.line.setGeometry(QtCore.QRect(194, 81, 3, 40))
        self.line.setStyleSheet("background-color: rgba(85, 85, 255,120);")
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.circularIndoor = QtWidgets.QFrame(self.frame_AC)
        self.circularIndoor.setGeometry(QtCore.QRect(70, 90, 220, 220))
        self.circularIndoor.setStyleSheet("QFrame{\n"
                "    border-radius: 110px;    \n"
                "    background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.88 rgba(255,196,13,255), stop:0.712 rgba(255, 255, 255, 0));\n"
                "}")
        self.circularIndoor.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.circularIndoor.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circularIndoor.setObjectName("circularIndoor")
        self.circularOutdoor_2 = QtWidgets.QFrame(self.circularIndoor)
        self.circularOutdoor_2.setGeometry(QtCore.QRect(15, 15, 190, 190))
        self.circularOutdoor_2.setBaseSize(QtCore.QSize(0, 0))
        self.circularOutdoor_2.setStyleSheet("QFrame{\n"
                "    border-radius: 95px;    \n"
                "    background-color: rgb(43,87,151);\n"
                "}")
        self.circularOutdoor_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.circularOutdoor_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circularOutdoor_2.setObjectName("circularOutdoor_2")
        self.label_weather_percentage_3 = QtWidgets.QLabel(self.circularOutdoor_2)
        self.label_weather_percentage_3.setGeometry(QtCore.QRect(40, 50, 132, 100))
        font = QtGui.QFont()
        font.setFamily("Roboto Thin")
        font.setPointSize(30)
        self.label_weather_percentage_3.setFont(font)
        self.label_weather_percentage_3.setStyleSheet("color: rgb(115, 185, 255); padding: 0px; background-color: none;")
        self.label_weather_percentage_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_weather_percentage_3.setIndent(-1)
        self.label_weather_percentage_3.setObjectName("label_weather_percentage_3")
        self.label_Indoor_temp = QtWidgets.QLabel(self.circularOutdoor_2)
        self.label_Indoor_temp.setGeometry(QtCore.QRect(40, 30, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(10)
        self.label_Indoor_temp.setFont(font)
        self.label_Indoor_temp.setStyleSheet("QLabel\n"
                "{\n"
                "background:None;\n"
                "color:rgb(255,255,255,100);\n"
                "}")
        self.label_Indoor_temp.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Indoor_temp.setObjectName("label_Indoor_temp")
        self.checked =AnimatedToggle(self.frame_AC)
        self.checked.setGeometry(QtCore.QRect(140, 310, 100, 50))
        
        self.frame_music = QtWidgets.QFrame(self.centralwidget)
        self.frame_music.setGeometry(QtCore.QRect(70, 120, 971, 411))
        self.frame_music.setStyleSheet("QFrame{\n"
                "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(34, 46, 61), stop:1 rgba(34, 34, 47));\n"
                "\n"
                "border-radius:200px;\n"
                "\n"
                "}")
        self.frame_music.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_music.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_music.setObjectName("frame_music")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        
        # map frame 
        self.frame_map = QtWidgets.QFrame(self.centralwidget)
        self.frame_map.setGeometry(QtCore.QRect(70, 120, 971, 411))
        self.frame_map.setStyleSheet("QFrame{\n"
                "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(34, 46, 61), stop:1 rgba(34, 34, 47));\n"
                "\n"
                "border-radius:200px;\n"
                "\n"
                "}\n"
                "QPushButton{\n"
                "    \n"
                "    background-color: rgba(0,171,169,80);\n"
                "    border:None;\n"
                "    color:#fff;\n"
                "    font: 10pt;\n"
                "\n"
                "}\n"
                "QPushButton:Hover{\n"
                "\n"
                "    \n"
                "    background-color: rgba(0,171,169,120);\n"
                "\n"
                "\n"
                "}\n"
                "\n"
                "QPushButton:Pressed{\n"
                "    \n"
                "    \n"
                "background-color: rgba(0,171,169,100);\n"
                "\n"
                "}")
        self.frame_map.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_map.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_map.setObjectName("frame_map")
        
        self.arduino_update()
        map_ = folium.Map(location=self.loc_curr, zoom_start=13)
        folium.Marker(self.loc_curr, popup="Car Location").add_to(map_)
        # m = folium.Map(
        #     tiles='Stamen Terrain',
        #     zoom_start=10,
        #     location=coordinate,
        #     attr='Map tiles by Stamen Design, CC BY 3.0 — Map data © OpenStreetMap contributors'
        # )

        # save map data to data object
        data = io.BytesIO()
        map_.save(data, close_file=False)

        #webView = QWebEngineView(self.frame_map)
        #webView.setHtml(data.getvalue().decode())

        self.map_plot = QWebEngineView(self.frame_map)
        self.map_plot.setHtml(data.getvalue().decode())
        self.map_plot.setObjectName(u"map_plot")
        self.map_plot.setGeometry(QRect(100, 40, 391, 331))
        self.btn_map_start = QPushButton(self.frame_map)
        self.btn_map_start.setObjectName(u"btn_map_start")
        self.btn_map_start.setGeometry(QRect(830, 240, 119, 37))
        sizePolicy.setHeightForWidth(self.btn_map_start.sizePolicy().hasHeightForWidth())
        self.btn_map_start.setSizePolicy(sizePolicy)
        self.btn_map_stop = QPushButton(self.frame_map)
        self.btn_map_stop.setObjectName(u"btn_map_stop")
        self.btn_map_stop.setGeometry(QRect(830, 190, 119, 37))
        sizePolicy.setHeightForWidth(self.btn_map_stop.sizePolicy().hasHeightForWidth())
        self.btn_map_stop.setSizePolicy(sizePolicy)
        global timer
        self.timer = QTimer()
        # set timer timeout callback function
        self.timer.timeout.connect(self.viewCam)

        self.webcam = QLabel(self.frame_map)
        self.webcam.setObjectName(u"webcam")
        self.webcam.setGeometry(QRect(500, 40, 321, 331))

    
        MainWindow.setCentralWidget(self.centralwidget)
        self.show_Dash()
        self.progress()
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.label_km = QLabel(self.speed)
        self.label_km.setText("Km/h")
        self.label_km.setGeometry(QRect(130, 190, 57, 16))
        self.label_km.setStyleSheet(u"\n"
                "color:#fff;\n"
                "    font: 15pt;\n"
                "background:None;\n"
                "\n"
                )
        self.label_km.setAlignment(Qt.AlignCenter)



    def viewCam(self):
        ret, image = cap.read()
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        height, width, channel = image.shape
        step = channel * width
        qImg = QImage(image.data, width, height, step, QImage.Format_RGB888)
        self.webcam.setPixmap(QPixmap.fromImage(qImg))

    def quit_cam(self):
        self.timer.stop()
        cap.release()
        
    def controlTimer(self):
        global cap
        if not self.timer.isActive():
            cap = cv2.VideoCapture(0)
            self.timer.start(20)
        else:
            self.timer.stop()
            cap.release()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        
        MainWindow.setWindowTitle(_translate("Rolls Royce Dashboard", "Rolls Royce Dashboard"))
        
        self.btn_dash.setText(_translate("MainWindow", "DASHBOARD"))
        self.btn_ac.setText(_translate("MainWindow", "AC"))
        self.btn_music.setText(_translate("MainWindow", "MUSIC"))
        self.btn_map.setText(_translate("MainWindow", "MAP"))
        self.date.setText(datetime.now().strftime("%I: %M: %S  %p"))
        self.arduino_update()

        self.label_backLeftDoor.setText(_translate("MainWindow", f"{self.backLeftDoor}"))
        self.label_frontRightDoor.setText(_translate("MainWindow", f"{self.frontRightDoor}"))
        self.label_frontLeftDoor.setText(_translate("MainWindow", f"{self.frontLeftDoor}"))
        self.label_frontBonnet.setText(_translate("MainWindow", f"{self.frontBonnet}"))
        self.label_backBonnet.setText(_translate("MainWindow", f"{self.backBonnet}"))
        self.label_backRightDoor.setText(_translate("MainWindow", f"{self.backRightDoor}"))
        self.label_Fuel.setText(_translate("MainWindow",f"Fuel:"))
        self.label_Doorlocked.setText(_translate("MainWindow",f"All Door locked"))
        self.label_Bottom_title.setText(_translate("MainWindow",f"Rolls Royce Phantom"))
        self.label_weather_percentage.setText(_translate("MainWindow", f"<html><head/><body><p>{weather.temp_celsius:.0f}°C</p></body></html>"))
        self.label_outdoor_temp.setText(_translate("MainWindow", "Outdoor\n"
                "Temperature"))
        self.label_weather_forecast.setText(_translate("MainWindow", "Weather Forecast"))
        self.label_weather_cond.setText(_translate("MainWindow", 
                f"<html><head/><body><p>{weather.weather_condition}</p> <p>{weather.city}, {weather.country}</p></body></html>"))
        self.label_Ac_Mode1.setText(_translate("MainWindow", "Mode1"))
        self.label_Ac_Mode2.setText(_translate("MainWindow", "Mode2"))
        self.label_Ac_Mode3.setText(_translate("MainWindow", "Mode3"))
        self.label_weather_percentage_4.setText(_translate("MainWindow", f"<html><head/><body><p>{weather.weather_condition}</p></body></html>"))
        self.label_weather_percentage_3.setText(_translate("MainWindow", f"<html><head/><body><p>{self.temperature}°C</p></body></html>"))
        self.label_Indoor_temp.setText(_translate("MainWindow", "Indoor\n"
                "Temperature"))
        self.checked.setText(_translate("MainWindow", "PushButton"))
        
        self.btn_map_start.setText(_translate("MainWindow", "Start"))
        self.btn_map_stop.setText(_translate("MainWindow", "Stop"))
        
        #btn function
        self.btn_dash.clicked.connect(self.show_Dash)
        self.btn_ac.clicked.connect(self.show_AC)
        self.btn_music.clicked.connect(self.show_Music)
        self.btn_map.clicked.connect(self.show_Map)



    def show_Dash(self):
        self.quit_cam
        self.progress()

        self.frame_dashboard.setVisible(True)
        self.frame_AC.setVisible(False)
        self.frame_map.setVisible(False)
        self.frame_music.setVisible(False)
        self.timer.stop




    def show_AC(self):
        self.progress()

        self.quit_cam
        self.frame_dashboard.setVisible(False)
        self.frame_AC.setVisible(True)
        self.frame_map.setVisible(False)
        self.frame_music.setVisible(False)

    def show_Music(self):
        self.progress()
        self.quit_cam
        self.frame_dashboard.setVisible(False)
        self.frame_AC.setVisible(False)
        self.frame_map.setVisible(False)
        self.frame_music.setVisible(True)
        self.browser = QWebEngineView(self.frame_music)
        self.browser.setUrl(QUrl("https://music.youtube.com/"))  # Spotify Web Player URL
        
        # Add the browser to the layout (inside the frame) # Dont know what happened here but working fine.
        self.music_layout = QVBoxLayout()
        self.music_layout.addWidget(self.browser)
        self.frame_music.setLayout(self.music_layout)
        MainWindow.setCentralWidget(self.centralwidget) 

    def show_Map(self):
        self.progress()
        self.frame_dashboard.setVisible(False)
        self.frame_AC.setVisible(False)
        self.frame_map.setVisible(True)
        self.frame_music.setVisible(False)
        self.controlTimer()

    def progress(self):
        self.speed.set_MaxValue(100)
        self.speed.set_DisplayValueColor(200,200,200)
        self.speed.set_CenterPointColor(0,0,0)
        self.speed.set_NeedleColor(255,0,0)
        self.speed.set_NeedleColorDrag(255,255,255)
        self.speed.set_ScaleValueColor(255,200,255)
        self.speed.set_enable_big_scaled_grid(True)
        self.speed.set_enable_barGraph(False)
        self.speed.set_enable_filled_Polygon(False)
        self.speed.update_value(0) # set the value of speed to 5


        self.rpm.set_scala_main_count(6)
        self.rpm.set_MaxValue(6)
        self.rpm.set_MinValue(0)
        self.rpm.update_value(0) # set the value of RPM to 5
        self.rpm.set_DisplayValueColor(200,200,200)
        self.rpm.set_enable_big_scaled_grid(True)
        self.rpm.set_ScaleValueColor(255,255,255)
        self.rpm.set_NeedleColor(255,0,0)
        self.rpm.set_NeedleColorDrag(255,255,255)
        self.rpm.set_CenterPointColor(0,0,0)
        
        # Create a timer to update the speed and RPM values dynamically
        self.timer.timeout.connect(self.update_gauges)

        
#     def progress(self):
#         self.speed.set_MaxValue(100)
#         self.speed.set_DisplayValueColor(200, 200, 200)
#         self.speed.set_CenterPointColor(255, 255, 255)
#         self.speed.set_NeedleColor(255, 255, 200)
#         self.speed.set_NeedleColorDrag(255, 255, 255)
#         self.speed.set_ScaleValueColor(255, 200, 255)
#         self.speed.set_enable_big_scaled_grid(True)
#         self.speed.set_enable_barGraph(False)
#         self.speed.set_enable_filled_Polygon(False)

#         self.rpm.set_scala_main_count(6)
#         self.rpm.set_MaxValue(6)
#         self.rpm.set_MinValue(0)
#         self.rpm.set_DisplayValueColor(200, 200, 200)
#         self.rpm.set_enable_big_scaled_grid(True)
#         self.rpm.set_ScaleValueColor(255, 255, 255)
#         self.rpm.set_NeedleColorDrag(255, 255, 255)
#         self.rpm.set_CenterPointColor(255, 255, 255)

#         # Create a timer to update the speed and RPM values dynamically
#         self.timer = QTimer()
#         self.timer.timeout.connect(self.update_gauges)
#         self.timer.start(1000)  # Update every second

    def update_gauges(self):
        _translate = QtCore.QCoreApplication.translate
       
        
        self.date.setText(datetime.now().strftime("%I: %M: %S  %p"))
        self.arduino_update()
 
        map_ = folium.Map(location=self.loc_curr, zoom_start=13)
        folium.Marker(self.loc_curr, popup="Car Location").add_to(map_)      
        print(f"Updated Location - Latitude: {self.loc_curr[0]}, Longitude: {self.loc_curr[1]}")
        self.label_backLeftDoor.setText(f"{self.backLeftDoor}")
        self.label_frontRightDoor.setText(f"{self.frontRightDoor}")
        self.label_frontLeftDoor.setText(f"{self.frontLeftDoor}")
        self.label_frontBonnet.setText(f"{self.frontBonnet}")
        self.label_backBonnet.setText(f"{self.backBonnet}")
        self.label_backRightDoor.setText(f"{self.backRightDoor}")
        self.label_Fuel.setText(f"Fuel:")
        self.label_Doorlocked.setText(f"Door locked")
        self.label_Bottom_title.setText(f"Rolls Royce Phantom")
        self.label_weather_percentage.setText(f"<html><head/><body><p>{weather.temp_celsius:.0f}°C</p></body></html>")
        self.label_outdoor_temp.setText(f"Outdoor\nTemperature")
        self.label_weather_percentage_3.setText(_translate("MainWindow", f"<html><head/><body><p>{self.temperature}°C</p></body></html>"))
        
        self.label_backLeftDoor.adjustSize()
        self.label_frontRightDoor.adjustSize()
        self.label_frontLeftDoor.adjustSize()
        self.label_frontBonnet.adjustSize()
        self.label_backBonnet.adjustSize()
        self.label_backRightDoor.adjustSize()
        self.label_Fuel.adjustSize()
        self.label_Doorlocked.adjustSize()
        self.label_Bottom_title.adjustSize()
        # self.label_weather_percentage.adjustSize()
        # self.label_outdoor_temp.adjustSize()
        # self.label_weather_percentage_3.adjustSize()
        
        # self.label_backLeftDoor.setText(f"{frontLeftDoor}")
        # self.label_frontRightDoor.setText(f"{frontRightDoor}")       
        # self.label_frontLeftDoor.setText(f"{backLeftDoor}")
        # self.label_frontBonnet.setText(f"{backRightDoor}")
        # self.label_backBonnet.setText(f"{frontBonnet}")
        # self.label_backRightDoor.setText(f"{backBonnet}")
        # self.label_Fuel.setText(f"Fuel:")
        # self.label_Doorlocked.setText(f"Door locked")
        # self.label_Bottom_title.setText(f"Rolls Royce Phantom")
        # self.label_weather_percentage.setText(f"<html><head/><body><p>{weather.temp_celsius:.0f}°C</p></body></html>")
        # self.label_outdoor_temp.setText(f"Outdoor\nTemperature")
                # self.label_weather_percentage_3.setText(_translate("MainWindow", f"<html><head/><body><p>{temperature}°C</p></body></html>"))

    
        
    def arduino_update(self):
        # Get live data from Arduino
        #     car_status = get_live_data()

        # Print the live data
        #     print_data(car_status)

        #     # Save the data to a file
        #     save_data_to_file(car_status)

        # Optionally, read data from file (if needed)
        data_from_file = read_data_from_file()
                
        self.frontLeftDoor = data_from_file[1][0]
        self.frontRightDoor = data_from_file[1][1]
        self.backLeftDoor =   data_from_file[1][2]
        self.backRightDoor =   data_from_file[1][3]
        self.frontBonnet =   data_from_file[1][4]
        self.backBonnet =   data_from_file[1][5]
        self.temperature =   data_from_file[1][6]
        self.gasDetected =   data_from_file[1][7]
        self.motionDetected=     data_from_file[1][8]
        # self.loc_curr = [data_from_file[1][9], data_from_file[1][10]]
        self.loc_curr = [getlocation.current_location[0], getlocation.current_location[1]]
        self.loc_curr = [data_from_file[1][9], data_from_file[1][10]] if self.loc_curr == [0,0] else self.loc_curr

        self.speed_value = int(data_from_file[1][11])
        self.rpm_value = int(data_from_file[1][12])
        
        
        self.speed.update_value(self.speed_value)
        self.rpm.update_value(self.rpm_value)
        self.fuel_level = int(data_from_file[1][13])
        self.Fuel_Progress_bar.setValue(self.fuel_level)
        #     print_file_data(data_from_file)
        
        
import resources

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

