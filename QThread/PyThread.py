from PyQt5 import QtCore, QtWidgets

class Thread(QtCore.QThread):
	mysignal = QtCore.pyqtSignal(str)
	def __init__(self, parent=None):
		QtCore.QThread.__init__(self, parent)

	def run(self):
		for i in range(1,20):
			self.sleep(2)
			self.mysignal.emit("i = {0}".format(i))


class MyWindow(QtWidgets.QWidget):
	def __init__(self, parent=None):
		QtWidgets.QWidget.__init__(self, parent)

		self.label = QtWidgets.QLabel("Press button for start process")
		self.label.setAlignment(QtCore.Qt.AlignHCenter)
		self.button = QtWidgets.QPushButton("Start Process")
		self.vbox = QtWidgets.QVBoxLayout()
		self.vbox.addWidget(self.label)
		self.vbox.addWidget(self.button)
		self.setLayout(self.vbox)

		self.mythread = Thread()
		self.button.clicked.connect(self.on_clicked)
		self.mythread.started.connect(self.on_started)
		self.mythread.finished.connect(self.on_finished)
		self.mythread.mysignal.connect(self.on_change, QtCore.Qt.QueuedConnection)

	def on_clicked(self):
		self.button.setDisabled(True)
		self.mythread.start()

	def on_started(self):
		self.label.setText("Called method 'on_started()'")

	def on_finished(self):
		self.label.setText("Called method 'on_finished()'")
		self.button.setDisabled(False)

	def on_change(self, s):
		self.label.setText(s)

if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	window = MyWindow()
	window.resize(300, 70)
	window.show()

	sys.exit(app.exec_())
