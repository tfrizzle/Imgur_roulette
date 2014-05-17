# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtWebKit import QWebView
from imgur_support import gen_url

class Imgur_roulette(QtGui.QWidget):
    
	def __init__(self):
		super(Imgur_roulette, self).__init__()
		
		self.initUI()
		
	def initUI(self):
		# app geometry
		self.setGeometry(300, 300, 880, 720)
		self.setWindowTitle('mgr_rltt')
		self.setWindowIcon(QtGui.QIcon('icon.png'))
		
		# layouts declared
		layout = QtGui.QVBoxLayout()
		blayout = QtGui.QHBoxLayout()
		
		# views and buttons declared
		view = Imgur_view()
		gen_btn = QtGui.QPushButton('generate', self)
		quit_btn = QtGui.QPushButton('quit', self)

		# button clicks
		gen_btn.clicked.connect(view.gen_img)
		quit_btn.clicked.connect(QtCore.QCoreApplication.instance().quit)

		# button layout format
		blayout.addWidget(gen_btn)
		blayout.addWidget(quit_btn)
		blayout.addStretch(1)		
		
		# main layout format
		layout.addLayout(blayout)
		layout.addWidget(view)

		self.setLayout(layout)
		self.show()
		
class Imgur_view(QWebView):

	def __init__(self):
		QWebView.__init__(self)	
		self.load(QtCore.QUrl(gen_url()))

	def gen_img(self):
		self.load(QtCore.QUrl(gen_url()))
		
def main():
	app = QtGui.QApplication(sys.argv)
	ex = Imgur_roulette()

	sys.exit(app.exec_())

if __name__ == '__main__':
    main()
