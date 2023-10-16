from modules.api import conf
import os

def check_open_folder(mw):
    '''
    Проверка можно ли открыть папку с видео, которая указана в программе
    '''
    if conf['LAST_PATH'] and os.path.exists(os.path.normpath(conf['LAST_PATH'])):
        mw.pushButton_open.setEnabled(True)
    else:
        mw.pushButton_open.setEnabled(False)