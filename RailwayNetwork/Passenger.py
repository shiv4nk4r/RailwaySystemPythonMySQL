import mysql.connector as mysql
from Animations import Animations
from DB_Connection import DB_Connection
class Passenger:

	def __init__(self, Name, Pass, Age, UserID):
		self.Name = Name
		self.Pass = Pass
		self.Age = Age
		self.UserID = UserID
		self.animate = Animations()
		self.DB = DB_Connection()
		self.cursor = self.DB.get_Database()

	def get_Name(self):
		return self.Name

	def get_Pass(self):
		return self.Pass

	def get_Age(self):
		return self.Age

	def get_UserID(self):
		return self.UserID


	def menu(self):
		print("hello %s" % self.Name)
