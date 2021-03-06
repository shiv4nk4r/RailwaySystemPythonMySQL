import sys
import time
import os
from Train import Train
from Station import Station
from Animations import Animations
from Database import Database

class Main:
	def __init__(self):
		self.clear()
		self.animate = Animations()
		self.animate.dots(4)
		print ("Getting you online")
		self.animate.dots(3)
		self.DB = Database()

	def clear(self): 
		os.system('cls' if os.name=='nt' else 'clear')

if __name__ == "__main__":
	obj = Main()
	print("Starting the Software")
	obj.animate.dots(4)
	obj.clear()
	print("Enter your choice")
	print("1.Login")
	print("2.Register")
	print("3.Admin Login")

	choice = raw_input()
	obj.clear()
	if(choice == "1"):
		print("Enter UserID")
		userID = raw_input()
		obj.clear()
		print("Enter Pass")
		password = raw_input()
		obj.clear()
		checked = obj.DB.Login(userID, password)
		obj.clear()
		if(checked != 0):
			print("Welcome, " + str(checked[0]))
			obj.animate.dots(2)
			print("1.Book A Ticekt")
			print("2.Cancel A Ticket")
			print("3.View Ticekts")
			print("0 to Logout")
			print("Enter Your choice:")
			choice_new = raw_input()
			obj.clear()
			if(choice_new == "1"):
				obj.animate.dots(1)
				print("Printing all the stations list with there station no")
				obj.DB.showTable_Details("Stations")
				obj.animate.dots(2)
				print("Enter Source Stations No: ")
				source = raw_input()
				print("Enter destination Station No:")
				destination = raw_input()
				obj.animate.dots(3)
				obj.clear()
				print("Finding the Trains Available")
				obj.animate.dots(5)
				sql = "SELECT * FROM Trains WHERE Source = %s AND Destination = %s"
				val = (str(source), str(destination))
				rows = obj.DB.cursor.execute(sql, val)
				if(rows>0):
					for r in obj.DB.cursor.fetchall():
						if(int(r[3]) > 0):
							print("TrainName " + r[0] + ",Train ID " + r[1])
							print("Seats Available")
							print("Normal, " + str(r[3]))
						else:
							print("TrainName " + r[0] + ",Train ID " + r[1] + ", Seats Full")
						obj.animate.dots(2)
					print("Enter the TrainNo to Book: ")
					trainNo = raw_input()
					obj.clear()
					obj.DB.Book_Ticket(source, destination, userID, trainNo)
					
				else:
					print("Sorry No trains Available")

			elif(choice_new == "2"):
				print("Printing All your Ticekts")
				sql = "SELECT * FROM TICKETS WHERE UserID = %s"
				val = (str(userID))
				rows = obj.DB.cursor.execute(sql, val)
				if(rows>0):
					for r in obj.DB.cursor.fetchall():
						print(r[2])
					print("Enter PNR NO to cancel Ticket")
					cancel_pnr = raw_input()
					sql_new = "SELECT * FROM TICKETS WHERE PNR = %s AND UserID = %s"
					val_new = (str(cancel_pnr), str(userID))
					obj.DB.cursor.execute(sql_new, val_new)
					rows = obj.DB.cursor.fetchall()
					trainNOtoCancel = rows[0][4]
					obj.clear()
					obj.DB.Cancel_Ticket(cancel_pnr, userID, trainNOtoCancel)
				else:
					print("No Booked Tickets")
			elif(choice_new == "3"):
				print("Printing All your Ticekts")
				sql = "SELECT * FROM TICKETS WHERE UserID = %s"
				val = (str(userID))
				rows = obj.DB.cursor.execute(sql, val)
				if(rows>0):
					for r in obj.DB.cursor.fetchall():
						print(r[2])
				else:
					print("No Tickets Booked for userID %s" % userID)
	if(choice == "2"):
		print("Enter Name")
		userName = raw_input()
		print("Enter Pass")
		userPass = raw_input()
		print("Enter Age")
		userAge = raw_input()
		print("UseID is: " + str(obj.DB.Add_Passenger(userName, userPass, userAge)))
	if(choice == "3"):
		print("Enter UserName:")
		userName = raw_input()
		obj.clear()
		print("Enter password:")
		userPass = raw_input()
		obj.clear()
		if(userName=="Admin" and userPass == "123456789"):
			print("Welcome, Admin")
			obj.animate.dots(3)
			print("1.Trains")
			print("2.Stations")
			print("3.Passengers")
			choice = raw_input()
			obj.animate.dots(4)
			if(choice == "1"):
				obj.clear()
				print("1.Add a Train")
				print("2.View All Trains")
				choice_new = raw_input()
				if(choice_new == "1"):
					print("Enter TrainName, Source, Destination, SeatsNormal")
					Tname = raw_input()
					Tsource = raw_input()
					Tdestination = raw_input()
					Tseats = raw_input()
					obj.clear()
					obj.DB.Add_Train(Tname, Tsource, Tdestination, 10, Tseats)
				elif(choice_new == "2"):
					obj.clear()
					print("TrainNo, TrainName, SeatsWaiting, SeatsNormal, Source, Destination")
					obj.DB.showTable_Details("Trains")
			elif(choice == "2"):
				obj.clear()
				print("1.Add a Station")
				print("2.View All Stations")
				choice_new = raw_input()
				if(choice_new=="1"):
					print("Enter Station name")
					name = raw_input()
					obj.clear()
					obj.DB.Add_Stations(name)
				elif(choice_new == "2"):
					obj.clear()
					print("Station Name, Station ID")
					obj.DB.showTable_Details("Stations")
			elif(choice == "3"):
				obj.clear()
				print("UserName, password, UserID, Age")
				obj.DB.showTable_Details("Passenger")
		else:
			print("Invalid Credentials, Quitting the application") 