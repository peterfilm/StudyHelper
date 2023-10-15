from modules.api import conf, load_key_to_api
from PyQt5.QtWidgets import QMessageBox
import os


def checker_kmplayer(mw):
    if not conf['KMPLAYER_PATH']:
        kmplayer_set(mw, 0)
    elif not conf['LAST_PATH']:
        kmplayer_set(mw, 0)

    elif conf['LAST_PATH'] and not os.path.exists(conf['LAST_PATH']):
        QMessageBox.warning(
            mw, 'Ошибка', 'Указан некорректный путь к папке с видео')
        kmplayer_set(mw, 0)
        load_key_to_api('LAST_PATH', '')
        conf['LAST_PATH'] = ''

    elif conf['KMPLAYER_PATH'] and not os.path.exists(conf['KMPLAYER_PATH']):
        QMessageBox.warning(
            mw, 'Ошибка', 'Указан некорректный путь к KMPlayer')
        kmplayer_set(mw, 0)
        load_key_to_api('KMPLAYER_PATH', '')
        conf['KMPLAYER_PATH'] = ''
    
    elif conf['KMPLAYER_PATH'] and os.path.exists(conf['KMPLAYER_PATH']) and not mw.files:
        kmplayer_set(mw, 0)
    else:
        kmplayer_set(mw, 1)


def kmplayer_set(mw, value):
    mw.pushButton_kmplay.setEnabled(value)
    if value == 0:
        mw.pushButton_kmplay.setStyleSheet(
            'background-color: #949494')
    if value == 1:
        mw.pushButton_kmplay.setStyleSheet(
            'background-color: #5b449b')
