import time

class Animations:
	def dots(self, x):
		for i in range(1,x):
			print(".")
			time.sleep(0.5)