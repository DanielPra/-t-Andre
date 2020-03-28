import sys
from PyQt5.QtGui import QApplication
from PyQt5.QtCore import QUrl
from PyQt5.QtWebKit import QWebPage
import bs4 as bs
import urllib.request


class Client(QWebPage):

    def __init__(self, url):
        self.app = QApplication(sys.argv)
        QWebpage.__init__(self)
        self.loadFinished.connect(self.on_page_load)
        self.mainFrame().load(QUrl(url))
        self.app.exec_()

    def on_page_load(self):
        self.app.quit()



url = 'https://pythonprogramming.net/parsememcparseface'
client_response = Client(url)
source = client_response.mainFrame().toHtml()
