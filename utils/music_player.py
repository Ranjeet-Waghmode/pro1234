# import sys
# from PyQt5.QtCore import QUrl
# from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
# from PyQt5.QtWebEngineWidgets import QWebEngineView

# class SpotifyApp(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Spotify Player")
#         self.setGeometry(100, 100, 1200, 800)

#         # Set up the WebEngineView to display the Spotify web player
#         self.browser = QWebEngineView(self)
#         self.youtube = self.browser.setUrl(QUrl("https://music.youtube.com/watch?v=w_VQJBWvJcI&list=OLAK5uy_nzzlEcO_t5ZFyS-sjbLO6Q1W0X9FEa0gs"))  # yputube Web Player URL
#         # self.spotify = self.browser.setUrl(QUrl("https://open.spotify.com"))
#         # Load the Spotify web player
#         # self.browser.setUrl(QUrl("https://open.spotify.com"))

#         # Layout
#         layout = QVBoxLayout()
#         layout.addWidget(self.browser)
#         widget = QWidget()
#         widget.setLayout(layout)
#         self.setCentralWidget(widget)

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = SpotifyApp()
#     window.show()
#     sys.exit(app.exec_())


# import sys
# from PyQt5 import QtCore
# from PyQt5.QtCore import QUrl
# from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QAction, QMenuBar
# from PyQt5.QtWebEngineWidgets import QWebEngineView

# class SpotifyApp(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Main Car Dashboard App")
#         self.setGeometry(100, 100, 1200, 800)

#         # Set up a simple menu bar with an option to open the music player
#         self.menu_bar = self.menuBar()
#         file_menu = self.menu_bar.addMenu("File")
        
#         # Add action to open music player
#         open_music_action = QAction("Open Music Player", self)
#         open_music_action.triggered.connect(self.open_music_player)
#         file_menu.addAction(open_music_action)

#         self.show()

#     def open_music_player(self):
#         # Create a new music player window
#         self.music_window = MusicPlayerWindow()
#         self.music_window.show()

# class MusicPlayerWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Music Player")
#         self.setGeometry(200, 200, 800, 600)

#         # Set up the WebEngineView to display the YouTube music player
#         self.browser = QWebEngineView(self)
#         self.browser.setUrl(QUrl("https://music.youtube.com/watch?v=w_VQJBWvJcI&list=OLAK5uy_nzzlEcO_t5ZFyS-sjbLO6Q1W0X9FEa0gs"))  # YouTube music playlist

#         # Layout for the music player window
#         layout = QVBoxLayout()
#         layout.addWidget(self.browser)
#         widget = QWidget()
#         widget.setLayout(layout)
#         self.setCentralWidget(widget)

#         # Handle the close event to prevent closing the entire app
#         self.setWindowFlags(self.windowFlags() | QtCore.Qt.WindowMinimized)
#         self.setAttribute(QtCore.Qt.WA_DeleteOnClose)

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = SpotifyApp()  # Main app window
#     sys.exit(app.exec_())


# import sys
# from PyQt5.QtCore import QUrl
# from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QMenuBar, QAction
# from PyQt5.QtWebEngineWidgets import QWebEngineView

# class music(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Car Dashboard with Music Player")
#         self.setGeometry(100, 100, 1200, 800)

#         # Set up the main layout
#         layout = QVBoxLayout()

#         # Add the music player section (Web Engine View)
#         self.music_player = QWebEngineView(self)
#         self.music_player.setUrl(QUrl("https://music.youtube.com/watch?v=w_VQJBWvJcI&list=OLAK5uy_nzzlEcO_t5ZFyS-sjbLO6Q1W0X9FEa0gs"))  # YouTube Music Playlist
#         layout.addWidget(self.music_player)

#         # Add other widgets for the rest of the dashboard (e.g., controls, car data, etc.)
#         # Add more widgets to layout as needed for your app
#         self.other_widget = QWidget()
#         layout.addWidget(self.other_widget)

#         # Set up a simple menu bar with options
#         self.menu_bar = self.menuBar()
#         file_menu = self.menu_bar.addMenu("File")
        
#         # Add an option to stop or close music player
#         close_music_action = QAction("Close Music Player", self)
#         close_music_action.triggered.connect(self.close_music_player)
#         file_menu.addAction(close_music_action)

#         # Set up central widget
#         widget = QWidget()
#         widget.setLayout(layout)
#         self.setCentralWidget(widget)

#     def close_music_player(self):
#         """Option to stop/close the music player (optional)"""
#         self.music_player.deleteLater()
#         print("Music player closed.")

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = music()
#     window.show()
#     sys.exit(app.exec_())
import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QFrame, QWidget, QAction
from PyQt5.QtWebEngineWidgets import QWebEngineView

class SpotifyApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set up the main window
        self.setWindowTitle("Car Dashboard with Music Player")
        self.setGeometry(100, 100, 1200, 800)

        # Create the layout and main widget
        layout = QVBoxLayout()

        # Create a frame for the music player
        self.frame_music = QFrame(self)
        self.frame_music.setGeometry(100, 100, 1000, 600)  # Set position and size for music frame
        self.frame_music.setStyleSheet("background-color: lightgray;")  # Optional: Style the frame

        # Create the music player (browser) widget inside the frame
        self.browser = QWebEngineView(self.frame_music)
        self.browser.setUrl(QUrl("https://music.youtube.com/watch?v=w_VQJBWvJcI&list=OLAK5uy_nzzlEcO_t5ZFyS-sjbLO6Q1W0X9FEa0gs"))  # YouTube Music Player

        # Add the browser to the layout (inside the frame)
        self.music_layout = QVBoxLayout()
        self.music_layout.addWidget(self.browser)
        self.frame_music.setLayout(self.music_layout)

        # Set the central widget (it will contain other parts of the dashboard)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        # Optionally: Add a menu to quit the music player or stop it
        self.add_menu()

    def add_menu(self):
        # Create the menu bar
        self.menu_bar = self.menuBar()

        # Add 'File' menu with an option to quit the music player
        file_menu = self.menu_bar.addMenu("File")
        close_music_action = QAction("Close Music Player", self)
        close_music_action.triggered.connect(self.quit_cam)  # Call the quit_cam method when triggered
        file_menu.addAction(close_music_action)

    def quit_cam(self):
        """Optionally: Method to stop/close the music player (browser)"""
        print("Closing Music Player")
        self.browser.deleteLater()  # Removes the music player (browser) widget from the window

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SpotifyApp()
    window.show()
    sys.exit(app.exec_())
