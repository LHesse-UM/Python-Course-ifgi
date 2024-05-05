# import necessary modules
from qgis.PyQt.QtCore import QUrl
from qgis.PyQt.QtWebKitWidgets import QWebView

# Create an instance of QWebView
myWV = QWebView(None)

# Loading url and displaying the pop up window
myWV.load(QUrl('https://wikipedia.org/wiki/[%name%]'))
myWV.show()
