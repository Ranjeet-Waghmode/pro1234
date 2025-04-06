import os
import sys
import cv2
import threading
from datetime import datetime


import io
import folium # pip install folium

from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView # pip install PyQtWebEngine
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from qtwidgets import *
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer


from .gui.gauge import AnalogGaugeWidget
from .read_data_from_file import read_data_from_file, print_file_data
from .theft_detection_ml import theft_detection_main
from . import weather, getlocation
from .shape_predictor import sleep_detection
from .shape_predictor.sleep_detection import counter
from .shape_predictor.sounds.play_sounds import welcome_sound
from .loading_screen.loading import LoadingSplash