from PyQt5.QtGui import QDesktopServices, QIcon
from PyQt5.QtCore import QUrl, QSize
import subprocess
import keyboard
import time
from filters._openFiles import open_in_kmplayer
import os
from modules.api import conf


class KMPlay:
    '''
    Кнопка открытия папки
    '''

    def __init__(self, main_window):
        self.mw = main_window
        self.mw.pushButton_kmplay.setIcon(QIcon('img/kmplayer.png'))
        self.mw.pushButton_kmplay.setIconSize(QSize(28, 28))

        self.mw.pushButton_kmplay.clicked.connect(self.play)

    def play(self):
        try:
            command = [conf['KMPLAYER_PATH'], os.path.join(
                conf['LAST_PATH'], self.mw.files[0])]
            subprocess.Popen(command)

        except Exception as e:
            print(f"Error: {e}")


# # Specify the path to the KMPlayer executable
# kmplayer_path = "C:\\Program Files (x86)\\KMPlayer\\kmplayer.exe"

# # Specify the path to the video file you want to play
# video_path = "E:\\Самообразование\\Туторы\\! Спина\\[SW.BAND] [Ярош Анастасия] Здоровая спина онлайн-курс\\[SW.BAND] Урок 1.mp4"

# # Open KMPlayer
# subprocess.Popen([kmplayer_path, video_path])

# # Wait for KMPlayer to open (you can adjust the duration as needed)
# time.sleep(5)

# # Send the "Space" key to start playback
# keyboard.press_and_release("space")

# # Keep the script running
# keyboard.wait("esc")
