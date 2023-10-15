def kmplayer_to_google(mw, value):
    if value == 'KMPlayer':
        mw.label_kmplayer.show()
        mw.label_kmplayer_path.show()
        mw.lineEdit.show()
        mw.pushButton_kmplay.show()
        mw.pushButton.show()
        mw.pushButton_open.show()
        mw.label_choose_chrome.hide()
        mw.comboBox_chrome.hide()
    if value == 'Google Chrome':
        mw.label_kmplayer.hide()
        mw.label_kmplayer_path.hide()
        mw.lineEdit.hide()
        mw.pushButton_kmplay.hide()
        mw.pushButton.hide()
        mw.pushButton_open.hide()
        mw.label_choose_chrome.show()
        mw.comboBox_chrome.show()