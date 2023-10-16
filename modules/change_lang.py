from modules.api import conf
import keyboard


class ChangeLang:
    '''
    Автоматическое переключение языка
    '''

    def __init__(self, main_window):
        self.mw = main_window
        self.mw.comboBox_language.addItem('-')
        self.mw.comboBox_language.setItemData(0, {"language": "-"})
        for i in conf['LANGUAGE']:
            self.mw.comboBox_language.addItem(i)
            self.mw.comboBox_language.setItemData(0, {"language": i})

        self.mw.comboBox_language.activated.connect(self.activate)

    def activate(self):
        lang = self.mw.comboBox_language.currentText()
        self.mw.lang = conf['LANGUAGE'][lang] if lang != '-' else None

    def switch_input_language(self, lang):
        want_lang = conf['LANGUAGE'][self.mw.comboBox_language.currentText()]
        if lang != want_lang:
            keyboard.press_and_release(conf['LANG_KEYS'])
