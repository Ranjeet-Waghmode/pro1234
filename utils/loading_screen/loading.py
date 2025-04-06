from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QSplashScreen, QLabel, QWidget, QVBoxLayout)
from PyQt5.QtGui import QPixmap, QFont, QMovie
from PyQt5.QtCore import Qt, QTimer
import sys
import random

class LoadingSplash(QSplashScreen):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.showFullScreen()
        self.setPixmap(QPixmap(Fr"D:\RANJEET\sap\car_dash\pro1234\utils\loading_screen\car{random.randint(1, 6)}.jpg"))
        self.setStyleSheet("background-color: rgb(30, 31, 40); color: white;")

        # Layout for splash content
        self.container = QWidget(self)
        self.container.setGeometry(0, 0, 400, 300)
        layout = QVBoxLayout()
        self.container.setLayout(layout)

        # Animated GIF loader
        self.gif = QMovie(r"D:\RANJEET\sap\car_dash\pro1234\utils\loading_screen\load_car.gif")  # Replace with your spinner GIF
        self.gif_label = QLabel()
        self.gif_label.setMovie(self.gif)
        self.gif.start()

        # Text below the loader
        self.label = QLabel("🚗 Loading Smart Dashboard...")
        self.label.setFont(QFont("Segoe UI", 12))
        self.label.setAlignment(Qt.AlignCenter)

        layout.addStretch()
        layout.addWidget(self.gif_label, alignment=Qt.AlignCenter)
        layout.addWidget(self.label, alignment=Qt.AlignCenter)
        layout.addStretch()


class MainDashboard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Smart Car Dashboard")
        self.setFixedSize(1117, 636)
        self.setStyleSheet("background-color: rgb(30, 31, 40); color: white;")

        label = QLabel("🏁 Welcome to Smart Dashboard", self)
        label.setFont(QFont("Segoe UI", 18))
        label.setStyleSheet("color: white;")
        label.setAlignment(Qt.AlignCenter)
        label.setGeometry(300, 250, 500, 100)


def main():
    app = QApplication(sys.argv)

    # Show splash
    splash = LoadingSplash()
    splash.show()

    # Show main window after 3 seconds
    window = MainDashboard()
    QTimer.singleShot(3000, splash.close)
    QTimer.singleShot(3000, window.show)

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
