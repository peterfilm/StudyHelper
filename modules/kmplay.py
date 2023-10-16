from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize
import subprocess
import os
from modules.api import conf


class KMPlay:
    '''
    Кнопка открытия плеера + воспроизведение файлов из выбранной папки
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
