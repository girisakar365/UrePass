import resource

from PyQt5 import Qt, QtCore, QtGui, QtWidgets


def shadow(radius:int):
	shadow  =  Qt.QGraphicsDropShadowEffect()
	shadow.setColor(QtCore.Qt.black)
	shadow.setBlurRadius(radius)
	return shadow

def hide(button,linedit):
	icon = QtGui.QIcon()
	icon.addPixmap(QtGui.QPixmap("Image/show.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
	button.setIcon(icon)
	button.setToolTip('Show')
	linedit.setEchoMode(QtWidgets.QLineEdit.Password)

def show(button,linedit):
	icon = QtGui.QIcon()
	icon.addPixmap(QtGui.QPixmap("Image/hide.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
	button.setIcon(icon)
	linedit.setEchoMode(QtWidgets.QLineEdit.Normal)

def message(master, msg:str, type:str):
	_frame = QtWidgets.QFrame(master)
	_frame.resize(350, 80)

	_frame.setGraphicsEffect(shadow(200))

	close = QtWidgets.QPushButton(_frame)
	close.setGeometry(QtCore.QRect(250, 6, 15, 10))
	close_ico = QtGui.QIcon()
	close_ico.addPixmap(QtGui.QPixmap("Image/cancel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
	close.setIcon(close_ico)
	if type.upper() == 'W': 
		_frame.setStyleSheet('background-color: #410910; color:#ffffff;border-radius:15px;')
		close.setStyleSheet('''QPushButton{
background-color: #410910;
border-radius: 2px;
}
QPushButton:hover{
background-color:#a00000;
}''')
	elif type.upper() == 'S': 
		_frame.setStyleSheet('background-color: #49ab81; color:#ffffff; border-radius:15px;')
		close.setStyleSheet('''QPushButton{
background-color:#49ab81;
border-radius: 2px;
}
QPushButton:hover{
background-color:#52bf90;
}''')
	elif type.upper() == 'A':
		_frame.setStyleSheet('background-color: #FDD835; color:#24292E; border-radius:15px;')
		close.setStyleSheet('''QPushButton{
	background-color:#FDD835;
border-radius: 2px;
}
QPushButton:hover{
background-color:#AA9530;
}''')
	
	close.setIconSize(QtCore.QSize(16,16))
	close.move(320,4)
	close.clicked.connect(_frame.hide)

	lable = QtWidgets.QLabel(msg, _frame)
	font = QtGui.QFont()
	font.setFamily('Segoe UI Light')
	font.setPointSize(10)
	lable.setFont(font)
	lable.move(8,20)
	lable.resize(300, 20 + len(msg))
	lable.setWordWrap(True)

	time = QtCore.QTimer(_frame)
	time.timeout.connect(_frame.hide)
	time.start(10000)

	_frame.move(200,520)
	_frame.show()

	return _frame