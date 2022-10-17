from FrontEnd.src import *

from .Csys import Hash


class conDBRegister(Hash):
	def __init__(self) -> None:
		super().__init__()
		self.switch = False

	def check_user_exist(self, userName:str):
		if userName in [self._decrypt(i[3]) for i in self.db.fetch()]: return True
		else: return False

	def register_user(self,data:tuple[str,str,str,str]):
		fname, lname, userName, pwd = data		
		user_id = self._id()
		self.db.ins([user_id,  self._encrypt(fname.capitalize()), self._encrypt(lname.capitalize()),
		self._encrypt(userName), self._encrypt(pwd)])
		self.db.create_table(user_id)

class validateRegister(conDBRegister):

	def __init__(self,mainDict: dict):
		
		super().__init__()

		self.errorStyleSheet = 'QLineEdit{border-radius:15px;background-color:#F0F0F0;border:1px solid;border-color:red;}'
		self.normalStyleSheet = 'QLineEdit{border-radius: 15px;background-color: #F0F0F0;border: 1px solid;border-color:#EBEBEB}' 
		self.parent = mainDict['parent']
		self.master = mainDict['master']
		self.firstName:QtWidgets.QLineEdit = mainDict['firstNameEntry']
		self.lastName:QtWidgets.QLineEdit = mainDict['lastNameEntry']
		self.userName:QtWidgets.QLineEdit = mainDict['userNameEntry']
		self.pass1:QtWidgets.QLineEdit = mainDict['passwordEntry']
		self.pass2:QtWidgets.QLineEdit = mainDict['repasswordEntry']
		self.get:QtWidgets.QPushButton = mainDict['registerButton']

	def __get_inputs(self):
		return self.firstName.text(),self.lastName.text(),self.userName.text(), self.pass1.text(), self.pass2.text()

	def checkUqChar(self):
		uqChar = '@_!#$%^&*()<>?-~'
		for letters in list(self.__get_inputs()[3]):
			if uqChar.find(letters) > -1: return False

		return True

	def validate(self):

		for entry in [self.firstName, self.lastName, self.userName, self.pass1, self.pass2]: entry.setStyleSheet(self.normalStyleSheet)

		if any([self.__get_inputs()[0] =='', self.__get_inputs()[1] == '',self.__get_inputs()[2] == '',
		self.__get_inputs()[3] == '',self.__get_inputs()[4] == '']):
			for entry in [self.firstName, self.lastName, self.userName, self.pass1, self.pass2]: 
				entry.setStyleSheet(self.errorStyleSheet)
			message(self.parent, 'Felids empty!','w')
		
		elif len(self.__get_inputs()[2]) < 5:
			message(self.parent,'User name can\'t have less than 5 characters','w')
			self.userName.setStyleSheet(self.errorStyleSheet)

		elif len(self.__get_inputs()[2]) > 30: 
			message(self.parent,'User name can\'t have more than 30 characters','w')
			self.userName.setStyleSheet(self.errorStyleSheet)

		elif self.__get_inputs()[2] == self.__get_inputs()[3]:
			message(self.parent,'Invalid input: User name and password must not be same!','w')

		elif len(self.__get_inputs()[3]) < 8:
			message(self.parent,'Password can\'t have less than 8 characters','w')
			self.pass1.setStyleSheet(self.errorStyleSheet)
	
		elif self.checkUqChar():
			message(self.parent,'Your password must contain special characters like @,#,$ etc.','w')
			self.pass1.setStyleSheet(self.errorStyleSheet)

		elif self.__get_inputs()[3].isnumeric() or self.__get_inputs()[3].isalpha():
			message(self.parent,'Your password must conatin alphabets and numbers.','w')
			self.pass1.setStyleSheet(self.errorStyleSheet)

		elif self.__get_inputs()[3] != self.__get_inputs()[4]:
			message(self.parent,'Password Unmatched!','w')
			self.pass2.setStyleSheet(self.errorStyleSheet)

		else:
			userName = self.__get_inputs()[3]
			if self.check_user_exist(userName):
				message(self.parent,'User already exists! Try loging in.','w')
				self.userName.setStyleSheet(self.errorStyleSheet)

			else:
				self.register_user( self.__get_inputs()[0:4] )
				message(self.parent,'Account successfully created!','s')
				self.switch = True
				for entry in [self.firstName, self.lastName, self.userName, self.pass1, self.pass2]: entry.clear()
