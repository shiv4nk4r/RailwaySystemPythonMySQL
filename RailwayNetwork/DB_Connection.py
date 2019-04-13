import MySQLdb
import sys

class DB_Connection:

	def get_Database(self):
		return self.cur

	def __init__(self):
		DB_Host = "localhost"
		DB_User = "root"
		DB_pass = "root"
		DB_Name = "railways"
		try:
			self.db = MySQLdb.connect(DB_Host, DB_User, DB_pass, DB_Name)
			self.cur = self.db.cursor()
			print("Succesfully connected To Database")
		except Exception as e:
			print("Not Able to connect to Database")
		