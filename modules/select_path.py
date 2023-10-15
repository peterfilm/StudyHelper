from PyQt5.QtWidgets import QFileDialog, QMessageBox
from modules.api import conf, load_key_to_api
import os


class SelectPath:
    '''
    Кнопка выбра пути к KMplayer
    '''

    def __init__(self, main_window):
        self.mw = main_window
        self.mw.label_kmplayer_path.clicked.connect(self.choosePath)

    def choosePath(self):
        kmplayer_path = QFileDialog.getOpenFileName(
            self.mw, 'Выбрать путь к KMPlayer64', conf['KMPLAYER_EXE'], 'EXE *.exe')
        if kmplayer_path and (conf['KMPLAYER_EXE'] == os.path.basename(kmplayer_path[0]) or os.path.basename(kmplayer_path[0]) == 'kmplayer.exe'):
            conf['KMPLAYER_PATH'] = os.path.normpath(kmplayer_path[0])
            load_key_to_api('KMPLAYER_PATH',
                            os.path.normpath(kmplayer_path[0]))
        else:
            QMessageBox.warning(self.mw, 'Ошибка',
                                'Некорректный путь к KMPlayer')
            conf['KMPLAYER_PATH'] = ''
            load_key_to_api('KMPLAYER_PATH', '')
