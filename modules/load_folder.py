from PyQt5.QtGui import QDesktopServices
from PyQt5.QtCore import QUrl
from functools import partial
import os
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget, QFileDialog, QMessageBox
from PyQt5.QtGui import QDesktopServices, QIcon
from filters._CHECKER_kmplayer import checker_kmplayer
from filters._open_folder import check_open_folder
from modules.api import conf, load_key_to_api


class LoadFolder:
    '''
    Кнопка выбора папки
    '''

    def __init__(self, main_window):
        self.mw = main_window
        self.mw.pushButton.clicked.connect(partial(self.open_folder, 'button'))
        self.mw.lineEdit.returnPressed.connect(
            partial(self.open_folder, 'lineedit'))
        if conf['LAST_PATH']:
            if os.path.exists(conf['LAST_PATH']):
                self.mw.files = [i for i in os.listdir(
                    conf['LAST_PATH']) if os.path.isfile(os.path.join(conf['LAST_PATH'], i)) and i.split('.')[-1].lower() in conf['FORMATS']]
        else:
            conf['LAST_PATH'] = ''
            load_key_to_api('LAST_PATH', '')

    def open_folder(self, value):
        if value == 'lineedit':
            directory = self.mw.lineEdit.text()
        if value == 'button':
            directory = QFileDialog.getExistingDirectory(self.mw, 'Выберите путь к видео', conf['LAST_PATH'])
        if os.path.exists(directory):
            self.mw.files = [i for i in os.listdir(
                directory) if os.path.isfile(os.path.join(directory, i)) and i.split('.')[-1].lower() in conf['FORMATS']]

            conf['LAST_PATH'] = directory
            load_key_to_api('LAST_PATH', directory)

            self.mw.lineEdit.setText(directory)
            self.mw.pushButton_open.setEnabled(True)
            checker_kmplayer(self.mw)
            check_open_folder(self.mw)
            QMessageBox.information(self.mw, 'Информация', 'Папка выбрана')
        else:
            conf['LAST_PATH'] = ''
            load_key_to_api('LAST_PATH', '')
            QMessageBox.warning(self.mw, 'Ошибка', 'Выберите корректный путь')
            self.mw.lineEdit.setText('')
            self.mw.pushButton_open.setEnabled(False)
            checker_kmplayer(self.mw)
            check_open_folder(self.mw)
