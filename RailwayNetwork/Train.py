class Train:
	def __init__(self, Seats_AvailableSleeper, Seats_AvailableNormal, Train_Name, Source, Destination):
		self.Seats_AvailableSleeper = Seats_AvailableSleeper
		self.Seats_AvailableNormal = Seats_AvailableNormal
		self.Train_Name = Train_Name
		self.Source = Source
		self.Destination = Destination
		self.TrainNo = None

	def get_Date(self):
		return self.Date

	def get_Seats_AvailableSleeper(self):
		return self.Seats_AvailableSleeper

	def get_Seats_AvailableNormal(self):
		return self.Seats_AvailableNormal

	def get_TrainNo(self):
		return self.TrainNo

	def get_Source(self):
		return self.Source

	def get_Destination(self):
		return self.Destination

	def get_Train_Name(self):
		return self.Train_Name