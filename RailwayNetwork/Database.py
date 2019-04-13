import mysql.connector as mysql
import sys
from Station import Station
from Train import Train
from Passenger import Passenger
from Ticket import Ticket
from DB_Connection import DB_Connection
from Animations import Animations
import random 

class Database:

	global animate

	def Update_Trains_List(self):
		self.cursor.execute("SELECT * FROM Trains")
		Trains_List_Temp = []
		for row in self.cursor.fetchall():
			T1 = Train(row[2], row[3], row[0], row[4], row[5])
			Trains_List_Temp.append(T1)
		self.Trains_List =  Trains_List_Temp

	def Update_Stations_List(self):
		Station_List_temp = []
		self.cursor.execute("SELECT * FROM Stations")
		for row in self.cursor.fetchall():
			S1 = Station(row[0], row[1])
			Station_List_temp.append(S1)
		self.Stations_List = Station_List_temp

	def Update_Passenger_List(self):
		Passenger_List_temp = []
		self.cursor.execute("SELECT * FROM Passenger")
		for row in self.cursor.fetchall():
			U1 = Passenger(row[0], row[1], row[3], row[2])
			Passenger_List_temp.append(U1)
		self.Passenger_List =  Passenger_List_temp

	def Update_Ticket_List(self):
		Ticket_List_Temp = []
		self.cursor.execute("SELECT * FROM TICKETS")
		for row in self.cursor.fetchall():
			Tick1 = Ticket(row[0], row[1], row[2], row[3], row[4])
			Ticket_List_Temp.append(Tick1)
		self.Tickets_List = Update_Ticket_List

	def set_Trains_List(self, Train_List_temp):
		self.Trains_List = Train_List_temp

	def set_Stations_List(self, Stations_List_temp):
		self.Stations_List = Stations_List_temp

	def set_User_List(self, Passenger_List_Temp):
		self.Passenger_List = Passenger_List_Temp

	def __init__(self):
		self.Trains_List = []
		self.Stations_List = []
		self.Passenger_List = []
		self.Tickets_List = []

		print("Trying to connect to Database")
		self.animate = Animations()
		self.animate.dots(3)
		self.DB = DB_Connection()
		self.cursor = self.DB.get_Database()
		self.Update_Passenger_List()
		self.Update_Stations_List()
		self.Update_Trains_List()

	def showTable_Details(self, Name):
		print("Showing details of table %s" % Name)
		self.animate.dots(3)
		self.cursor.execute("SELECT * FROM %s" % Name)
		for row in self.cursor.fetchall():
			print(" ".join(map(str,row)))

	def showTable_Format(self, Name):
		print("Showing format for %s" %Name)
		self.animate.dots(3)
		self.cursor.execute("DESCRIBE %s" % Name)
		for row in self.cursor.fetchall():
			print(row[0] + " " + row[1])

	def show_Tables(self):
		self.cursor.execute("SHOW TABLES")
		print("Showing the list of tables")
		self.animate.dots(3)
		i = 1
		for row in self.cursor.fetchall():
			print("%d.%s" % (i, row[0]))
			i=i+1

	def Add_Train(self, Train_Name, Source, Destination, SeatsSleeper, SeatsNormal):
		T1 = Train(SeatsSleeper, SeatsNormal, Train_Name, Source, Destination)
		sql = "INSERT INTO Trains (TrainName, TrainID, SeatsSleeper, SeatsNormal, Source, Destination) VALUES (%s, %s, %s, %s, %s, %s)"
		index = len(self.Trains_List) + 1
		val = (Train_Name, str(index), str(SeatsSleeper), str(SeatsNormal), str(Source), str(Destination))
		self.cursor.execute(sql, val)
		self.DB.db.commit()
		print ("Record inserted successfully into table")
		self.Trains_List.append(T1)

	def Add_Stations(self, StationName):
		index = len(self.Stations_List) + 1
		S1 = Station(StationName, index)
		sql = "INSERT INTO Stations (StationName, StationNo) VALUES (%s, %s)"
		val = (StationName, str(index))
		self.cursor.execute(sql, val)
		self.DB.db.commit()
		print ("Record inserted successfully into table")
		self.Stations_List.append(S1)

	def Add_Passenger(self, Name, Pass, Age):
		index = len(self.Passenger_List) + 1
		sql = "INSERT INTO Passenger (UserName, Password, UserID, Age) VALUES (%s,%s,%s,%s)"
		val = (Name, Pass, str(index), str(Age))
		self.cursor.execute(sql, val)
		self.DB.db.commit()
		print ("Record inserted successfully into table")
		U1 = Passenger(Name, Pass, Age, index)
		self.Passenger_List.append(U1)
		return index

	def Book_Ticket(self, Source, Destination, UserID, TrainNo):
		PNRNO = "PNR" + str(format(random.randint(int(UserID), 500), '05d'))
		sql = "INSERT INTO TICKETS (Source, Destination, PNR, UserID, TrainNo) VALUES (%s, %s, %s, %s, %s)"
		val = (str(Source), str(Destination), PNRNO, str(UserID), str(TrainNo))
		self.cursor.execute(sql,val)
		self.DB.db.commit()
		self.Tickets_List.append(Ticket(Source, Destination, PNRNO, UserID, TrainNo))

		sql = "SELECT * FROM Trains WHERE TrainID = %s"
		val = (str(TrainNo))
		self.cursor.execute(sql,val)
		Seats = int(self.cursor.fetchall()[0][3])
		sql = "UPDATE Trains SET SeatsNormal = %s WHERE TrainID = %s"
		val = (str(Seats-1),TrainNo)
		self.cursor.execute(sql,val)
		self.DB.db.commit()

		print("TrainBooked successfully")
		print("Your PNR NO: " + PNRNO)

		return PNRNO

	def Cancel_Ticket(self, PNRNO, userID, TrainNo):
		sql = "DELETE FROM TICKETS WHERE PNR = %s AND UserID = %s"
		val = (PNRNO, str(userID))
		self.cursor.execute(sql, val)
		self.DB.db.commit()
		sql = "INSERT INTO CanceledTickets (PNRNO, UserID, TrainNo) VALUES (%s, %s, %s)"
		val = (PNRNO, str(userID), str(TrainNo))
		self.cursor.execute(sql,val)
		self.DB.db.commit()

		sql = "SELECT * FROM Trains WHERE TrainID = %s"
		val = (str(TrainNo))
		self.cursor.execute(sql,val)
		Seats = int(self.cursor.fetchall()[0][3])
		sql = "UPDATE Trains SET SeatsNormal = %s WHERE TrainID = %s"
		val = (str(Seats+1),TrainNo)
		self.cursor.execute(sql,val)
		self.DB.db.commit()
		print("successfully Canceled a Ticket")

	def Login(self,userID, Pass):
		sql="SELECT * FROM Passenger WHERE UserID = %s AND Password = %s"
		val=(str(userID),Pass)
		rows = self.cursor.execute(sql, val)
		if(rows > 0):
			print("LoggedIn")
			self.animate.dots(3)
			index = int(userID) - 1
			return (self.Passenger_List[index].get_Name(),1)
		else:
			print("UserID ans Password does nto appear to be correct")
			return 0


if __name__ == "__main__":
	obj = Database()
	obj.Add_Stations("Kashmir")